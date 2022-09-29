import sys

# local imports
from functions import checkFunctions, constructFunctions
from optimiser import runOptimiser
from variables import checkVariableAssignments
from util import *

if __name__ == "__main__":
    targetFile = sys.argv[1]

    targetCode = readFile(targetFile)

    targetCode = runOptimiser(targetCode)

    # check that code is valid
    if not checkFunctions(targetCode): throwError(message = "Error in Functions")

    variableAssignment = checkVariableAssignments(targetCode)
    if not variableAssignment[1]: throwError(message = "Error in Variable Assignment")
    targetCode = variableAssignment[0]

    # replace code
    targetCode = constructFunctions(targetCode)

    print("Code Compiled!")
    print(targetCode)

    writeFile(targetFile.replace(".pyc", ".py"), targetCode)