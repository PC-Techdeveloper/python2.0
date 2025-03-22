"""
The single responsibility principle (SRP) states that every class method, and function should have a single responsibility.

* Create a high cohesive and robust classes, methods and functions.
* Promote class composition.
* Avoid code duplication.
"""

# The Person class is responsible for managing the person's properties.
# The PersonDB class is responsible for saving the person to the database.


class PersonDB:
    def save(self, person):
        print(f"Save the {person} to the database")


class Person:
    def __init__(self, name):
        self.name = name
        self.db = PersonDB()

    def __repr__(self):
        return f"Person(name={self.name})"

    def save(self):
        self.db.save(person=self)


if __name__ == "__main__":
    p = Person("Jhon Doe")
    p.save()
