from Compiler import ErrorHandler,Token

class Lexer:

    @staticmethod
    def scan(externalFile):

        result = []

        with open(externalFile,"r") as simplified:
            currentFile = simplified.readlines()
            for line in currentFile:
                result.append(line.split())
        return result

    @staticmethod
    def tokenize(lines):
        
        rawTokens = []
        line = 0

        for code in lines:
            packager = []

            line += 1

            for i in code:
                token = Token.Classify(i,line)
                packager.append(token)
            rawTokens.append(packager)

        partialTokens = []

        for j in rawTokens:
            if len(j) != 0:
                partialTokens.append(j)

        return partialTokens
    
    @staticmethod 
    def Tokenizer(externalFile):
        Divided = Lexer.scan(externalFile)
        
        RawTokens = Lexer.tokenize(Divided)

        return RawTokens

class Syntax:
    
    @staticmethod
    def Analyze(Tokens):
        
        for line in Tokens:
            if len(line) > 4:
                msg = []

                for i in line:
                    msg.append(i.getName())

                ErrorHandler.Errors.instructionOverbounds(" ".join(msg),line[0].getLine())

                return False
            
            elif len(line) == 4:
                if line[3].getType() != "CALLEE":
                    ErrorHandler.Errors.invalidArgument(line[3].getName(),line[3].getLine(),"This must be a CALLEE")
                    return False

                #possible redundancy
                if line[2].getType() != "KEYWORD":
                    ErrorHandler.Errors.invalidArgument(line[2].getName(),line[2].getLine(),"This must be a KEYWORD")
                    return False

                if line[1].getType() != "SYMBOL":
                    ErrorHandler.Errors.invalidArgument(line[1].getName(),line[1].getLine(),"This must be a SYMBOL")
                
                #possible redundancy
                if line[0].getType() != "KEYWORD":
                    ErrorHandler.Errors.invalidArgument(line[0].getName(),line[0].getLine(),"This must be a KEYWORD")
                    return False
            
            elif len(line) == 2:
                if line[0].getType() != "KEYWORD":
                    ErrorHandler.Errors.invalidArgument(line[0].getName(),line[0].getLine(),"This must be a KEYWORD")
                    return False
                
                if line[1].getType() not in ["SYMBOL", "CALLEE"]:
                    ErrorHandler.Errors.invalidArgument(line[1].getName(),line[1].getLine(),"This must be a SYMBOL or a CALLEE")
                    return False
            
            elif len(line) == 1:
                if line[0].getType() not in ["LABEL","KEYWORD"]:
                    ErrorHandler.Errors.invalidArgument(line[0].getName(),line[0].getLine(),"This must be a LABEL or a KEYWORD")
                    return False

class Semantic:
    
    @staticmethod
    def Analyze(Tokens):
        for line in Tokens:
            if len(line) == 4:
                if line[0].getName() != "IF":
                    ErrorHandler.Errors.semanticError(line[0].getName(),line[0].getLine())
                    return False
                
                if line[2].getName() != "GOTO":
                    ErrorHandler.Errors.semanticError(line[2].getName(),line[2].getLine())
                    return False

            elif len(line) == 2:


                if line[1].getType() == "SYMBOL":
                    if line[0].getName() != "WRITE":
                        ErrorHandler.Errors.semanticError(line[0].getName() + " " + line[1].getName(),line[0].getLine())
                        return False
                
                elif line[1].getType() == "CALLEE":
                    if line[0].getName() != "GOTO":
                        ErrorHandler.Errors.semanticError(line[0].getName() + " " + line[1].getName(),line[0].getLine())
                        return False



            elif len(line) == 1:
                if line[0].getName() in ["GOTO","IF","WRITE"]:
                    ErrorHandler.Errors.semanticError(line[0].getName(),line[0].getLine())
                    return False
        return True
                    
    @staticmethod
    def checkNonexistentLabels(Tokens):
        labels = []

        callees = []

        for token in Tokens:
            for i in token:
                if i.getType() == "LABEL":
                    labels.append(i.getName())
                elif i.getType() == "CALLEE":
                    callees.append(i.getName())
        
        for caller in callees:
            labeledCaller = caller + ":"
            if labeledCaller not in labels:
                ErrorHandler.Errors.labelUndefined(caller)
                return False
        

        return True
    
    @staticmethod
    def checkDuplicateLabels(Tokens):
        checker = {}

        for i in Tokens:
            identifier = i[0].getName()

            if identifier[-1] == ":":
                if i[0].getName() not in checker:
                    checker[i[0].getName()] = 1
                else:
                    checker[i[0].getName()] += 1
        
        for k,v in checker.items():
            if v >= 2:
                ErrorHandler.Errors.duplicatedLabel(k)
                return False
        return True

    @staticmethod 
    def finalLabelCheck(Tokens):
        check = []

        for i in Tokens:
            if i[0].getType() == "LABEL":
                verify = i[0].getName()[:-1] 
                
                if len(verify) == 1:
                    ErrorHandler.Errors.invalidLabel(verify)
                    return False

                if verify in ["LEFT","RIGHT","IF","GOTO","HALT","WRITE"]:
                    ErrorHandler.Errors.invalidLabel(verify)
                    return False

        for j in Tokens:
            check.append(j[0].getName())
        
        if "START:" not in check and "start" not in check:
            ErrorHandler.Errors.startNotFound()
            return False
        
        return True
                
    

    
        


