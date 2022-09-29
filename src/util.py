import os

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

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles