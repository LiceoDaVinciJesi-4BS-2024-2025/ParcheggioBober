#Parking

from parking_spot import *

class Parking:
    def __init__(self, spotsMaxCars: int, spotsMaxMotorBikes: int):
        self.__spotsMaxCars = spotsMaxCars
        self.__spotsFreeCars = self.__spotsMaxCars
        self.__spotsMaxMotorBikes = spotsMaxMotoBikes
        self.__spotsFreeMotorBikes = self.__spotsMaxMotorBikes
        self.__parkingSpotsCars = []
        
    @property
    def spotsMaxCars(self):
        return self.__spotsMaxCars
    @property
    def spotsMaxMotorBikes(self):
        return self.__spotsMaxMotorBikes
    
    def reserveSpotCar(self, vehiclePlate: str):
        if len(self.__parkingSpotsCars) < self.__spotsMaxCars:
            pass
        pass
            
