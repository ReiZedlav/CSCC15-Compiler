from Compiler import Token

class Describe:
    @staticmethod
    def groupLabels(Table):
        
        newTable = []

        currentLabel = "UNLABELED:"

        for row in Table:
            if row[0].getType() == "LABEL":
                currentLabel = row[0].getName()
            else:
                row[0].setLabel(currentLabel)    
        return None

    @staticmethod
    def unpack(row):
        unpacked = []

        for i in row:
            unpacked.append(i.getName())
        return unpacked

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

def executeLabel(instructions,label,TuringMachine):
    code = instructions[label]

    for i in code:
        if len(i) == 1:
            if i[0].upper() == "HALT":
                return

            elif i[0].upper() == "LEFT":
                TuringMachine.left()
                TuringMachine.printTape()
            
            elif i[0].upper() == "RIGHT":
                TuringMachine.right()
                TuringMachine.printTape()
            
            
        
        elif len(i) == 2:
            if i[0].upper() == "WRITE":
                TuringMachine.write(i[1])
                TuringMachine.printTape()
            
            elif i[0].upper() == "GOTO":
                executeLabel(instructions,i[1],TuringMachine)
    
        elif len(i) == 4:
            cmp = TuringMachine.read()
            
            if i[1].upper() == cmp:
                executeLabel(instructions,i[3],TuringMachine)
                return
            else:
                continue


    
    


def Execute(code,TuringMachine):
    initial = code["UNLABELED"]

    for i in initial:
        if len(i) == 1:
            if i[0].upper() == "HALT":
                TuringMachine.printTape()
                return

            elif i[0].upper() == "LEFT":
                TuringMachine.left()
                TuringMachine.printTape()
            
            elif i[0].upper() == "RIGHT":
                TuringMachine.right()
                TuringMachine.printTape()
            
            
        
        elif len(i) == 2:
            if i[0].upper() == "WRITE":
                TuringMachine.write(i[1])
                TuringMachine.printTape()
            
            elif i[0].upper() == "GOTO":
                executeLabel(code,i[1],TuringMachine)
        
        elif len(i) == 4:
            cmp = TuringMachine.read()
            if i[1] == cmp:
                executeLabel(code,i[3],TuringMachine)
                return 
            else:
                continue
    
    if "start" in code:
        TuringMachine.default()
        executeLabel(code,"start",TuringMachine)
    elif "START" in code:
        TuringMachine.default()
        executeLabel(code,"START",TuringMachine)

    return


        

            
        

        
        
        