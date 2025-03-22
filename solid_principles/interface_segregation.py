"""
The interface segregation principle states that an interface should be as small a possible in terms of cohesion. In other words, it should do ONE thing.

An interface is a description of behaviors that an object can do. For example, when you press the power button on the TV remote control, it turns the TV on, and you don’t need to care how.
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class Car(Vehicle):
    def go(self):
        print("Going to work")

    def fly(self):
        return Exception("The car can't fly")


class Movable(ABC):
    @abstractmethod
    def go(self):
        pass


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Aircraft(Flyable):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")


class Car(Movable):
    def go(self):
        print("Going to work in a car")


if __name__ == "__main__":
    car = Car()
    car.go()

    aircraft = Aircraft()
    aircraft.go()
    aircraft.fly()
