from Compiler import ErrorHandler

class Lexer:

    @staticmethod
    def verifyToken(packagedTokens,line):
        #verify write statements
        if len(packagedTokens) == 2:
            if packagedTokens[0] != "WRITE" or len(str(packagedTokens[1])) > 1:
                if (len(str(packagedTokens[1])) > 1):
                    ErrorHandler.Errors.unknownStatement("Invalid Symbol: ",packagedTokens,line)
                    return False
                ErrorHandler.Errors.unknownStatement("Invalid Keyword: ",packagedTokens,line)
                return False

        if len(packagedTokens) == 4:
            if packagedTokens[0] != "IF":
                ErrorHandler.Errors.unknownStatement("Mismatched IF: ",packagedTokens,line)
                return False
            
            elif packagedTokens[2] != "GOTO":
                ErrorHandler.Errors.unknownStatement("Mismatched GOTO: ",packagedTokens,line)
                return False
        
        if len(packagedTokens) > 4:
            ErrorHandler.Errors.unknownStatement("Syntax overbounds: ",packagedTokens,line)
            return False
    
             
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
                        return

                    RawTokens.append(i.strip().split())
        
        #PROCESS THEM TOKENS HERE WITH SOME IDENTIFIERS
        print(RawTokens)            

        return RawTokens
    
    
     




    
    
    

    
        


