import ControlUnit
import tui
from Compiler import FrontEnd,BackEnd,ErrorHandler,Token


class Console:
    def __init__(self):
        self.TuringMachine = ControlUnit.Head()
        

    #------------------------------------------------------------

    def compile(self,turingFile,debug):

        
        
        #Divide each command into tokens and designate 
        #a grammar rule based on regular expressions.

        try:
            Table = FrontEnd.Lexer.Tokenizer(turingFile)
        except FileNotFoundError:
            ErrorHandler.Errors.fileNotFound()
            return

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

        if debug == True:
            BackEnd.ExecuteInitials(Segregated,self.TuringMachine,debug)
        else:
            BackEnd.ExecuteInitials(Segregated,self.TuringMachine,debug)

    #------------------------------------------------------------

    def execute(self,command):
        if "TMX" in command or "tmx" in command:
            argument = command.split()
            if len(argument) == 1 or len(argument) > 2:
                ErrorHandler.Errors.invalidCommand()
            else:
                self.compile(argument[1],debug=False)
            return
        
        elif "DEBUG" in command or "debug" in command:
            argument = command.split()
            if len(argument) == 1 or len(argument) > 2:
                ErrorHandler.Errors.invalidCommand()
            else:
                self.compile(argument[1],debug=True)
            return


        elif command.upper() == "CLEAR":
            self.TuringMachine.clearTape()
            self.TuringMachine.printTape()
            return

        elif command.upper() == "LEFT":
            self.TuringMachine.left()
            self.TuringMachine.printTape()
            return
        
        elif command.upper() == "SHOW":
            self.TuringMachine.printTape()
            return

        elif command.upper() == "RIGHT":
            self.TuringMachine.right()
            self.TuringMachine.printTape()
            return

        elif command.upper() == "HALT":
            self.TuringMachine.printTape()
            exit()
            
        elif "WRITE" in command.upper():
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

tui.Design.header()

user = Console()
user.shell()
