mod read_file;
mod functions;

use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let file_contents: String = read_file::read_from_file(&args[1]);

    let mut file_processing = functions::replace_functions(file_contents);

    println!("{}", file_processing);
}
