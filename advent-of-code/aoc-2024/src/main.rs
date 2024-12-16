// Day 16
// doesn't work yet

use std::cmp::Ordering;
use std::collections::BinaryHeap;
use std::error::Error;
use std::fs;

const DIRECTIONS: [(i32, i32); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)]; // 0: right, 1: down, 2: left, 3: up

fn main() -> Result<(), Box<dyn Error>> {
    let input = fs::read_to_string("./src/input16.txt")?;
    let grid: Vec<Vec<bool>> = input
        .lines()
        .map(|line| {
            line.chars()
                .map(|c| match c {
                    '#' => false,
                    _ => true,
                })
                .collect()
        })
        .collect();

    let rows = grid.len();
    let cols = grid[0].len();

    let start = (rows - 2, 1);
    let goal = (1, cols - 2);

    match bfs_with_priority_queue(&grid, start, goal) {
        Some(cost) => println!("Minimum cost to reach the goal: {}", cost),
        None => println!("Goal is unreachable."),
    }

    Ok(())
}

#[derive(Copy, Clone, Eq, PartialEq)]
struct State {
    cost: usize,
    position: (usize, usize),
    direction: usize, // 0: right, 1: down, 2: left, 3: up
}

// Reverse the ordering for BinaryHeap (min-heap behavior)
impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        other.cost.cmp(&self.cost) // Reverse order for min-heap
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

fn bfs_with_priority_queue(
    grid: &[Vec<bool>],
    start: (usize, usize),
    goal: (usize, usize),
) -> Option<usize> {
    let rows = grid.len();
    let cols = grid[0].len();

    let mut visited = vec![vec![vec![false; 4]; cols]; rows]; // Track visited states for each direction
    let mut heap = BinaryHeap::new();

    heap.push(State {
        cost: 0,
        position: start,
        direction: 0,
    });

    while let Some(State {
        cost,
        position,
        direction,
    }) = heap.pop()
    {
        let (x, y) = position;

        // Reached the goal?
        if position == goal {
            return Some(cost);
        }

        // Visited?
        if visited[x][y][direction] {
            continue;
        }
        visited[x][y][direction] = true;

        // Explore neighbors
        for (dir_index, &(dx, dy)) in DIRECTIONS.iter().enumerate() {
            let new_x = x as i32 + dx;
            let new_y = y as i32 + dy;

            // In bounds and grid passability?
            if new_x >= 0 && new_x < rows as i32 && new_y >= 0 && new_y < cols as i32 {
                let new_pos = (new_x as usize, new_y as usize);
                if grid[new_pos.0][new_pos.1] {
                    // Calculate cost (turning costs 1000 if direction changes)
                    let turn_cost = if dir_index == direction { 0 } else { 1000 };
                    heap.push(State {
                        cost: cost + 1 + turn_cost,
                        position: new_pos,
                        direction: dir_index,
                    });
                }
            }
        }
    }

    None // Goal is unreachable
}
