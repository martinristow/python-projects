def calculate(n, **kwargs):
    print(kwargs)  # ova pecati dictionary ili recnik
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    n /= kwargs["divide"]
    return n


amount = calculate(2, add=5, divide=10, multiply=4)
print(f"Calculate: {amount}")


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)
