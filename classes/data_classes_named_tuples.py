from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int


# The above code is equivalent to writing the following code:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"


from collections import namedtuple

Person = namedtuple("Person", ["name", "age"])
p = Person("Alice", 30)
print(p.name)  # Alice
