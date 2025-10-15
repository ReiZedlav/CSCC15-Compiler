class Symbol:
    def __init__(self,Data,Previous=None,Next=None):
        self.Data = Data
        self.Previous = Previous
        self.Next = Next

class Tape:
    def __init__(self):
        self.head = Symbol(None)
    
    def read(self):
        print(self.head.Data)

    def write(self,bit):
        self.head.Data = bit

    def left(self):
        if self.head.Previous == None:
            newSymbol = Symbol(None)
            self.head.Previous = newSymbol
            newSymbol.Next = self.head
            newSymbol.Previous = None

            self.head = newSymbol
        else: 
            self.head = self.head.Previous  

    def right(self):
        if self.head.Next == None:
            newSymbol = Symbol(None)

            self.head.Next = newSymbol
            newSymbol.Previous = self.head
            newSymbol.Next = None

            self.head = newSymbol
        else: 
            self.head = self.head.Next  

Machine = Tape()

