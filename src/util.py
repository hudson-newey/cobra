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

def displayTip(location = "", problem = "", description = "", fix = ""):
    print()
    print("--------------------")
    print(f"Warning from {location}")
    print(f"Currently Using {problem}")
    print(f"This can be incorrect because {description}")
    print(f"Suggestion: {fix}")
    print()
    return

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

def createDirectory(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    else:
        deleteDirectory(dirName)
        os.makedirs(dirName)
    
    return True

def deleteDirectory(dirName):
    try:
        os.rmdir(dirName)
    except OSError as e:
        print("Error: %s : %s" % (path_dir, e.strerror))
        return False
    
    return True

def deleteFile(fileName):
    try:
        os.remove(fileName)
    except:
        return False
    
    return True

def removeListDuplicates(myList):
    final_list = []
    for num in myList:
        if num not in final_list:
            final_list.append(num)
    return final_list