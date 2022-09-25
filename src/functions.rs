extern crate regex;

use regex::Regex;

pub fn replace_functions(file_contents: String) -> String {
    let re = Regex::new("^fn ").unwrap();
    let replaced_file_contents = re.replace(file_contents.as_str(), "def ").to_string();

    return replaced_file_contents;
}