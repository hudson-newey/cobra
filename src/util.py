def throwError(code = 1, message = "Unknown Error..."):
    print(f"\nError {code}: {message}")
    exit(1)

def readFile(filepath):
    with open(filepath, "r") as file:
        return file.read()

def writeFile(filepath, contents):
    with open(filepath, "w") as file:
        file.write(contents)
    
    return True