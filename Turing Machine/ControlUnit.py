
class Cell:
    def __init__(self,Symbol,Previous=None,Next=None):
        self.Symbol = Symbol
        self.Previous = Previous
        self.Next = Next

class Head:
    def __init__(self):
        self.pointer = Cell("_")

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
            tape.append(current)
            current = current.Next

        tape.append(current)
        
        self.visualizePosition(tape)
        
        print()
    
    def read(self):
        return self.pointer.Symbol

    def write(self,symbol):
        self.pointer.Symbol = symbol

    def left(self):
        if self.pointer.Previous == None:
            return
        else: 
            self.pointer = self.pointer.Previous

            if self.pointer.Next.Next == None:
                if self.pointer.Next.Symbol == "_":
                    self.pointer.Next = None
        

    def right(self):
        if self.pointer.Next == None:
            newCell = Cell("_")

            self.pointer.Next = newCell
            newCell.Previous = self.pointer
            newCell.Next = None

            self.pointer = newCell

        else: 
            self.pointer = self.pointer.Next
    
    def clearTape(self):
        self.pointer.Previous = None
        self.pointer.Next = None

        self.pointer = Cell("_")




    def default(self):

        current = self.pointer
        
        while current.Previous != None:    
            current = current.Previous
            
        self.pointer = current

        return
    


