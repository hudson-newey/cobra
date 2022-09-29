mod functions;
mod optimiser;
mod utilities;
mod linter;
mod casing;
mod variables;

use std::env;

fn main() {
    let files: Vec<String> = env::args().collect();
    let file_contents: String = utilities::read_from_file(&files[1]);

    // convert custom notation
    let mut file_processing_out = functions::replace_functions(file_contents.clone());

    // do some basic optimization
    file_processing_out = optimiser::optimise(file_processing_out.clone());

    // // check that variables are valid
    file_processing_out = variables::check_variables(file_processing_out.clone());

    casing::check_casing(file_processing_out.clone());

    println!("{}", file_processing_out);
    
    utilities::write_to_file(
        &(files[1]).replace(".pyc", ".py"),
        &file_processing_out
    )
}
