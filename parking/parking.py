#Parking

from parking_spot import *

class Parking:
    def __init__(self):
        self.__spotsMaxCars = 1000
        self.__spotsMaxMotorBikes = 500
        self.__parkingSpotsCars = []
        self.__parkingSpotsMotorBikes = []
    
    
        
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
            
