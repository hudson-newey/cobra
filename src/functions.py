import re

def constructFunctions(code):
    return replaceCustomFunctions(code)

def replaceCustomFunctions(code):
    findAndReplaceRE = r"fn"
    pythonFunctionReplacement = "def"

    return re.sub(findAndReplaceRE, pythonFunctionReplacement, code)

def checkFunctions(code):
    return True