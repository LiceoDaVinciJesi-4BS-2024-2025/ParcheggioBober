#Vehicle

colourList = ["blu", "giallo", "nero"]
brandList = ["audi", "nissan", "panda"]
listaalim = ["diesel", "elettrico"]
listalett = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]
listanum = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
import random

class Veicolo:
    def __init__(self, brand, model, colour, enginesize:int, fuelType, plates):
        if brand not in brandList:
            raise ValueError("IMPOSSIBLE")
        else:
            self.brand = brand
        if colour not in colourList:
              raise ValueError("IMPOSSIBLE")
        else:  
            self.colour = colour
        if enginesize < 0 and enginesize % 100 != 0:
            raise ValueError("value not supported")
        else:
            self.enginesize = enginesize
        if fuelType not in listaalim:
            raise ValueError("IMPOSSIBLE")
        else:
            self.fuelType = fuelType
        for x in plates:
            if x[0] in listalett and x[1] in listalett and x[2] in listanum and x[3] in listanum and x[4] in listanum and x[5] in listalett and x[6] in listalett:
                self.plates = plates
            else:
                raise ValueError("plates not available")
           
    def __lt__(self, other):
        if self.brand == other.brand:
            if self.model == other.model:
                return self.enginesize < other.enginesize
            else:
                return listalett.index(self.model.upper()[0]) < listalett.index(other.model.upper()[0])
        else:
            return listalett.index(self.brand.upper()[0]) < listalett.index(other.brand.upper()[0])
