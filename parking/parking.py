#Parking

from parking_spot import *
from car import *
from motorbike import *
import datetime

class Parking:
    def __init__(self):
        self.__spotsMaxCars = 1000
        self.__spotsMaxMotorBikes = 200
        self.__parkingSpotsCars = []
        self.__parkingSpotsMotorBikes = []
        self.__pricesPerHour = {
        "cars": 1.5,
        "motorbikes": 1.2
        }
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
    @property
    def parkingSpotsMotorBikes(self):
        return self.__parkingSpotsMotorBikes
    @property
    def parkingSpotsCars(self):
        return self.__parkingSpotsCars

    
    
    def reserveSpot(self, vehicle, hoursOfOccupation):
        if type(vehicle) not in vehicleTypes:
            raise ValueError("Vehicle type not available")
        if type(vehicle) == Car:
            for x in self.__parkingSpotsCars:
                if x.free:
                    x.reserveSpot(vehicle, hoursOfOccupation)
                    return
        else:
            for y in self.__parkingSpotsMotorBikes:
                if y.free:
                    y.reserveSpot(vehicle, hoursOfOccupation)
                    return
        return


    def payDay(self):
        totalMoney = 0
        for x in self.__parkingSpotsMotorBikes:
            if not x.free:
                timeOfOccupation = x.datetimeOfLeaving - datetime.datetime.now()
                money = self.__pricesPerHour * (timeOfOccupation.total_seconds() / 3600)
                totalMoney += money

        for y in self.__parkingSpotsCars:
            if not y.free:
                timeOfOccupation = y.datetimeOfLeaving - datetime.datetime.now()
                money = self.__pricesPerHour * (timeOfOccupation.total_seconds() / 3600)
                totalMoney += money

        return totalMoney

    def freeUpSpots(self):
        for x in self.__parkingSpotsMotorBikes:
            if not x.free and x.datetimeOfLeaving < datetime.datetime.now():
                x.freeSpot()

        for y in self.__parkingSpotsCars:
            if not y.free and y.datetimeOfLeaving < datetime.datetime.now():
              y.freeSpot()
        return

    def __str__(self):
        return __class__.__name__ + str({"spotsMaxCars": self.__spotsMaxCars, "spotsMaxMotorBikes": self.__spotsMaxMotorBikes, "pricesPerHour": self.__pricesPerHour})
    def __repr__(self):
        return __class__.__name__ + str({"spotsMaxCars": self.__spotsMaxCars, "spotsMaxMotorBikes": self.__spotsMaxMotorBikes, "pricesPerHour": self.__pricesPerHour})
    
    
#--<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>----<<|>>--

if __name__ == "__main__":
    parcheggioSenzaBarboni = Parking()
    print(parcheggioSenzaBarboni)
    parcheggioSenzaBarboni.freeUpSpots()
    v1 = Car("AG666ES")
    v2 = Motorbike("GG324GJ")
    v3 = Motorbike("BO111SI")
    parcheggioSenzaBarboni.reserveSpot(v1, 3)
    parcheggioSenzaBarboni.reserveSpot(v2, 2)
    parcheggioSenzaBarboni.reserveSpot(v3, 4)
    print(parcheggioSenzaBarboni)

    file = open("park.data", "w")
    file.write("Cars parking: \n")
    for x in range(parcheggioSenzaBarboni.spotsMaxCars):
        file.write(str(parcheggioSenzaBarboni.parkingSpotsCars[x]) + "\n")
    file.write("Motorbike parking: \n")
    for y in range(parcheggioSenzaBarboni.spotsMaxMotorBikes):
        file.write(str(parcheggioSenzaBarboni.parkingSpotsMotorBikes[y]) + "\n")
    file.close()
