#Motorbike

import vehicle

class Motorbike(vehicle.Vehicle):
    def __init__(self,
        plates: str,
        brand: str = "Toyota",
        model: str = "Yaris",
        colour: str = "Yellow",
        enginesize:int = 100,
        fuelType: str = "Diesel",
        passengersMax: int = 2,
        passengersOnBoard: int = 2):
        
        super().__init__(plates, brand, model, colour, enginesize, fuelType)
        self.__passengersMax = passengersMax
        self.__passengersOnBoard = passengersOnBoard
        
