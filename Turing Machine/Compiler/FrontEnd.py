from Compiler import ErrorHandler

class Lexer:
    @staticmethod
    def scan(externalFile):
        RawTokens = []        

        with open(externalFile, "r") as simplified:
            currentFile = simplified.readlines()

            for i in currentFile:
                if i.strip() == "":
                    pass
                else:
                    RawTokens.append(i.strip())
        return RawTokens

     



class Analyze:
    def __init__(self,externalFile=None):
        self.scanned = Lexer.scan(externalFile)  
        print(self.scanned)
    
    
    

    
        


