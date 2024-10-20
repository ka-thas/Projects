use std::convert::TryInto;

fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
    let mut result: Vec<i32> = Vec::<i32>::with_capacity((m + n).try_into().unwrap());
    let mut i: usize = 0;
    let mut j: usize = 0;
    let m: usize = m.try_into().unwrap();
    let n: usize = n.try_into().unwrap();

    while i < m && j < n {
        if nums2[j] < nums1[i] {
            result.push(nums2[j]);
            j += 1;
            continue;
        }
        result.push(nums1[i]);
        i += 1;
    }

    while i < m {
        result.push(nums1[i]);
        i += 1;
    }
    while j < n {
        result.push(nums2[j]);
        j += 1;
    }

    for (k, num) in result.iter().enumerate() {
        nums1[k] = *num;
    }
}

fn main() {
    let mut nums1: Vec<i32> = vec![1, 3, 6, 7, 8, 0, 0, 0, 0, 0];
    let mut nums2: Vec<i32> = vec![2, 5, 6, 8, 10];

    merge(&mut nums1, 5, &mut nums2, 5);
}
