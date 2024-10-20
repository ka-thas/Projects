use std::collections::VecDeque;

fn plus_one(digits: Vec<i32>) -> Vec<i32> {
    let mut deque: VecDeque<i32> = VecDeque::from(digits);

    let mut ptr = deque.len();
    loop {
        if ptr == 0 {
            deque.push_front(1);
            break;
        }
        ptr -= 1;
        deque[ptr] = (deque[ptr] + 1) % 10;
        if deque[ptr] != 0 {
            break;
        }
    }
    Vec::from(deque)
}

fn main() {
    let digits = vec![9, 9, 8, 9, 9, 9];

    let result = plus_one(digits);

    println!("{:?}", result);
}
