use std::fs;

pub fn read_from_file(file_path: &String) -> String {
    let contents: String = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    return contents;
}
