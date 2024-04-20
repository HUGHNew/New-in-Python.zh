import functools

def log3(*args, **kwargs):
    print(f"argc: {len(args)}")
    print(args)

    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"wrapper3 called")
            return func(*args, **kwargs)

        return wrapper

    return decorator

def log2(func):
    def wrapper(*args, **kwargs):
        print(f"wrapper2 called")
        return func(*args, **kwargs)

    return wrapper

def log2unwrap(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"wrapper2 called")
        return func(*args, **kwargs)

    return wrapper

# 使用装饰器
@log3("...")
def your_func(*args, **kwargs):
    print(f"your_func called")

@log2
def your_func2(*args, **kwargs):
    print(f"your_func2 called")

@log2unwrap
def your_func3(*args, **kwargs):
    print(f"your_func3 called")

if __name__ == "__main__":
    your_func("argc")
    print('-' * 20)
    your_func2("argc")
    print('-' * 20)
    print(your_func.__name__)
    print('-' * 20)
    print(your_func3.__name__)

