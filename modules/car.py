class Car:
    __name: str
    __max_speed: int

    def __init__(self, name: str, max_speed: int):
        self.__name = name
        self.__max_speed = max_speed

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def max_speed(self) -> int:
        return self.__max_speed
    
    def info(self) -> str:
        return f'{self.name}, {self.max_speed}'
    
class CountryCar(Car):
    __country: str

    def __init__(self, name: str, max_speed: int, country: str):
        super().__init__(name, max_speed)
        self.__country = country

    @property
    def country(self) -> str:
        return self.__country
    
    """ def info(self) -> str:
        return f'{super().info()}, {self.country}' """
