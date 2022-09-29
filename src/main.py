import sys

# local imports
from functions import checkFunctions, constructFunctions
from optimiser import runOptimiser
from variables import cobraVariables
from imports import checkImports
from util import *

if __name__ == "__main__":
    targetFile = sys.argv[1]

    targetCode = readFile(targetFile)

    targetCode = runOptimiser(targetCode)

    # check that code is valid
    if not checkFunctions(targetCode): throwError(code = 2, message = "Error in Functions...")

    variableAssignment = cobraVariables(targetCode)
    if not variableAssignment[0]: throwError(code = 3, message = "Error in Variable Assignment...")
    targetCode = variableAssignment[1]

    if not checkImports(targetCode): throwError(code = 4, message = "Unused Imports...")

    # replace code
    targetCode = constructFunctions(targetCode)

    print("Code Compiled!")
    print(targetCode)

    writeFile(targetFile.replace(".pyc", ".py"), targetCode)