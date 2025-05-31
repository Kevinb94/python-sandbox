# Example to understand Python decorators

def my_decorator(func):
    # This is the decorator function
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Example 2: Decorator with arguments

def repeat_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat_decorator(times=3)
def greet(name):
    print(f"Hello, {name}!")

# Example 3: Decorating a function with arguments

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def say_message(message):
    return message

# Example 4: Class Decorator

def class_decorator(cls):
    class WrappedClass(cls):
        def __init__(self, *args, **kwargs):
            print(f"Creating an instance of {cls.__name__}")
            super().__init__(*args, **kwargs)
        def __str__(self):
            return f"[Decorated] {super().__str__()}"
    return WrappedClass

@class_decorator
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
    




def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def multiply(x, y):
    return x * y




# Example usage
if __name__ == "__main__":
    # say_hello()

    # # Example 2 usage
    # greet("Alice")

    # # Example 3 usage
    # print(say_message("This is a decorated message."))

    # # Example usage for class decorator
    # person = Person("John", 30)
    # print(person)
    multiply(3, 4)
    multiply(5, 6)