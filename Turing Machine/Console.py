import ControlUnit
from Compiler import FrontEnd,ErrorHandler,Token


class Console:
    def __init__(self):
        self.TuringMachine = ControlUnit.Head()

    #TOD0 FILE HANDLER FOR .tm FILES

    #IDEA SINCE self.TuringMachine is an object, we can reference another a filehandler class to handle the file io

    #------------------------------------------------------------

    def compile(self,turingFile):
        
        #still not done
        Tokens = FrontEnd.Lexer.Tokenizer(turingFile)

        #To debug Tokenization issues later.
        #for i in Tokens:
            #for j in i:
                #print(j.getName(),"-",j.getType())

        
        


    #------------------------------------------------------------

    def execute(self,command):
        #------------------------------------------
        if "TMC" in command:
            argument = command.split()
            if len(argument) == 1 or len(argument) > 2:
                ErrorHandler.Errors.invalidCommand()
            else:
                self.compile(argument[1])
            return
        #-----------------------------------------

        elif command == "LEFT":
            self.TuringMachine.left()
            self.TuringMachine.printTape()
            return

        elif command == "RIGHT":
            self.TuringMachine.right()
            self.TuringMachine.printTape()
            return

        elif command == "HALT":
            self.TuringMachine.printTape()
            exit()
            
        elif "WRITE" in command:
            size = len(command)

            if size >= 8:
                ErrorHandler.Errors.invalidCommand()
                return

            if size == 7 and size < 8:
                self.TuringMachine.write(command[-1])
                self.TuringMachine.printTape()
                return

        ErrorHandler.Errors.invalidCommand()

        return

    def interact(self):
        while True:
            command = input("$ ")
            self.execute(command)

#ADD TUI HERE SOON

user = Console()
user.interact()
