from typing import List

class MonotonicStack:
    __data: List[int]

    def __init__(self, data: List[int]):
        self.__data = []
        self.add_list(data)

    def add(self, val: int):
        n = len(self.__data)

        while n > 0 and self.__data[n-1] < val:
            self.__data.pop()
            n -= 1

        self.__data.append(val)        

    def add_list(self, data: List[int]):
        for val in data:
            self.add(val)

    def data(self) -> List[int]:
        return self.__data
