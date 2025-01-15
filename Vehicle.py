#Vehicle

colourList = ["Blue", "Yellow", "Black"]
brandList = ["Audi", "Nissan", "Panda", "Toyota"]
fuelList = ["Diesel", "Electric"]
letterList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]
numList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
import random

class Vehicle:
    #Init
    def __init__(
        self,
        plates: str,
        brand: str = "Toyota",
        model: str = "Yaris",
        colour: str = "Yellow",
        enginesize:int = 100,
        fuelType: str = "Diesel"):

        
        if brand not in brandList:
            raise ValueError("IMPOSSIBLE")
        else:
            self.brand = brand
        if colour not in colourList:
              raise ValueError("IMPOSSIBLE")
        else:  
            self.colour = colour
        if enginesize < 0 or enginesize % 100 != 0:
            raise ValueError("value not supported")
        else:
            self.enginesize = enginesize
        if fuelType not in fuelList:
            raise ValueError("IMPOSSIBLE")
        else:
            self.fuelType = fuelType
        if plates[0] in letterList and plates[1] in letterList and plates[2] in numList and plates[3] in numList and plates[4] in numList and plates[5] in letterList and plates[6] in letterList:
            self.plates = plates
        else:
            raise ValueError("plates not available")
           
    def __lt__(self, other):
        if self.brand == other.brand:
            if self.model == other.model:
                return self.enginesize < other.enginesize
            else:
                return letterList.index(self.model.upper()[0]) < letterList.index(other.model.upper()[0])
        else:
            return letterList.index(self.brand.upper()[0]) < letterList.index(other.brand.upper()[0])

    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)


v = Vehicle("AB123CD")
print(v)

