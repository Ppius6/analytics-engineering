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