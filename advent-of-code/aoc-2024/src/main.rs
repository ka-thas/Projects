use std::fs::read_to_string;

const WORD: &str = "MAS";
const DIRECTIONS: [(i32, i32); 4] = [
    (1, 1),   // Down-right (diagonal)
    (-1, -1), // Up-left (diagonal)
    (1, -1),  // Down-left (diagonal)
    (-1, 1),  // Up-right (diagonal)
];

fn main() {
    let input = read_to_string("input4.txt").expect("Failed to read input file");
    let grid: Vec<Vec<char>> = input.lines().map(|line| line.chars().collect()).collect();

    let mut found_coords = Vec::new();
    let mut found_coords2 = Vec::new();
    for row in 0..grid.len() {
        for col in 0..grid[row].len() {
            let mut i = 0;
            for &(dir_r, dir_c) in &DIRECTIONS {
                if find_word(&grid, row, col, dir_r, dir_c, WORD) {
                    found_coords.push((row, col));
                    if i == 0 {
                        // down-right
                        if find_word(&grid, row, col + 2, 1, -1, WORD)
                            || find_word(&grid, row + 2, col, -1, 1, WORD)
                        {
                            found_coords2.push((row, col));
                        }
                    }
                    if i == 1 {
                        // up-left
                        if find_word(&grid, row, col - 2, 1, -1, WORD)
                            || find_word(&grid, row - 2, col, -1, 1, WORD)
                        {
                            found_coords2.push((row, col));
                        }
                    }
                    if i == 2 {
                        // down-left
                        if find_word(&grid, row - 2, col, 1, 1, WORD)
                            || find_word(&grid, row, col + 2, -1, -1, WORD)
                        {
                            found_coords2.push((row, col));
                        }
                    }
                    if i == 3 {
                        // up-right
                        if find_word(&grid, row, col - 2, 1, 1, WORD)
                            || find_word(&grid, row + 2, col, -1, -1, WORD)
                        {
                            found_coords2.push((row, col));
                        }
                    }
                }
                i += 1;
            }
        }
    }

    for (row, col) in found_coords2.iter() {
        println!("Found X-MAS starting at ({}, {})", row, col);
    }
    println!("{}", found_coords2.len())
}

fn find_word(grid: &[Vec<char>], row: usize, col: usize, dr: i32, dc: i32, word: &str) -> bool {
    let mut r = row as i32;
    let mut c = col as i32;

    for ch in word.chars() {
        if r < 0 || r >= grid.len() as i32 || c < 0 || c >= grid[0].len() as i32 {
            return false;
        }
        if grid[r as usize][c as usize] != ch {
            return false;
        }
        r += dr;
        c += dc;
    }
    true
}
