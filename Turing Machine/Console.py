import ControlUnit
import re

class Console:
    def __init__(self):
        self.TuringMachine = ControlUnit.Head()

    def execute(self,command):
        if command == "LEFT":
            self.TuringMachine.left()
        
        elif command == "RIGHT":
            self.TuringMachine.right()

        elif command == "HALT":
            self.TuringMachine.halt()
            exit()
        
        elif "WRITE" in command:
            size = len(command)

            if size == 7 and size < 8:
                self.TuringMachine.write(command[-1])


    def interact(self):
        while True:
            command = input("$ ")
            self.execute(command)

user = Console()

user.interact()
