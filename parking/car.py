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
        passengersOnBoard: int = 3,
        weightMax: int = 20,
        wieghtTransported: int = 10):

        super().__init__(plates, brand, model, colour, enginesize, fuelType)

        if passengersMax < 1:
            raise ValueError("passengersMax must be positive")
        else:
            self.__passengersMax = passengersMax
         
        if passengersOnBoard > self.__passengersMax:
            raise ValueError("The number of passengers can not be more than the passengers max quantity")
        else:
            self.__passengersOnBoard = passengersOnBoard

    @property
    def passengersMax(self):
        return self.__passengersMax

    @passengersMax.setter
    def passengersMax(self, value):
        if passengersMax < 1:
            raise ValueError("passengersMax must be positive")
        else:
            self.__passengersMax = passengersMax

    @property
    def passengersOnBoard(self):
        return self.__passengersOnBoard

    @passengersOnBoard.setter
    def passengersOnBoard(self, value):
         if passengersOnBoard <= self.__passengersMax:
            self.__passengersOnBoard = passengersOnBoard
            return
         raise ValueError("The number of passengers can not be more than the passengers max quantity")

    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)

if __name__ == "__main__":

    c = Car("AB123CD")
    print(c)
