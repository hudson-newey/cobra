mod util;
mod functions;

use std::env;

fn main() {
    let files: Vec<String> = env::args().collect();
    let file_contents: String = util::read_from_file(&files[1]);

    let mut file_processing_out = functions::replace_functions(file_contents);

    println!("{}", file_processing_out);

    util::write_to_file(
        &(files[1]).replace(".pyc", ".py"),
        &file_processing_out
    )
}
