class Cell:
    def __init__(self,Symbol,Previous=None,Next=None):
        self.Symbol = Symbol
        self.Previous = Previous
        self.Next = Next

class Head:
    def __init__(self):
        self.pointer = Cell("_")

    def printTape(self):
        current = self.pointer

        tape = []

        while current.Previous != None:
            current = current.Previous
        
        while current.Next != None:
            tape.append(current.Symbol)
            current = current.Next
        tape.append(current.Symbol)
        
        print(tape)
    
    def read(self):
        print(self.pointer.Symbol)
        return self.pointer.Symbol

    def write(self,symbol):
        self.pointer.Symbol = symbol

    def left(self):
        if self.pointer.Previous == None:
            newCell = Cell("_")
            self.pointer.Previous = newCell
            newCell.Next = self.pointer
            newCell.Previous = None

            self.pointer = newCell
        else: 
            self.pointer = self.pointer.Previous  

    def right(self):
        if self.pointer.Next == None:
            newCell = Cell("_")

            self.pointer.Next = newCell
            newCell.Previous = self.pointer
            newCell.Next = None

            self.pointer = newCell
        else: 
            self.pointer = self.pointer.Next  



