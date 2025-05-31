"""
    ARGS AND KWARGS
"""
def demo(*args):
    print(args)


def demo_two(**kwargs):
    print(kwargs)

def demo_three(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)


demo(1, 2, 3)  # Output: (1, 2, 3)
demo_two(name="Alice", age=30)  # Output: {'name': 'Alice', 'age': 30}
demo_three(1, 2, 3, name="Alice", age=30)

