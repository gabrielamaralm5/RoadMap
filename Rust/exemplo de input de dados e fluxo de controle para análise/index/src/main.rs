use std::io;

fn convert_to_int(data_input:& str) -> i32{
    let x data_input.trim().parse()::<i32>().unwrap();
    x
}

fn main() {
    println!("Hello, world!");
}
