fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    for i in 0..nums.len() {
        for j in i + 1..nums.len() {
            if nums[i] + nums[j] == target {
                return vec![i as i32, j as i32];
            }
        }
    }
    vec![]
}

fn main() {
    let vector = vec![2, 4, 7, 3, 6, 1];
    println!("{:?}", two_sum(vector, 3));
}
