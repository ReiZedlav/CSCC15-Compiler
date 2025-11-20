class Cell:
    def __init__(self,Symbol,Previous=None,Next=None):
        self.Symbol = Symbol
        self.Previous = Previous
        self.Next = Next

class Head:
    def __init__(self):
        self.pointer = Cell("_")
        self.position = 0

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
            if self.position != 0:

                newCell = Cell("_")
                self.pointer.Previous = newCell
                newCell.Next = self.pointer
                newCell.Previous = None

                self.pointer = newCell
            #to do list here

        else: 
            self.pointer = self.pointer.Previous

            self.position -= 1  

    def right(self):
        if self.pointer.Next == None:
            newCell = Cell("_")

            self.pointer.Next = newCell
            newCell.Previous = self.pointer
            newCell.Next = None

            self.pointer = newCell

            self.position += 1
        else: 
            self.pointer = self.pointer.Next

            self.position += 1  

