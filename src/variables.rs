use lazy_static::lazy_static;
use regex::Regex;

pub fn check_variables(code: String) -> String {
    let adjusted_code = remove_keywords(code.clone());

    if check_variable_type(code.clone()) != true { throw_variable_error("mismatched variable type assignment..."); }
    if check_variable_assignment(code.clone()) != true { throw_variable_error("assignment to constant variable..."); }

    return adjusted_code;
}

fn remove_keywords(code: String) -> String {
    return code.replace("const ", "");
}

fn check_variable_type(code: String) -> bool {
    find_matches(&code);
    return true;
}

fn check_variable_assignment(code: String) -> bool {
    return true;
}

fn throw_variable_error(error_message: &str) {
    println!("Variable Error: {}", error_message);
    std::process::exit(1);
}

fn find_matches(haystack: &str) {
    let pattern = r#"(?P<strings> string)"#;
    let mut matches: Vec<(String, (usize, usize))> = vec![];

    let re = Regex::new(pattern).unwrap();
    // We skip the first capture group, which always corresponds
    // to the entire pattern and is unnamed. Otherwise, we assume
    // every capturing group has a name and corresponds to a single
    // alternation in the regex.
    let group_names: Vec<&str> =
        re.capture_names().skip(1).map(|x| x.unwrap()).collect();
    for caps in re.captures_iter(haystack) {
        for name in &group_names {
            if let Some(m) = caps.name(name) {
                matches.push((name.to_string(), (m.start(), m.end())));
            }
        }
    }

    println!("{:?}", matches);
}