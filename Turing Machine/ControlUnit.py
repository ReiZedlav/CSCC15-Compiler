
class Cell:
    def __init__(self,Symbol,Previous=None,Next=None):
        self.Symbol = Symbol
        self.Previous = Previous
        self.Next = Next

class Head:
    def __init__(self):
        self.pointer = Cell("_")
        self.position = 0

    def visualizePosition(self,tape):
        for cell in tape:
            if cell == self.pointer:
                print(f"[{cell.Symbol}]" + " ",end="")
            else: 
                print(cell.Symbol + " ",end="")

    def printTape(self):
        current = self.pointer

        tape = []

        while current.Previous != None:
            current = current.Previous
        
        while current.Next != None:
            #tape.append(current.Symbol)
            tape.append(current)
            current = current.Next

        tape.append(current)
        #tape.append(current.Symbol)
        
        self.visualizePosition(tape)
        #print(" ".join(tape))
        print()
    
    def read(self):
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

    def default(self):

        current = self.pointer

        while current.Previous != None:
            current = current.Previous

        self.pointer = current

        self.position = 0
        
        return
    


