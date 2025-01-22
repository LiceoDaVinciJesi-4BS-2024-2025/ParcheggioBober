#Vehicle

import random

colorList = ["Blue", "Yellow", "Black", "White"]
brandList = ["Audi", "Nissan", "Panda", "Toyota", "BMW", "KTM"]
fuelList = ["Diesel", "Electric", "Fuel"]
letterList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

class Vehicle:
    #Init
    def __init__(
        self,
        plates: str,
        brand: str = "Toyota",
        model: str = "Yaris",
        color: str = "Yellow",
        enginesize:int = 100,
        fuelType: str = "Diesel"):
        
        self.__model = model
        
        if brand not in brandList:
            raise ValueError("IMPOSSIBLE")
        else:
            self.__brand = brand
        if color not in colorList:
              raise ValueError("IMPOSSIBLE")
        else:  
            self.__color = color
        if enginesize < 0 or enginesize % 100 != 0:
            raise ValueError("value not supported")
        else:
            self.__enginesize = enginesize
        if fuelType not in fuelList:
            raise ValueError("IMPOSSIBLE")
        else:
            self.__fuelType = fuelType
        if plates[0] in letterList and plates[1] in letterList and plates[2] in numList and plates[3] in numList and plates[4] in numList and plates[5] in letterList and plates[6] in letterList:
            self.__plates = plates
        else:
            raise ValueError("plates not available")
    
    @property
    def plates(self):
        return self.__plates
    
    @property
    def brand(self):
        return self.__brand
    
    @property
    def model(self):
        return self.__model
    
    @property
    def color(self):
        return self.__color
    
    @property
    def engineSize(self):
        return self.__enginesize
    
    @property
    def fuelType(self):
        return self.__fuelType
    
    @color.setter
    def color(self, value):
        if value in colorList:
            self.__color = value
            return
        raise ValueError("Color not in color list")
           
    def __lt__(self, other):
        if self.__brand.upper() == other.__brand.upper():
            if self.__model.upper() == other.__model.upper():
                return self.__enginesize.upper() < other.__enginesize.upper()
            else:
                return self.__model.upper() < other.__model.upper()
        else:
            return self.__brand.upper()[0] < other.__brand.upper()

    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)


v = Vehicle("AB123CD")
print(v)
v1 = Vehicle("AB124CD", "Audi")
vList = [v, v1]
vList.sort()
print(vList)

