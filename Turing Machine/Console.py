import ControlUnit
from Compiler import FrontEnd,BackEnd,ErrorHandler,Token

class Console:
    def __init__(self):
        self.TuringMachine = ControlUnit.Head()

    #IDEA SINCE self.TuringMachine is an object, we can reference another a filehandler class to handle the file io

    #------------------------------------------------------------

    def compile(self,turingFile):
        
        #Divide each command into tokens and designate 
        #a grammar rule based on regular expressions.
        Table = FrontEnd.Lexer.Tokenizer(turingFile)

        #check if it is syntactically correct
        if FrontEnd.Syntax.Analyze(Table) == False:
            return
        
        #even if syntax is correct, check if it is meaningful 
        if FrontEnd.Semantic.Analyze(Table) == False:
            return

        #check CALLEES that are called from nonexisting labels
        if FrontEnd.Semantic.checkNonexistentLabels(Table) == False:
            return
        
        #check dupes
        if FrontEnd.Semantic.checkDuplicateLabels(Table) == False:
            return
        
        #semantic checks on labels
        if FrontEnd.Semantic.keywordAsLabelOrSymbolAsLabelCheck(Table) == False:
            return

        BackEnd.Describe.groupLabels(Table) 

        Segregated = BackEnd.Describe.segregate(Table)

        

        for i in Segregated["UNLABELED"]:
            print(len(i))
        


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

    def shell(self):
        while True:
            command = input("$ ")
            self.execute(command.strip())

#ADD TUI HERE SOON

user = Console()
user.shell()
