from Compiler import Token,ErrorHandler
import time

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"

class Describe:
    
    @staticmethod
    def segregate(Table):

        segregated = {}

        currentLabel = "UNLABELED"

        container = []

        for row in Table:
            if row[0].getType() != "LABEL":

                container.append(Token.Classify.declassify(row))
                
            elif row[0].getType() == "LABEL":

                segregated[currentLabel] = container

                currentLabel = row[0].getName()[:-1]

                container = []

        segregated[currentLabel] = container
        
        return segregated


def deadEndAutoJump(instructions,currentLabel):
    
    labels = list(instructions.keys()) + [None]

    for i in range(0,len(labels),1):
        if labels[i] == currentLabel:
            return labels[i + 1]


def visualizeLabel(code,index,labelname):
    print(labelname + ":")
    for count in range(0,len(code)):
        if count == index:
            print(BOLD + RED + "    ["+ " ".join(code[count]) + "]" + RESET)
        else:
            print("    " + " ".join(code[count]))
        
    print()

def executeLabel(instructions,label,TuringMachine):
    if label == None:
        return

    code = instructions[label]

    for index in range(0,len(code)):

        
        print("\n")

        while True:
            step = str(input(""))
            visualizeLabel(code,index,label)
            break

        if len(code[index]) == 1:
            if code[index][0].upper() == "HALT":
                TuringMachine.printTape()
                return

            elif code[index][0].upper() == "LEFT":
                TuringMachine.left()
                TuringMachine.printTape()
                continue

            elif code[index][0].upper() == "RIGHT":
                TuringMachine.right()
                TuringMachine.printTape()
                continue

        elif len(code[index]) == 2:
            if code[index][0].upper() == "WRITE":
                TuringMachine.write(code[index][1])
                TuringMachine.printTape()
                continue

            elif code[index][0].upper() == "GOTO":
                executeLabel(instructions,code[index][1],TuringMachine)
                return

        elif len(code[index]) == 4:
            cmp = TuringMachine.read()
            if code[index][1] == cmp:
                executeLabel(instructions,code[index][3],TuringMachine)
                return
            else:
                continue
    

    executeLabel(instructions,deadEndAutoJump(instructions,label),TuringMachine)
        

    return 





    




            
        

        
        
        