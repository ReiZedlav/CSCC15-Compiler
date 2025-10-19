
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
    def __init__(self,rawToken):
        self.name = rawToken
        self.type = identify(rawToken)

    def getType(self):
        return self.type

    def getName(self):
        return self.name
    

