from Compiler import Token,ErrorHandler
import time

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
    
    labels = list(instructions.keys())

    for i in range(0,len(labels),1):
        if labels[i] == currentLabel:
            return labels[i + 1]


def executeLabel(instructions,label,TuringMachine):
    code = instructions[label]

    for i in code:
        if len(i) == 1:
            if i[0].upper() == "HALT":
                return

            elif i[0].upper() == "LEFT":
                time.sleep(0.1)
                TuringMachine.left()
                TuringMachine.printTape()
                continue

            elif i[0].upper() == "RIGHT":
                time.sleep(0.1)
                TuringMachine.right()
                TuringMachine.printTape()
                continue

        elif len(i) == 2:
            if i[0].upper() == "WRITE":
                time.sleep(0.1)
                TuringMachine.write(i[1])
                TuringMachine.printTape()
                continue

            elif i[0].upper() == "GOTO":
                time.sleep(0.1)
                executeLabel(instructions,i[1],TuringMachine)
                return

        elif len(i) == 4:
            cmp = TuringMachine.read()
            time.sleep(0.1)
            if i[1] == cmp:
                executeLabel(instructions,i[3],TuringMachine)
                return
            else:
                continue
    

    executeLabel(instructions,deadEndAutoJump(instructions,label),TuringMachine)
        

    return 

def ExecuteInitials(code,TuringMachine):

    TuringMachine.default()

    executeLabel(code,"UNLABELED",TuringMachine)

    return



    




            
        

        
        
        