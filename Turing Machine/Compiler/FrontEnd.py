from Compiler import ErrorHandler,Token

class Lexer:

    @staticmethod
    def verifyToken(packagedTokens,line):
        if len(packagedTokens) == 1:
            if packagedTokens[0] == "WRITE":
                ErrorHandler.Errors.unknownStatement("Missing Write Symbol: ",packagedTokens,line)
                return False

        #verify write statements - MISSING GOTO STATEMENT
        if len(packagedTokens) == 2:
            if packagedTokens[0] != "WRITE" or packagedTokens[0] != "GOTO":
                if packagedTokens[0] == "WRITE":
                    if len(str(packagedTokens[1])) > 1:
                        ErrorHandler.Errors.unknownStatement("Write overbounds: ",packagedTokens,line)
                        return False
                

        if len(packagedTokens) == 4:
            if packagedTokens[0] != "IF":
                ErrorHandler.Errors.unknownStatement("Mismatched IF: ",packagedTokens,line)
                return False
            
            if len(str(packagedTokens[1])) > 1:
                ErrorHandler.Errors.unknownStatement("Symbol overbounds: ",packagedTokens,line)
                return False
            
            elif packagedTokens[2] != "GOTO":
                ErrorHandler.Errors.unknownStatement("Mismatched GOTO: ",packagedTokens,line)
                return False
        
        if len(packagedTokens) > 4:
            ErrorHandler.Errors.unknownStatement("Syntax overbounds: ",packagedTokens,line)
            return False

    @staticmethod
    def duplicateChecker(rawTokens):
        checker = {}

        for i in rawTokens:
            identifier = i[0]

            if identifier[-1] == ":":
                if i[0] not in checker:
                    checker[i[0]] = 1
                else:
                    checker[i[0]] += 1
        
        for k,v in checker.items():
            if v >= 2:
                ErrorHandler.Errors.duplicateLabel(k)
                return False
        return True


    @staticmethod
    def Tokenizer(externalFile):
        RawTokens = []        
        line = 0

        with open(externalFile, "r") as simplified:
            currentFile = simplified.readlines()

            for i in currentFile:
                if i.strip() == "":
                    line += 1

                else:
                    line += 1
                    verify = Lexer.verifyToken(i.split(),line) 
                    
                    if verify == False:
                        return False

                    RawTokens.append(i.strip().split())
        
        LabelCheck = Lexer.duplicateChecker(RawTokens)

        if LabelCheck == False:
            return False
        
        ProcessedTokens = []

        for unprocessed in RawTokens:
            packager = []

            for rawToken in unprocessed:
                token = Token.Classify(rawToken)
                
                #print(token.getType())

                packager.append(token)

            ProcessedTokens.append(packager)

        #invoke compressed tokens with .getName() and .getType()
        
        return ProcessedTokens

class Syntax:
    
    @staticmethod
    def Analyze(Tokens):
        
        for packaged in Tokens:
            if len(packaged) == 1:
                if packaged[0].getType() not in ["LABEL","KEYWORD"]:
                    ErrorHandler.Errors.syntaxException("".join(packaged[0].getName()))
                    return False

            if len(packaged) == 2:
                if packaged[0].getType() != "KEYWORD":
                    ErrorHandler.Errors.syntaxException("".join(packaged[0].getName()))
                    return False
                
                if packaged[1].getType() not in ["SYMBOL","CALLEE"]:
                    ErrorHandler.Errors.syntaxException("".join(packaged[1].getName()))
                    return False
                
            if len(packaged) == 4:
                if packaged[3].getType() != "CALLEE":
                    ErrorHandler.Errors.syntaxException(packaged[0].getName() + " " + packaged[1].getName() + " " + packaged[2].getName() + " " + packaged[3].getName())
                    return False
        return True

class Semantic:

    @staticmethod
    def Analyze(Tokens):
        for packaged in Tokens:
            if len(packaged) == 1:
                if packaged[0].getName() in ["GOTO","IF","WRITE"]:
                    ErrorHandler.Errors.improperUsage(packaged[0].getName())
                    return False

            if len(packaged) == 2:
                if packaged[1].getType() == "SYMBOL":
                   if (packaged[0].getName() != "WRITE"):
                        ErrorHandler.Errors.improperUsage(packaged[0].getName())
                        return False
                
                elif packaged[1].getType() == "CALLEE":
                    if (packaged[0].getName() != "GOTO"):
                        ErrorHandler.Errors.improperUsage(packaged[0].getName())
                        return False
        return True

                
    
     




    
    
    

    
        


