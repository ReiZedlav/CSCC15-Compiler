
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
    def improperUsage(command):
        print(f"Error 3: Improper usage of {command}")
    
    @staticmethod
    def labelUndefined(callee):
        print(f"Error 4: No label defined for callee: {callee}")

    @staticmethod
    def syntaxException(name):
        print(f"Syntax Error Found: {name}")

    @staticmethod
    def unknownStatement(message,code,line):
        print(f"{message} {" ".join(code)} at line {line}")


        
    
