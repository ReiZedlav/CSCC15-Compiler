
class Errors:
    def __init__(self):
        pass
        
    @staticmethod
    def fileNotFound():
        print("Error 0: File not found!")

    @staticmethod
    def invalidCommand():
        print("Error 1: Command Invalid!")
    
    @staticmethod
    def duplicateLabel(label):
        print(f"Error 2: Duplicate label: {label}")
    
    @staticmethod
    def unknownStatement(message,code,line):
        print(f"{message} {" ".join(code)} at line {line}")

class StackTrace:
    pass    
        
        
    
