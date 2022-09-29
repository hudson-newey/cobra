# cobra
An abstraction of Python which supports stronger typing, error checking, defensive coding principles, and much needed features  
  
---
**Current Features:**  
* Constant Variables (via `const` keyword)
    * Displays an error if you try to reassign a value to a constant
* Short code function declaration (via the `fn` keyword)
* Optimised output code
    * Removes empty lines
    * Removes comments
    * Modifies functional assignments to be constants (where possible)

### And it's all backwards compatible with Python & Python3! Just rename your filetype to `.pyc`!