// Day 13
// doesn't work yet

// AX + BX = PX
// AY + BY = PY

use std::fs;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let input = fs::read_to_string("./src/input13.txt")?;
    let mut stored_input = Vec::new();
    for i in input.split("\n") {
        stored_input.push(i);
    }

    let mut sum = 0;

    for i in (0..stored_input.len()).step_by(4) {
        let a: Vec<i64> = stored_input[i]
            .split(|c: char| !c.is_numeric()) // Split by any non-numeric character
            .filter_map(|s| s.parse::<i64>().ok()) // Parse each part to i64, ignoring non-numbers
            .collect();
        let b: Vec<i64> = stored_input[i + 1]
            .split(|c: char| !c.is_numeric()) // Split by any non-numeric character
            .filter_map(|s| s.parse::<i64>().ok()) // Parse each part to i64, ignoring non-numbers
            .collect();
        let z: Vec<i64> = stored_input[i + 2]
            .split(|c: char| !c.is_numeric()) // Split by any non-numeric character
            .filter_map(|s| s.parse::<i64>().ok()) // Parse each part to i32, ignoring non-numbers
            .collect();

        let tokens = solve(
            a[0],
            a[1],
            b[0],
            b[1],
            z[0] + 10000000000000,
            z[1] + 10000000000000,
        ); // remove 10000000000000 for part 1
        sum += tokens
    }
    println!("sum: {}", sum);

    Ok(())
}

fn solve(x1: i64, x2: i64, y1: i64, y2: i64, z1: i64, z2: i64) -> i64 {
    let b = (z2 * x1 - z1 * x2) / (y2 * x1 - y1 * x2);
    let a = (z1 - b * y1) / x1;
    if (x1 * a + y1 * b, x2 * a + y2 * b) != (z1, z2) {
        return 0;
    }
    a * 3 + b
}
