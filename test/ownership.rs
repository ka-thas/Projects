// Rust borrow checker

fn main() {
    let mut x = 42;

    // Immutable borrows
    let r1 = &x;
    let r2 = &x;
    println!("r1: {}, r2: {}", r1, r2); // OK: Using immutable borrows

    // Mutable borrow
    let r3 = &mut x; // No error: r1 and r2 are no longer used
    *r3 += 1; // Modifying x through the mutable borrow
    println!("r3: {}", r3); // OK: using mutable borrow
}
