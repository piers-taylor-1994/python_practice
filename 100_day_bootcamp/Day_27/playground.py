def add(*args):
    total = 0
    for a in args:
        total += a
    return total

print(add(1,5,7,10,13))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n
print(calculate(1, add=3, multiply=5))

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
    
car = Car(make="Honda")
print(car.model)