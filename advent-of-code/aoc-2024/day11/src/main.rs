use std::error::Error;
use std::fs;

fn main() -> Result<(), Box<dyn Error>> {
    let mut stones = Vec::new();
    let input: String = fs::read_to_string("./src/input11.txt")?;
    let input = input
        .split_whitespace()
        .map(|num| num.parse::<u64>().unwrap());
    for num in input {
        stones.push(num)
    }

    for i in 0..75 {
        let mut new_stones = Vec::new();
        for stone in stones.iter() {
            if *stone == 0 {
                new_stones.push(1);
                continue;
            }
            let stone_str = stone.to_string();
            if stone_str.len() % 2 == 0 {
                let new_lengths = stone_str.len() / 2;
                let left = stone_str[..new_lengths].parse::<u64>().unwrap();
                let right = stone_str[new_lengths..].parse::<u64>().unwrap();
                new_stones.push(left);
                new_stones.push(right);
            } else {
                new_stones.push(stone * 2024);
            }
        }
        stones = new_stones;
        println!("{}", i)
    }
    println!("{}", stones.len());

    Ok(())
}
