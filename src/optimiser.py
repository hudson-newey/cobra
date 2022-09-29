import re

def runOptimiser(code):
    code = removeUnreachableCode(code)
    code = removeNonActionCode(code)
    code = replaceFuncAssignToConst(code)

    return code

def removeUnreachableCode(code):
    return code

def replaceFuncAssignToConst(code):
    funcitonAssignments = ["str()", "int()", "dict()", "tuple()", "list()"]
    constReplacments = ["\"\"", "0", "{}", "()", "[]"]

    for i in range(len(funcitonAssignments)):
        code = code.replace(funcitonAssignments[i], constReplacments[i])

    return code

def removeNonActionCode(code):
    findAndReplaceRE = r"[ ]*\t*#.+\n"
    replacement = ""

    code = re.sub(findAndReplaceRE, replacement, code)

    code = "".join([s for s in code.splitlines(True) if s.strip("\r\n")])

    return code