# Demonstrates various list and array operations in Python

def list_traversal():
    """Traverse a list and print each element."""
    my_list = [1, 2, 3, 4, 5]
    for item in my_list:
        print(item)

def list_comprehension():
    """Use list comprehension to create a new list."""
    my_list = [x**2 for x in range(10)]
    print(my_list)

def filter_list():
    """Filter elements in a list based on a condition."""
    my_list = [1, 2, 3, 4, 5, 6]
    filtered = [x for x in my_list if x % 2 == 0]
    print(filtered)

def map_list():
    """Apply a function to each element in a list using map."""
    my_list = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, my_list))
    print(squared)

def reduce_list():
    """Reduce a list to a single value using functools.reduce."""
    from functools import reduce
    my_list = [1, 2, 3, 4, 5]
    product = reduce(lambda x, y: x * y, my_list)
    print(product)

def array_operations():
    """Demonstrate array operations using the array module."""
    from array import array
    my_array = array('i', [1, 2, 3, 4, 5])
    my_array.append(6)
    my_array.remove(3)
    print(my_array)

def slicing_lists():
    """Demonstrate slicing operations on lists."""
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(my_list[2:5])  # Slice from index 2 to 4
    print(my_list[:3])   # First three elements
    print(my_list[5:])   # Elements from index 5 onward

def list_sorting():
    """Sort a list in ascending and descending order."""
    my_list = [5, 2, 9, 1, 5, 6]
    my_list.sort()  # Ascending
    print(my_list)
    my_list.sort(reverse=True)  # Descending
    print(my_list)

def list_querying():
    """Query elements in a list using conditions."""
    my_list = [1, 2, 3, 4, 5, 6]
    print(3 in my_list)  # Check if 3 is in the list
    print(my_list.index(4))  # Find the index of 4

def is_palindrome(word):
    """Check if a given word is a palindrome."""
    word = str(word)
    return word == word[::-1]

def main():
    """Call all functions to demonstrate their functionality."""
    print("List Traversal:")
    list_traversal()

    print("\nList Comprehension:")
    list_comprehension()

    print("\nFilter List:")
    filter_list()

    print("\nMap List:")
    map_list()

    print("\nReduce List:")
    reduce_list()

    print("\nArray Operations:")
    array_operations()

    print("\nSlicing Lists:")
    slicing_lists()

    print("\nList Sorting:")
    list_sorting()

    print("\nList Querying:")
    list_querying()

    print("\nPalindrome Check:")
    print(is_palindrome("radar"))  # True
    print(is_palindrome("hello"))  # False

if __name__ == "__main__":
    main()
