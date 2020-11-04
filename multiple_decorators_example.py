import time

def logging_time(func):
    """Decorator that logs time"""
    def logger():
        """Function that logs time"""
        start = time.time()
        func()
        print(f"Calling {func.__name__}: {time.time() - start:.5f}")
    return logger

def simple_decorator(func):
    print("Before function call....")
    func()
    print("After function call....")
    return func

    
@simple_decorator
@logging_time
def say_hi():
    print("Hi")


@logging_time
@simple_decorator
def say_hello():
    print("Hello")
