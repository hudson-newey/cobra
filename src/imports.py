import re

def checkImports(code):
    findImportsRE = r"import ([a-zA-Z0-9]+)"
    imports = re.findall(findImportsRE, code)

    allImports = list()
    for importSingular in imports:
        importMe = importSingular.split(",")
        for importSing in importMe:
            allImports.append(importSing)
    
    for i in range(len(allImports)):
        allImports[i] = allImports[i].replace(" ", "")

    for importSingular in allImports:
        validateImportRE = rf"{importSingular}\(.*\)"

        if not (len(re.findall(validateImportRE, code)) > 0):
            return False

    return True