use std::io;
use std::thread;
use std::time::Duration;

fn main() {
    println!("Enter the countdown time in seconds:");

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let countdown_time: u64 = input.trim().parse().unwrap();

    for i in (1..=countdown_time).rev() {
        println!("{} seconds remaining...", i);
        thread::sleep(Duration::from_secs(1));
    }

    println!("Time's up!");
}
