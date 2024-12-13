// Day 13
// doesn't work yet

use std::fs;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let input = fs::read_to_string("./src/input13.txt")?;
    let mut stored_input = Vec::new();
    for i in input.split("\n") {
        stored_input.push(i);
    }

    let mut sum = 0;

    for i in (0..stored_input.len()).step_by(4) {
        let button_a: Vec<i32> = stored_input[i]
            .split(|c: char| !c.is_numeric()) // Split by any non-numeric character
            .filter_map(|s| s.parse::<i32>().ok()) // Parse each part to i32, ignoring non-numbers
            .collect();
        let button_b: Vec<i32> = stored_input[i + 1]
            .split(|c: char| !c.is_numeric()) // Split by any non-numeric character
            .filter_map(|s| s.parse::<i32>().ok()) // Parse each part to i32, ignoring non-numbers
            .collect();
        let prize: Vec<i32> = stored_input[i + 2]
            .split(|c: char| !c.is_numeric()) // Split by any non-numeric character
            .filter_map(|s| s.parse::<i32>().ok()) // Parse each part to i32, ignoring non-numbers
            .collect();

        let mut tokens_list: Vec<i32> = Vec::from([0]);

        /* println!("{:?}", button_a);
        println!("{:?}", button_b);
        println!("{:?}", prize); */

        for b in 0..=100 {
            let x_pos = button_b[0] * b;
            let y_pos = button_b[1] * b;

            if x_pos > prize[0] || y_pos > prize[1] {
                break;
            }

            for a in 0..=100 {
                let x_pos = x_pos + button_a[0] * a;
                let y_pos = y_pos + button_a[1] * a;

                // println!("{}, {}", x_pos, y_pos);
                if x_pos > prize[0] || y_pos > prize[1] {
                    // println!("");
                    break;
                }
                if x_pos == prize[0] && y_pos == prize[1] {
                    // println!("WIN! {}, {} -> {}", a, b, a + b);
                    tokens_list.push(3 * a + b);
                }
            }
        }
        sum += tokens_list.pop().unwrap();
    }
    println!("{}", sum);

    Ok(())
}
