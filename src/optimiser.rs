fn remove_empty_lines(code: String) -> String {
    return code.replace("\n", "")
            .replace(";", "\n");
}

fn replace_method_assignments(code: String) -> String {
    let method_type_assignments = vec!["list()", "int()", "str()", "tuple()"];
    let empty_type_assignments = vec!["[]", "0", "\"\"", "()"];

    let mut i: u8 = 0;
    let mut code_out: String = code;

    for method in method_type_assignments {
        code_out = code_out.replace(method, empty_type_assignments[i as usize]);
        i += 1;
    }

    return code_out;
}

pub fn optimise(code: String) -> String {
    let mut new_code: String = code;

    new_code = replace_method_assignments(new_code);
    new_code = remove_empty_lines(new_code);
    
    return new_code;
}