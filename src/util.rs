use std::fs;

use std::fs::File;
use std::io::Write;

pub fn read_from_file(file_path: &String) -> String {
    let contents: String = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    return contents;
}

pub fn write_to_file(file_path: &String, file_contents: &String) {
    let mut f = File::create(file_path).expect("Unable to create file");

    f.write_all(file_contents.as_bytes()).expect("Unable to write data");
}