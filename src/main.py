import sys

# local imports
from functions import checkFunctions, constructFunctions
from optimiser import runOptimiser
from variables import cobraVariables
from imports import checkImports
from util import *

def isTargetFile(target):
    if ".pyc" in target: return True
    if "." in target: throwError(message = "Target File Not Found. Ensure that your have the .pyc extension")
    return False

if __name__ == "__main__":
    target = sys.argv[1]

    if isTargetFile(target):
        targetFiles = [target]
    else:
        targetFiles = getListOfFiles(target)
    
    for targetFile in targetFiles:

        targetCode = readFile(targetFile)

        targetCode = runOptimiser(targetCode)

        # check that code is valid
        if not checkFunctions(targetCode): throwError(code = 2, message = f"{targetFile} Functions Mismatched...")

        variableAssignment = cobraVariables(targetCode)
        if not variableAssignment[0]: throwError(code = 3, message = f"{targetFile} in Variable Assignment...")
        targetCode = variableAssignment[1]

        if not checkImports(targetCode): throwError(code = 4, message = f"{targetFile} Unused Imports...")

        # replace code
        targetCode = constructFunctions(targetCode)

        print("Code Compiled!")
        print(targetCode)

        writeFile(targetFile.replace(".pyc", ".py"), targetCode)