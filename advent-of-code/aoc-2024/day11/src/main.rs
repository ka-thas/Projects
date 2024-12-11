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
        let mut new_stones = Vec::with_capacity(stones.len() * 2);
        for stone in stones.iter() {
            if *stone == 0 {
                new_stones.push(1);
                continue;
            }
            let temp = stone.ilog10() + 1; // i64.ilog10() is available in Rust 1.67+
            if temp % 2 == 0 {
                let a = stone / 10_u64.pow((temp / 2) as u32);
                let b = stone % 10_u64.pow((temp / 2) as u32);
                new_stones.push(a);
                new_stones.push(b);
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
