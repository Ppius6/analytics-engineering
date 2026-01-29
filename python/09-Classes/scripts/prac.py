class Car:
    """Modelling a car"""

    def __init__(self, name, engine, mileage):
        """Initialize name, engine, and milage attributes"""
        self.name = name
        self.engine = engine
        self.mileage = mileage

    def car_name(self):
        """Return the name of the car"""
        print(f"This car is {self.name}")

    def display_engine(self):
        """Output the engine of the car"""
        print(f"The engine of this {self.name} is {self.engine}")

    def car_mileage(self):
        """Output the distance covered by the car, in total"""
        print(f"The total distance covered is {self.mileage}")


my_car = Car("Mazda 3", "1500cc", 82999)
print(my_car.name)
print(my_car.engine)
print(my_car.mileage)

my_car.car_mileage()
my_car.car_name()
my_car.display_engine()


class Car:

    def __init__(self, make, model, year):
        """
        Initialize attributes to describe a car
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """
        Return a neatly formatted descriptive name
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """
        Print a statement showing the car's mileage
        """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer! Mchezo wa Taoni!")

    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading
        """
        self.odometer_reading += miles


class ElectricCar(Car):
    """
    Represent aspects of a car, specific to electric vehicles
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        """
        super().__init__(make, model, year)


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
