use std::collections::VecDeque;

fn list1(list: &[i32]) {
    println!("{:?}", list);
}
fn list2(list: &Vec<i32>) {
    println!("{:?}", list);
}

fn main() {
    let my_list: Vec<i32> = vec![1, 2, 3, 4];
    let my_other_list: [i32; 4] = [1, 2, 3, 4];
    let mut my_deque: VecDeque<i32> = VecDeque::new();

    for i in (11..19) {
        my_deque.push_back(i);
    }
    for i in (8..11).rev() {
        my_deque.push_front(i);
    }

    let (front, back) = my_deque.as_slices();

    list1(&my_list); // Passing a slice of the vector
    list1(&front); // Passing a slice of the deque
    list1(&back); // Passing a slice of the deque
    list2(&my_list); // Passing a slice of the array
                     // list2(&my_other_list); // This would not work because my_other_list is an array
    println!("{:?}", my_deque);
}
