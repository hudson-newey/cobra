extern crate regex;

use regex::Regex;

pub fn replace_functions(file_contents: String) -> String {
    let re = Regex::new(r"(?P<y>^fn )").unwrap();
    return re.replace_all(&file_contents, "def ").to_string();
    // return file_contents.replace("fn", "def");
}