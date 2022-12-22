use std::io;

fn main() {
    println!("Enter a line of text:");

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    println!("You entered: {}", input);
}
