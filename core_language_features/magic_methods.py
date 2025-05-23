# Understanding __init__ and __str__ methods in Python

class ExampleClass:
    def __init__(self, name, value):
        """
        __init__ is a special method in Python classes, also known as a constructor.
        It is called automatically when an object of the class is created.

        Parameters:
        name (str): The name of the object.
        value (int): A value associated with the object.
        """
        self.name = name
        self.value = value

    def __str__(self):
        """
        __str__ is a special method in Python classes used to define a string representation of an object.
        It is called when the object is printed or converted to a string.

        Returns:
        str: A human-readable string representation of the object.
        """
        return f"ExampleClass(name={self.name}, value={self.value})"

# Example of additional magic methods

class ArithmeticExample:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        """Defines behavior for the + operator."""
        return ArithmeticExample(self.value + other.value)

    def __repr__(self):
        """Defines a developer-friendly string representation."""
        return f"ArithmeticExample(value={self.value})"

class ComparisonExample:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        """Defines behavior for the == operator."""
        return self.value == other.value

    def __lt__(self, other):
        """Defines behavior for the < operator."""
        return self.value < other.value

# Example usage
if __name__ == "__main__":
    obj = ExampleClass("Sample", 42)
    print(obj)  # This will call the __str__ method

    # ArithmeticExample usage
    obj1 = ArithmeticExample(10)
    obj2 = ArithmeticExample(20)
    obj3 = obj1 + obj2  # Calls __add__
    print(obj3)  # Calls __repr__

    # ComparisonExample usage
    comp1 = ComparisonExample(5)
    comp2 = ComparisonExample(10)
    print(comp1 == comp2)  # Calls __eq__
    print(comp1 < comp2)   # Calls __lt__