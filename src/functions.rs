extern crate regex;

use regex::Regex;

pub fn replace_functions(file_contents: String) -> String {
    let replaced_file_contents = Regex::new("^fn ").unwrap()
        .replace(file_contents.as_str(), "def ").to_string();

    return replaced_file_contents;
}