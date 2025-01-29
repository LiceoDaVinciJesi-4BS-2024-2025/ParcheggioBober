#Parking Spot

from motorbike import *
from car import *
import datetime

vehicleTypes = [Car, Motorbike]

class ParkingSpot:
    def __init__(self):
        if type(vehicleType) in vehicleTypes:
            self.__vehicleType = vehicleType
        else:
            raise ValueError("Invalid value type")
        self.__vehiclePlates = ""
        self.__free = True
        self.__datetimeOfLeaving = datetime.datetime.now()
    
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
    
    def reserveSpot(self, vehicleType, hoursOfOccupation: int, minutesOfOccupation: int = 0):
        if self.__free:
            self.__vehiclePlates = vehicleType.plates
            self.__datetimeOfLeaving += datetime.timedelta(0, 0, 0, 0, minutesOfOccupation, hoursOfOccupation) #0 Days, 0 Seconds, 0 Microseconds, 0 Milliseconds, tot Minutes, tot Hours
            self.__free = False
            return True
        return False
