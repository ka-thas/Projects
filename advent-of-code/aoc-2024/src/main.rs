// Day 12

use std::error::Error;
use std::fs;

fn main() -> Result<(), Box<dyn Error>> {
    let input: String = fs::read_to_string("./src/input12.txt")?;
    let input = input
    let mut grid: Vec<Vec<char>> = 



    Ok(())
}
