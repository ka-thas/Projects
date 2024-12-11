use regex::Regex;
use std::fs::read_to_string;

fn main() {
    // Read the content of the file into a string
    let input = read_to_string("./src/input3.txt").expect("Failed to read the file");

    // Define the regex pattern for "mul(<number>,<number>)"
    let re = Regex::new(r"mul\(\s*\d+\s*,\s*\d+\s*\)").expect("Failed to compile regex");

    // Find all matches in the input
    for cap in re.find_iter(&input) {
        println!("Found match: {}", cap.as_str());
    }
}
