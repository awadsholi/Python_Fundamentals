from typing import Union


class Vehicle:

        wheels: int = 4 #class attribute (shared by all instances)

        def __init__(self, make:str , model:str, year:int): #constructor initializer ,,, self is reference for current instance

            self.make = make      #public
            self.model = model    #public
            self._year = year     #protected
            self.__mileage = 0    #private

        def description(self) ->str: #instance method ,For actions specific to an individual instance

            return  f"{self._year} {self.make} {self.model}"

        @classmethod
        def from_year(cls,make:str , model:str, current_year:int): #class method (alternative constructor)
            age = 3
            return cls(make, model, current_year - age)

        @staticmethod
        def is_vintage(year:int)->bool: # functions related to class but not needing instance or class data
            return (2025 - year) >=25

        def __str__(self)->str :
            return  f"Vehicle: {self.description()} with {self.__mileage} miles"

        @property
        def mileage(self) -> int :
            return self.__mileage

        @mileage.setter
        def mileage(self,value:int)-> None:
            if value >= 0:
                self.__mileage = value


class ElectricCar(Vehicle):
        def __init__(self, make:str , model:str, year:int, battery:int ) ->None:
            super().__init__(make, model , year)
            self.__battery = battery

        def description(self)->str:
           base_dec =  super().description()
           return f"description of electric Car {base_dec} with battery {self.__battery}"





if __name__ == "__main__":
    car = Vehicle("Volks","polo", 2015)
    el_Car = ElectricCar("Ionic","s",2025,150)

    old_car = Vehicle.from_year("Ford","Mustang", 2025)

    print(car.description())
    print(el_Car.description())
    print(old_car.description())

    el_Car.mileage = 1000
    print(el_Car.mileage)

    print(str(car))

    print(f"Is Vintage",{Vehicle.is_vintage(1995)})
