import functools

def repeat(num_items):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwars):
            for _ in range(num_items):
                result = func(*args, **kwars)
            return result
        return wrapper
    return decorator_repeat
             


@repeat(num_items=3)
def greet(name):
    print(f'Hello {name}')


greet('alex')