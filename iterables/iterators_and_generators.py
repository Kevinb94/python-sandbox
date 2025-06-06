# iterators_and_generators.py

# ✅ 1. Basic Iterator Example (using __iter__ and __next__)

class CountToThree:
    def __init__(self):
        self.numbers = [1, 2, 3]
        self.index = 0

    def __iter__(self):
        return self  # An iterator must return itself

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        value = self.numbers[self.index]
        self.index += 1
        return value


# ✅ 2. Generator Function (using yield)

def count_up_to(n):
    print("Starting generator")
    for i in range(1, n + 1):
        print(f"Yielding: {i}")
        yield i  # Each call to next() resumes from here


# ✅ 3. Generator Expression (one-liner)

squares = (x * x for x in range(5))  # Similar to a list comprehension, but lazy


# ✅ 4. Real-world example: reading a file lazily

def read_lines(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()  # Yield lines one by one


# ✅ Run examples

def demo_iterators():
    print("Iterator Demo:")
    counter = CountToThree()
    for num in counter:
        print(num)

def demo_generators():
    print("\nGenerator Function Demo:")
    for number in count_up_to(3):
        print(f"Received: {number}")

    print("\nGenerator Expression Demo:")
    for sq in squares:
        print(sq)

if __name__ == "__main__":
    demo_iterators()
    demo_generators()

    # Note: To test read_lines, create a small .txt file in the same folder and uncomment:
    # for line in read_lines("example.txt"):
    #     print(line)