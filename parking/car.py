#Car

from vehicle import Vehicle

class Car(Vehicle):
    def __init__(
        self,
        plates: str,
        brand: str = "Toyota",
        model: str = "Yaris",
        colour: str = "Yellow",
        enginesize:int = 100,
        fuelType: str = "Diesel",
        passengersMax: int = 4,
        passengersOnBoard: int = 10,
        weightMax: int = 20,
        wieghtTransported: int = 10):

        super().__init__(plates, brand, model, colour, enginesize, fuelType)
        
        self.__passengersMax = passengersMax
         
        if passengersOnBoard > self.__passengersMax:
            raise ValueError("The number of passengers can not be more than the passengers max quantity")
        else:
            self.__passengersOnBoard = passengersOnBoard

    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)

c = Car("AB123CD")
print(c)
