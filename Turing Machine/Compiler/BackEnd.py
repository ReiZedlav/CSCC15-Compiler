from Compiler import Token,ErrorHandler

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


def executeLabel(instructions,label,TuringMachine):
    code = instructions[label]

    if code == []:
        return

    for i in code:

        print("\n")

        while True:
            step = str(input("Stepping Thru >> "))
            print("Now executing: " + " ".join(i))
            break

        if len(i) == 1:
            if i[0].upper() == "HALT":
                return

            elif i[0].upper() == "LEFT":
                TuringMachine.left()
                TuringMachine.printTape()
                continue

            elif i[0].upper() == "RIGHT":
                TuringMachine.right()
                TuringMachine.printTape()
                continue

        elif len(i) == 2:
            if i[0].upper() == "WRITE":
                TuringMachine.write(i[1])
                TuringMachine.printTape()
                continue

            elif i[0].upper() == "GOTO":
                executeLabel(instructions,i[1],TuringMachine)
                return

        elif len(i) == 4:
            cmp = TuringMachine.read()
            if i[1] == cmp:
                executeLabel(instructions,i[3],TuringMachine)
                return
            else:
                continue
    

    executeLabel(instructions,deadEndAutoJump(instructions,label),TuringMachine)
        

    return 





    




            
        

        
        
        