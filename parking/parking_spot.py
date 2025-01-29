#Parking Spot

from motorbike import *
from car import *
import datetime

vehicleTypes = [Car, Motorbike]

class ParkingSpot:
    def __init__(self):
        self.__vehicleType = None
        self.__vehiclePlates = ""
        self.__free = True
        self.__datetimeOfLeaving = datetime.datetime(1, 1, 1, 1, 1)
    
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)

    @property
    def vehicleType(self):
        return self.__vehicleType

    @property
    def vehiclePlates(self):
        return self.__vehiclePlates

    @property
    def free(self):
        return self.__free

    @property
    def datetimeOfLeaving(self):
        return self.__datetimeOfLeaving
    
    def reserveSpot(self, vehicle, hoursOfOccupation: int, minutesOfOccupation: int = 0):
        if type(vehicle) not in vehicleTypes:
            raise ValueError("Invalid vehicle type")

        self.__vehiclePlates = vehicle.plates
        self.__datetimeOfLeaving = datetime.datetime.now() + datetime.timedelta(minutes = minutesOfOccupation, hours = hoursOfOccupation)
        self.__free = False
        return

    def freeSpot(self):
        self.__vehiclePlates = ""
        self.__vehicleType = None
        self.__free = True
        self.__datetimeOfleaving = datetime.datetime(1, 1, 1, 1, 1)
        return


print("--<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>--")
spot = ParkingSpot()
print(spot)
print(spot.datetimeOfLeaving)
car = Car("AB123CD")
spot.reserveSpot(car, 3, 30)
print(spot.datetimeOfLeaving)
  
