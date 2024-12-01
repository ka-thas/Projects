use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() -> io::Result<()> {
    let path = Path::new("input1.txt");
    let input = File::open(path)?;
    let reader = io::BufReader::new(input);

    let mut column1 = Vec::new();
    let mut column2 = Vec::new();

    for line in reader.lines() {
        let line = line?;
        let mut numbers = line
            .split_whitespace()
            .map(|num| num.parse::<i32>().unwrap());

        if let Some(num1) = numbers.next() {
            column1.push(num1);
        }
        if let Some(num2) = numbers.next() {
            column2.push(num2);
        }
    }

    column1.sort();
    column2.sort();

    println!("{:?}", column1);
    println!("{:?}", column2);

    let mut sum = 0;
    for i in 0..column1.len() {
        sum += (column1[i] - column2[i]).abs();
    }

    println!("{}", sum);

    Ok(())
}
