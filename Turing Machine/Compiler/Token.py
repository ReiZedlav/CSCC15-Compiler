
def identify(rawToken):
    if rawToken[-1] == ":":
        return "LABEL"

    if rawToken in ["LEFT","RIGHT","IF","GOTO","HALT","WRITE"]:
        return "KEYWORD"
    
    if len(str(rawToken)) == 1:
        return "SYMBOL"
    
    else:
        return "CALLEE"

class Classify:
    def __init__(self,rawToken,line):
        self.name = rawToken
        self.line = line
        self.type = identify(rawToken)
        self.fromLabel = None

    def getType(self):
        return self.type
    
    def getLine(self):
        return self.line

    def getName(self):
        return self.name
    
    def getLabel(self):
        return self.fromLabel

    def setLabel(self,labelName):
        self.fromLabel = labelName
    
    
