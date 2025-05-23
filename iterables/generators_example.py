# Demonstrates Python generators and their usage

def simple_generator():
    """A simple generator that yields numbers from 1 to 5."""
    for i in range(1, 6):
        yield i


def generator_expression():
    """A generator expression for squares of numbers from 0 to 4."""
    return (x**2 for x in range(5))


def main():
    print("Simple Generator:")
    for value in simple_generator():
        print(value)

    print("\nGenerator Expression:")
    gen = generator_expression()
    for value in gen:
        print(value)

    print("\nDemonstrating next() with a generator:")
    gen2 = simple_generator()
    print(next(gen2))  # 1
    print(next(gen2))  # 2
    print(next(gen2))  # 3
    # You can continue calling next() until StopIteration is raised

if __name__ == "__main__":
    main()
