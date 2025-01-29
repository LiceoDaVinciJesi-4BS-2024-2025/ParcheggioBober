#Parking

from parking_spot import *
from car import *
from motorbike import *
import datetime

class Parking:
    def __init__(self):
        self.__spotsMaxCars = 1000
        self.__spotsMaxMotorBikes = 500
        self.__parkingSpotsCars = []
        self.__parkingSpotsMotorBikes = []
        for x in range(self.__spotsMaxMotorBikes):
            self.__parkingSpotsMotorBikes.append(ParkingSpot())
        for y in range(self.__spotsMaxCars):
            self.__parkingSpotsCars.append(ParkingSpot())
        
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
            
