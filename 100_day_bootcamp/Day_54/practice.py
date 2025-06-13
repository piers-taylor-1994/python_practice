import time
def delay_decorator(function):
    def wrapper_function():
        time.sleep(1)
        function()
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello!")

@delay_decorator
def say_bye():
    print("Bye!")

say_hello()