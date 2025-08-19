def debug_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} was called with:")
        print(f"  Positional arguments: {args}")
        print(f"  Keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@debug_decorator
def add(a, b, show_result=True):
    print(f"Sum: {a + b}")

# Calling the decorated function
add(5, 10, show_result=False)
