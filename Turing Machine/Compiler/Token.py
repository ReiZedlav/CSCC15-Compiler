
def identify(rawToken):
    if rawToken[-1] == ":":
        return "LABEL"

    if rawToken.upper() in ["LEFT","RIGHT","IF","GOTO","HALT","WRITE"]:
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
        
    def getType(self):
        return self.type
    
    def getLine(self):
        return self.line

    def getName(self):
        return self.name
    
    @staticmethod
    def declassify(token):
        if len(token) == 1:
            return [token[0].getName()]

        elif len(token) == 2:
            return [token[0].getName(),token[1].getName()]

        elif len(token) == 4:
            return [token[0].getName(),token[1].getName(),token[2].getName(),token[3].getName()]

    
    
    
