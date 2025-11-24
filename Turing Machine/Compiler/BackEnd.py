from Compiler import Token,ErrorHandler
import time

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

def debugLabel(instructions,label,TuringMachine):
    code = instructions[label]

    for i in code:
        
        while True: 

            command = str(input("TM Debugger >> "))

            if command == "":
                break
            
            elif command.upper() == "HALT":
                return

            elif command.upper() == "LEFT":
                TuringMachine.left()
                TuringMachine.printTape()
                continue

            elif command.upper() == "RIGHT":
                TuringMachine.right()
                TuringMachine.printTape() 
                continue

            elif "WRITE" in command.upper():
                size = len(command)

                if size >= 8:
                    ErrorHandler.Errors.invalidCommand()
                    continue

                if size == 7 and size < 8:
                    TuringMachine.write(command[-1])
                    TuringMachine.printTape()
                    continue       

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
                print(f"Jumping to: {" ".join(i)}")
                debugLabel(instructions,i[1],TuringMachine)
    
        elif len(i) == 4:
            cmp = TuringMachine.read()
    
            if i[1] == cmp:
                print(f"Jumping to: {" ".join(i)}")
                debugLabel(instructions,i[3],TuringMachine)
                return
            else:
                print(f"Condition Skipped: {" ".join(i)}")
                continue


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
            
            elif i[0].upper() == "RIGHT":
                time.sleep(0.1)
                TuringMachine.right()
                TuringMachine.printTape()
            
            
        
        elif len(i) == 2:
            if i[0].upper() == "WRITE":
                time.sleep(0.1)
                TuringMachine.write(i[1])
                TuringMachine.printTape()
            
            elif i[0].upper() == "GOTO":
                time.sleep(0.1)
                executeLabel(instructions,i[1],TuringMachine)
    
        elif len(i) == 4:
            cmp = TuringMachine.read()
            time.sleep(0.1)
            if i[1] == cmp:
                executeLabel(instructions,i[3],TuringMachine)
                return
            else:
                continue


    
    


def ExecuteInitials(code,TuringMachine,debug):
    initial = code["UNLABELED"]

    for i in initial:
        if len(i) == 1:
            if i[0].upper() == "HALT":
                TuringMachine.printTape()
                return

            elif i[0].upper() == "LEFT":
                time.sleep(0.1)
                TuringMachine.left()
                TuringMachine.printTape()
            
            elif i[0].upper() == "RIGHT":
                time.sleep(0.1)
                TuringMachine.right()
                TuringMachine.printTape()
            
            
        
        elif len(i) == 2:
            if i[0].upper() == "WRITE":
                time.sleep(0.1)
                TuringMachine.write(i[1])
                TuringMachine.printTape()
            
            elif i[0].upper() == "GOTO":
                executeLabel(code,i[1],TuringMachine)
        
        elif len(i) == 4:
            time.sleep(0.1)
            cmp = TuringMachine.read()
            if i[1] == cmp:
                executeLabel(code,i[3],TuringMachine)
                return 
            else:
                continue
    
    if "start" in code:
        TuringMachine.default()
        TuringMachine.printTape()

        if debug == True:
            debugLabel(code,"start",TuringMachine)
        else:
            executeLabel(code,"start",TuringMachine)

    elif "START" in code:
        TuringMachine.default()
        TuringMachine.printTape()
        
        if debug == True:
            debugLabel(code,"START",TuringMachine)
        else:
            executeLabel(code,"START",TuringMachine)

    return


        

            
        

        
        
        