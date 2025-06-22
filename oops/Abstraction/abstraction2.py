from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    def test(self):
        print("test...")

v = Vehicle()
v.start_engine()