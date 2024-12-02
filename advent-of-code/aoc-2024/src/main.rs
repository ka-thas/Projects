use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

//part 2
fn main() -> io::Result<()> {
    let path = Path::new("src/input2.txt");
    let input = File::open(path)?;
    let reader = io::BufReader::new(input);

    let mut num_safe = 0;

    'outer: for line in reader.lines() {
        let line = line?;
        let temp_numbers = line
            .split_whitespace()
            .map(|num| num.parse::<i32>().unwrap());

        let mut numbers = Vec::new();
        for num in temp_numbers {
            numbers.push(num);
        }

        println!("{:?}", numbers);

        // code logic
        let i = 1;
        let mut j = 0;
        let is_increasing = numbers[i] - numbers[j] > 0;

        println!("{}", is_increasing);

        for i in 1..numbers.len() {
            if (numbers[i] - numbers[j] > 0) != is_increasing {
                continue 'outer;
            } else if (numbers[i] - numbers[j]).abs() == 0 || (numbers[i] - numbers[j]).abs() > 3 {
                continue 'outer;
            }

            j += 1;
        }
        num_safe += 1;
        println!("num safe!")
    }

    println!("{}", num_safe);

    Ok(())
}
