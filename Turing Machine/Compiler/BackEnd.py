
class Describe:
    @staticmethod
    def groupLabels(Table):
        
        newTable = []

        currentLabel = "UNLABELED"

        for row in Table:
            if row[0].getType() == "LABEL":
                currentLabel = row[0].getName()
            else:
                row[0].setLabel(currentLabel)    
        return None

    @staticmethod
    def segregate(Table):

        segregated = {}

        for row in Table:
            if row[0].getLabel() != None:
                if row[0].getLabel() not in segregated:
                    segregated[row[0].getLabel()] = [row]
                else:
                    segregated[row[0].getLabel()].append(row)    
        return segregated