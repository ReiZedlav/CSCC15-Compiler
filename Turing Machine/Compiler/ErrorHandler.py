
class Errors:
    def __init__(self):
        pass
        
    @staticmethod
    def fileNotFound():
        print("Error 0: File not found!")

    @staticmethod
    def invalidCommand():
        print("Error 1. Command Invalid!")
    
    @staticmethod
    def instructionOverbounds(msg,line):
        print(f"Error 2. Instruction Overbounds. {msg} at line {line}")
    
    @staticmethod
    def invalidArgument(msg,line,error):
        print(f"Error 3. Invalid Argument Supplied. {msg} at line {line}. {error}")

    @staticmethod
    def semanticError(msg,line):
        print(f"Error 4. Semantic Error. Improper usage of {msg} at line {line}")

    @staticmethod
    def labelUndefined(callee,line):
        print(f"Error 5. No label defined for callee: {callee} at line {line}")
    
    @staticmethod
    def duplicatedLabel(callee):
        print(f"Error 6. {callee} is duplicated")
    
    @staticmethod
    def startNotFound():
        print("Error 7. No START: or start: label detected")
    
    @staticmethod
    def invalidLabel(label):
        if len(label) == 1:
            print(f"Error 8. Invalid Label {label}. SYMBOL cannot be a LABEL")
        else:
            print(f"Error 8. Invalid Label {label}. KEYWORD cannot be a LABEL")

        
    
