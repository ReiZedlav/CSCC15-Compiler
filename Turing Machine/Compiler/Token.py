
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
        #integrate labelName here

    def getType(self):
        return self.type
    
    def getLine(self):
        return self.line

    def getName(self):
        return self.name
    

