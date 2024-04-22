from modules.car import Car, CountryCar

class CarFabric:
    country: str = 'Kazakhstan'

    @classmethod
    def create_car(cls, type: int, name: str, max_speed: int) -> Car:
        match type:
            case 1:                 
                return CountryCar(name, max_speed, cls.country)
            case _:
                return Car(name, max_speed)
