extern crate regex;

use regex::Regex;

pub fn check_casing(code: String) {
    let edited_code = &(code.as_str());

    let camel_casing_re = Regex::new(r"[a-z][A-Z]").unwrap();
    let is_camel_case = camel_casing_re.is_match(edited_code.clone());

    let snake_casing_re = Regex::new(r"[a-z]_[a-z]").unwrap();
    let is_snake_case = snake_casing_re.is_match(edited_code.clone());

    if is_camel_case && is_snake_case {
        println!("Warning: use of inconsistant casing...");
    };
}