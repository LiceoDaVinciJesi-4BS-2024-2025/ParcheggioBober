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
        free: bool,
        datetimeOfLeaving: datetime.datetime):
        self.__vehicleType = vehicleType
        self.__vehiclePlates = vehiclePlates
        self.__free = free
        self.__datetimeOfLeaving = datetimeOfLeaving
    
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
    
