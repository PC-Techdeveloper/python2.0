"""
The open-closed principle states that a class, method and functions should be open for extension but closed for modification.
"""

from abc import ABC, abstractmethod


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person(name={self.name})"


class PersonStorage(ABC):
    @abstractmethod
    def save(self, person):
        pass


class PersonDB(PersonStorage):
    def save(self, person):
        print(f"Save the {person} to database")


class PersonJSON(PersonStorage):
    def save(self, person):
        print(f"Save the {person} to JSON file")


class PersonXML(PersonStorage):
    def save(self, person):
        print(f"Save the {person} to an XML file")


if __name__ == "__main__":
    person = Person("Maria Anders")
    storage = PersonXML()
    storage.save(person)
