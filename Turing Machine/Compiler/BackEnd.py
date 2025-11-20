from Compiler import Token

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

        #print(segregated["UNLABELED"])                
        
        return segregated

def Execute(code,TuringMachine):
    for k,v in code.items():
        print(k,v)


        

            
        

        
        
        