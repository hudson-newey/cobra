import re

def checkVariableAssignments(code):
    constantFindRE = r"const ([a-zA-Z0-9]+)[: ]"

    constantVariables = re.findall(constantFindRE, code)

    # check that the constant variables are not reassigned
    
    for variable in constantVariables:
        constCheckRE = rf"{variable}[ ]*="
        if (len(re.findall(constCheckRE, code)) > 0): return (code, False)

    code = removeCobraArtifacts(code)

    return (code, True)

def removeCobraArtifacts(code):
    constantFindRERaw = r"(const [a-zA-Z0-9]+)[: ]"
    constantFindRE = r"const ([a-zA-Z0-9]+)[: ]"

    constantVariablesRaw = re.findall(constantFindRERaw, code)
    constantFind = re.findall(constantFindRE, code)

    for i in range(len(constantVariablesRaw)):
        code = code.replace(constantVariablesRaw[i], constantFind[i])
    
    return code