#Parking Spot

from motorbike import *
from car import *
import datetime

vehicleTypes = ["Car", "Motorbike"]

class ParkingSpot:
    def __init__(
        self,
        vehicleType,
        vehiclePlates: str,
        datetimeOfLeaving: datetime.datetime):
        
        self.__vehicleType = vehicleType
        self.__vehiclePlates = vehiclePlates
        if self.__vehiclePlates == "":
            self.__free = True
        else:
            self.__free = False
        self.__datetimeOfLeaving = datetimeOfLeaving
    
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
    
