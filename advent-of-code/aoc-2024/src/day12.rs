// Day 12
// doesn't work

use std::collections::HashMap;
use std::error::Error;
use std::fs;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let input: String = fs::read_to_string("./src/input12.txt")?;
    println!("{}", input);
    let mut grid: Vec<Vec<char>> = Vec::new();
    for line in input.split("\n") {
        let mut row = Vec::new();
        for c in line.chars() {
            row.push(c);
        }
        grid.push(row);
    }
    println!("{:?}", grid);

    let M = grid.len();
    let N = grid[0].len();

    let mut area: HashMap<char, i32> = HashMap::new();
    let mut perimeter: HashMap<char, i32> = HashMap::new();

    for (i, row) in grid.iter().enumerate() {
        for (j, col) in row.iter().enumerate() {
            *area.entry(*col).or_insert(0) += 1;

            let mut edges = 0;
            if i == 0 || i == M - 1 {
                // Upper or lower edge
                edges += 1;
            }
            if j == 0 || j == N - 1 {
                // Right or left edge
                edges += 1;
            }
            if i > 0 && grid[i - 1][j] != *col {
                // Up
                edges += 1;
            }
            if i < M - 1 && grid[i + 1][j] != *col {
                // Down
                edges += 1;
            }
            if j > 0 && grid[i][j - 1] != *col {
                // left
                edges += 1;
            }
            if j < N - 1 && grid[i][j + 1] != *col {
                // right
                edges += 1;
            }
            *perimeter.entry(*col).or_insert(0) += edges;
        }
    }

    println!("{:?}", area);
    println!("{:?}", perimeter);

    let mut sum = 0;
    for (key, value) in &area {
        sum += value * perimeter.get(key).unwrap();
    }

    println!("{}", sum);

    Ok(())
}
