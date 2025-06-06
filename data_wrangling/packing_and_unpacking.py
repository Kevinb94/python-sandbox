# packing_and_unpacking.py

# ✅ 1. Positional Packing with *args

def print_all_args(*args):
    print("Received positional args:", args)

print_all_args(1, 2, 3, "hello")


# ✅ 2. Keyword Packing with **kwargs

def print_all_kwargs(**kwargs):
    print("Received keyword args:", kwargs)

print_all_kwargs(name="Kevin", age=30)


# ✅ 3. Unpacking a List or Tuple

numbers = [1, 2, 3]
a, b, c = numbers  # Unpacks each value into separate variables
print("Unpacked from list:", a, b, c)


# ✅ 4. Unpacking with * (grab the rest)

head, *tail = [10, 20, 30, 40]
print("Head:", head)
print("Tail:", tail)


# ✅ 5. Dictionary Unpacking with **

person = {"name": "Alice", "city": "NYC"}
def greet(name, city):
    print(f"Hello {name} from {city}!")

greet(**person)  # Unpacks dict keys as function arguments


# ✅ 6. Combining *args and **kwargs

def describe_person(*traits, **details):
    print("Traits:", traits)
    print("Details:", details)

describe_person("friendly", "funny", name="Bob", age=25)


# ✅ 7. Merging Containers with Unpacking

dict1 = {"a": 1}
dict2 = {"b": 2}
merged = {**dict1, **dict2}
print("Merged dictionary:", merged)

list1 = [1, 2]
list2 = [3, 4]
combined = [*list1, *list2]
print("Combined list:", combined)