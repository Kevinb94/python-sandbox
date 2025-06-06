# dunder_methods_example.py

class Animal:
    def __init__(self, name, species):
        # __init__ is the constructor. It runs when you create a new Animal.
        self.name = name
        self.species = species

    def __str__(self):
        # __str__ is called when you use print() on the object.
        return f"{self.name} the {self.species}"

    def __repr__(self):
        # __repr__ is for developers. It's used when you inspect the object in a console or debugger.
        return f"Animal(name='{self.name}', species='{self.species}')"

    def __eq__(self, other):
        # __eq__ defines behavior for the == operator
        return self.name == other.name and self.species == other.species

    def __len__(self):
        # __len__ lets you use len() on the object.
        return len(self.name)

    def __call__(self):
        # __call__ lets you call the object like a function.
        print(f"{self.name} makes a noise!")

    def __add__(self, other):
        # __add__ defines behavior for the + operator.
        return Animal(self.name + other.name, self.species + "-" + other.species)


# Try using the class and see what the dunder methods do
if __name__ == "__main__":
    dog = Animal("Buddy", "Dog")
    cat = Animal("Kitty", "Cat")

    print(dog)               # Calls __str__
    print(repr(cat))         # Calls __repr__

    print(dog == cat)        # Calls __eq__

    print(len(dog))          # Calls __len__

    dog()                    # Calls __call__

    combined = dog + cat     # Calls __add__
    print(combined)          # Uses __str__ again on the result
