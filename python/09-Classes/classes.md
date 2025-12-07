# Classes

Object-oriented programming (OOP) is one of the most effective approaches to writing software. In OOP, we write `classes` that represent real-world things and situations, and then we create `objects` based on these classes. When we write a class, we define the general behavior that a whole category of objects can have. 

When we create individual objects from the class, each object is automatically equipped with the general behavior; you can then give each object whatever unique traits you desire. 

Making an object from a class is called `instantiation`, and we work with `instances` of a class. 

## An Analogy of a Class, in the simplest way possible

Think of a blueprint for building houses.

- An `instance` is the actual house built from the blueprint.

- An `attribute` is the characteristics or properties of the house

- A `Method` is its actions or behaviors.

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand # Attribute
        self.color = color # Attribute

    def drive(self): # Method
        print("Vroom!")

my_car = Car("Toyota", "Red") # Instance
```

- Instance: `my_car` - your specific car
- Attributes: `my_car.brand` (Toyota), `my_car.color` (Red) - what it has
- Methods: `my_car.drive()` - what it can do

## Creating and Using a Class

Here, we will write a simple class `Dog`, that represents a dog, any dog to be specific. Behaviors and traits of a dog, such as the name and age, rolling over and sitting, will go in the Dog class because they are common to most dogs. 

Each instance created from the `Dog` class will store a `name` and an `age`, and we will give each dog the ability to `sit()` and `roll_over():`

```python
class Dog:
    """
    A simple attempt to model a dog
    """

    def __init__(self, name, age):
        """
        Initialize name and age attributes
        """
        self.name = name
        self.age = age

    def sit(self):
        """
        Simulate a dog sitting in response to a command
        """
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """
        Simulate rolling over in response to a command
        """
        print(f"{self.name} rolled over!")
```

Some things to note are that after defining our class called `Dog`, the capitalized name refers to a class in Python. There are no parentheses in the class definition because we are creating this class from scratch. We then write a docstring describing what this class does.

### The __init__() Method

A function that is part of a class is a `method`. 

The `__init__()` method is a special method that Python runs automatically whenever we create a new instance based on the `Dog` class. This method has two leading underscores and two trailing underscores, a convention that helps prevent Python's default method names from conflicting with our method names. 

We make sure to use two underscores on each side of `__init__()`. If we use just one on each side, the method will not be called automatically when we use our class, which can result in errors that are difficult to identify.

We define the `__init__()` method to have three parameters: `self`, `name`, and `age`. The `self` parameter is required in the method definition, and it must come first, before the other parameters. It must be included in the definition because when Python calls this method later (to create an instance of `Dog`), the method call will automatically pass the `self` argument. Every method call associated with an instance automatically passes `self`, which is a reference to the instance itself; it gives the individual instance access to the attributes and methods in the class.

When we make an instance of `Dog`, Python will call the `__init__()` method from the `Dog` class. We will pass `Dog()` a name and an age as arguments; self is passed automatically, so we do not need to pass it. Whenever we want to make an instance from the `Dog` class, we will provide values for only the last two parameters, `name`, and `age`.

The two variables defined in the body of the `__init__()` method each have the prefix `self`. Any variable prefixed with `self` is available to every method in the class, and we will also be able to access these variables through any instance created from the class. The line `self.name = name` takes the value associated with the parameter `name` and assigns it to the variable `name`, which is then attached to the instance being called. The same process happens with `self.age` = `age`. Variables that are accessible through instances like this are called `attributes`.

The `Dog` class has two other methods defined: `sit()` and `roll_over()`. Since these methods do not need additional information to run, we just define them to have one parameter, `self`. The instances we create later will have access to these methods. In other words, they will be able to sit and roll over. For now, `sit()` and `roll_over()` do simply print a message, saying the dog is sitting or rolling over. 

### Making an Instance from a Class

Think of a class as a set of instructions for how to make an instance. The `Dog` class is a set of instructions that tells Python how to make individual instances representing specific dogs.

```python
class Dog:
    """
    A simple attempt to model a dog
    """

    def __init__(self, name, age):
        """
        Initialize name and age attributes
        """
        self.name = name
        self.age = age

    def sit(self):
        """
        Simulate a dog sitting in response to a command
        """
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """
        Simulate rolling over in response to a command
        """
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Output
# >>> my_dog = Dog("Willie", 6)
# >>> print(f"My dog's name is {my_dog.name}.")
# My dog's name is Willie.
# >>> print(f"My dog is {my_dog.age} years old.")
# My dog is 6 years old.
```

#### Accessing Attributes

To access the attributes of an instance, you can use the dot notation. We access the value of my_dog's attribute `name` by writing: `my_dog.name`

Here, Python would look at the instance `my_dog` and then find the attribute `name` associated with `my_dog`. This is the same attribute referred to as `self.name` in the class `Dog`.

```python
# >>> print(f"My dog's name is {my_dog.name}.")
# My dog's name is Willie.
# >>> print(f"My dog is {my_dog.age} years old.")
# My dog is 6 years old.
```

#### Calling Methods

After we create an instance from the class `Dog`, we can use the dot notation to call any method defined in `Dog`.

```python
class Dog:
    --snip--

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

# Output:
# >>> my_dog = Dog('Willie', 6)
# >>> my_dog.sit()
# Willie is now sitting.
# >>> my_dog.roll_over()
# Willie rolled over!
```

When Python reads `my_dog.sit()`, it looks for the method `sit()` in the class Dog and runs that code. Same is done for `my_dog.roll_over()`. 

#### Creating Multiple Instances

We can create as many instances from a class as we need. For example, we can create a second dog called `your_dog`

```python
class Dog:
    """
    A simple attempt to model a dog
    """

    def __init__(self, name, age):
        """
        Initialize name and age attributes
        """
        self.name = name
        self.age = age

    def sit(self):
        """
        Simulate a dog sitting in response to a command
        """
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """
        Simulate rolling over in response to a command
        """
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Steve', 4)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")

# Output:
# >>> my_dog = Dog("Willie", 6)
# >>> your_dog = Dog("Steve", 4)
# >>> print(f"My dog's name is {my_dog.name}.")
# My dog's name is Willie.
# >>> print(f"My dog is {my_dog.age} years old.")
# My dog is 6 years old.
# >>> print(f"Your dog's name is {your_dog.name}.")
# Your dog's name is Steve.
# >>> print(f"Your dog is {your_dog.age} years old.")
# Your dog is 4 years old.
```

We can make as many instances from one class as we need, as long as we give each instance a unique variable name or it occupies a unique spot in a list or dictionary.

## Working with Classes and Instances

We can use classes to represent many real-world situations. Once we write a class, we will spend most of our time working with instances created from that class. 

One of the first tasks we will want to do is modify the attributes associated with a particular instance. You can modify the attributes of an instance directly or write methods that update attributes in specific ways.

In the example below of a car class, we will store information about the kind of car we are working with, and it will have a method that summarizes this information:

```python
class Car:
    """
    A simple attempt to represent a car
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes to describe a car
        """
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """
        Return a neatly formatted descriptive name
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

# Output:
# >>> user.describe_user()
# This user is known as Pius Mutuma
# >>> user.greet_user()
# Hello, Pius Mutuma!
```

### Setting a Default Value for an Attribute

When an instance is created, attributes can be defined without being passed in as parameters. These attributes can be defined in the `__init__()` method, where they are assigned a default value.

For example, let us add an attribute called `odometer_reading` that always starts with a value of 0. We will also add a method `read_odometer()` that helps us read each car's odometer.

```python
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

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
print(my_new_car.read_odometer())

# Output:
# >>> print(my_new_car.get_descriptive_name())
# 2024 Audi A4
# >>> print(my_new_car.read_odometer())
# This car has 0 miles on it.
# None
```

When Python calls the `__init__()` method to create a new instance, it stores the make, model, and year values as attributes, like it did before. Then, it creates a new attribute called `odometer_reading` and sets its initial value to 0 and so, our car starts with a mileage of 0. However, not many cars are sold with exactly 0 miles on the odometer, so we need a way to change the value of this attribute.

### Modifying Attribute Values

We can change an attribute's value in three ways; change the value directly through an instance, set the value through a method, or increment the value through a method.

#### Modifying an Attribute's Value Directly

The simplest way to modify the value of an attribute is to avvess the attribute directly through an instance. Here, we set the odometer reading to 23 directly:

```python
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


my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23 # Set an explicit value
print(my_new_car.read_odometer())

# Output:
# >>> print(my_new_car.get_descriptive_name())
# 2024 Audi A4
# >>> my_new_car.odometer_reading = 23
# >>> print(my_new_car.read_odometer())
# This car has 23 miles on it.
# None
```

We use the dot notation to access the car's `odometer_reading` attribute, and set its value directly. This line tells Python to take the instance `my_new_car`, find the attribute `odometer_reading` associated with it, and set the value of that attribute to 23.

#### Modifying an Attribute's Value Through a Method

It can be helpful to have methods that update certain attributes for us. Instead of accessing the attribute directly, we pass the new value to a method that handles the updating internally. 

```python
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
        Set the odometer reading to the given value
        """
        self.odometer_reading = mileage

my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23) # Update here
print(my_new_car.read_odometer())

# Output:
# >>> my_new_car = Car("audi", "a4", 2024)
# >>> print(my_new_car.get_descriptive_name())
# 2024 Audi A4
# >>> my_new_car.update_odometer(23)
# >>> print(my_new_car.read_odometer())
# This car has 23 miles on it.
# None
```

Our new function, `update_odometer()` takes in a mileage value and assigns it to `self.odometer_reading`. Using the `my_new_car` instance, we call `update_odometer()` with 23 as an argument. This sets the odometer reading to 23, and then `read_odometer()` prints out the reading with miles updated.

We can extend the method `update_odometer()` to do additional work every time the odometer reading is modified, such as ensuring no one tries to roll back the odometer reading.

```python
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

my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
print(my_new_car.read_odometer())
```

Now, `update_odometer()` checks that the new reading makes sense before modifying the attribute. If the value provided for `mileage` is greater than or equal to the existing mileage, `self.odometer_reading`, we can update the odometer reading to the new mileage, otherwise, it warns us.

#### Incrementing an Attribute's Value Through a Method

We may also want to increment an attribute's value by a certain amount, rather than set an entirely new value. Say we buy a used car and put 100 miles on it between the time we buy it and the time we register it. 

```python
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

my_used_car = Car("audi", "a4", 2024)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
print(my_used_car.read_odometer())

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# Output:
# >>> my_used_car = Car("audi", "a4", 2024)
# >>> print(my_used_car.get_descriptive_name())
# 2024 Audi A4
# >>> my_used_car.update_odometer(23_500)
# >>> print(my_used_car.read_odometer())
# This car has 23500 miles on it.
# None
# >>> my_used_car.increment_odometer(100)
# >>> my_used_car.read_odometer()
# This car has 23600 miles on it.
```

## Inheritance

When writing a class, we do not always have to start from scratch. 

If the class we are writing is a specialize version of another class we wrote earlier, we can use `inheritance`. When one class inherits from another, it takes on the attributes and methods of the first class. The original class is called the `parent class`, and the new class is the `child class`. 

The child class can inherit any or all of the attributes and methods of its parent class, but it is also free to define new attributes and methods of its own.

### The __init__() Method for a Child Class

When we are writing a new class based on an existing class, we will often want to call the `__init__()` method from the parent class. This will initialize any attributes that were defined in the parent `__init__()` method and make them available in the child class. 

For example, for an electric car, it is just a specific kind of car, so we can base our new `ElectricCar` class on the `Car` class we wrote earlier. Then we will only have to write code for the attributes and behaviors specific to electric cars.

```python
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

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# Output:
# >>> my_leaf = ElectricCar("nissan", "leaf", 2024)
# >>> print(my_leaf.get_descriptive_name())
# 2024 Nissan Leaf
```

When we create a child class, the parent class must be part of the current file and must appear before the child class in the file. We then define the child class, `ElectricCar` and include the name of the parent class in the parentheses in the definition of a child class: `class ElectricCar(Car)`. Then the `__init__()` method takes in the information required to make a Car instance.

The `Super()` function is a special function that allows us to call a method from the parent class. Here, we call the `__init__()` method from our parent class, which gives the child class, `ElectricCar` instance all the attributes defined in that method. The name `super` comes from a convention of calling the parent class a `superclass` and the child class a `subclass`.

We then test whether the inheritance is working properly by trying to create an electric car with the same kind of information we would provide when making a regular car. 

### Defining Attributes and Methods for the Child Class

Once we have a child class that inherits from a parent class, we can add any new attributes and methods necessary to differentiate the child class from the parent class. 

Updating our previous program:

```python
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
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery_size = 40
    
    def describe_battery(self):
        """
        Print a statement describing the battery size
        """
        print(f"This car has a {self.battery_size}-kWh battery")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_lead.describe_battery()

# Output:
# >>> my_leaf = ElectricCar("nissan", "leaf", 2024)
# >>> print(my_leaf.get_descriptive_name())
# 2024 Nissan Leaf
# >>> my_leaf.describe_battery()
# This car has a 40-kWh battery
# >>> 
```

We add a new attribute `self.battery_size` that is associated with all instances created in the child class and not the parent class, in any way. We can always add as many attributes and methods as we need to model an electric car to whatever degree of accuracy we need.

### Overriding Methods from the Parent Class

We can override any method from the parent class that does not fit what we are trying to model with the child class. To do this, we define a method in the child class with the same name as the method we want to override in attention to the method we define in the child class.

Say the class `Car` had a method called `fill_gas_tank()`. This method is meaningless for an all-electric vehicle so we might want to override this method:

```python
class ElectricCar(Car):
    """
    Represent aspects of a car, specific to electric vehicles
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery_size = 40
    
    def describe_battery(self):
        """
        Print a statement describing the battery size
        """
        print(f"This car has a {self.battery_size}-kWh battery")

    def fill_gas_tank(self):
        """
        Electric cars do not have gas tanks
        """
        print("This car does not have a gas tank!")
```

Now, if someone tries to call `fill_gas_tank()` with an electric car, Python will ignore the method `fill_gas_tank()` in `Car` and run this code instead. 

When we use inheritance, we can make our child classes retain what we need and override anything we do not need from the parent class.

### Instances as Attributes

When modelling something from the real world in code, we may find that we are adding more and more detail to a class. Therefore, the list of attributes and methods continue to grow as well as the files. In this instance, we may realize that part of one class can be written as a separate class. We can break a large class into smaller classes that work together, an approach known as `composition`

For example, if we continue adding detail to the `ElectricCar` class, we might notice that we are adding as many attributes and methods specific to the car's battery. When we see this happening, we can stop and move those attributes and methods to a separate class, `Battery`, then use a `Battery` instance as an attribute in the `ElectricCar` class:

```python
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


class Battery:
    """
    A simple attempt to model a battery for an electric car
    """
    def __init__(self, battery_size=40):
        """
        Initialize the battery's attributes
        """
        self.battery_size = battery_size

    def describe_battery(self):
        """
        Print a statement describing the battery size
        """
        print(f"This car has a {self.battery_size}-kWh battery")


class ElectricCar(Car):
    """
    Represent aspects of a car, specific to electric vehicles
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()

# Output:
# >>> print(my_leaf.get_descriptive_name())
# 2024 Nissan Leaf
# >>> my_leaf.battery.describe_battery()
# This car has a 40-kWh battery
# >>> 
```

In the `ElectricCar` class, we add an attribute `self.battery` which tells Python to create a new instance of `Battery` with a default size of 40.

We can add another method to `Battery` that reports the range of the car based on the battery size:

```python
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


class Battery:
    """
    A simple attempt to model a battery for an electric car
    """
    def __init__(self, battery_size=40):
        """
        Initialize the battery's attributes
        """
        self.battery_size = battery_size

    def describe_battery(self):
        """
        Print a statement describing the battery size
        """
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """
        Print a statement about the range this battery provides
        """
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This can can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """
    Represent aspects of a car, specific to electric vehicles
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

Output:
# >>> my_leaf = ElectricCar("nissan", "leaf", 2024)
# >>> print(my_leaf.get_descriptive_name())
# 2024 Nissan Leaf
# >>> my_leaf.battery.describe_battery()
# This car has a 40-kWh battery
# >>> my_leaf.battery.get_range()
# This can can go about 150 miles on a full charge.
```

## Importing Classes

As we add more functionality to our classes, our files can get long, even when we use inheritance and composition properly. In keeping with the overall philosophy of Python, we will want to keep our files as uncluttered as possible. 

To help, Python lets us store classes in modules and then import the classes we need into our main program.

### Importing a Single Class

We can have a single module with just the `Car` class stored as `car.py`

```python
"""A class that can be used to represent a car."""

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
```

We add a module-level docstring that briefly describes the contents of this module. We should always write a docstring for each module we create. 

Now, we create a separate file `my_car.py` where we will import the `Car` class and then create an instance from that class:

```python
from car import Car

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Output:
# 2024 Audi A4
# This car has 23 miles on it.
```

For this, the output would be the same as before. Separating files this way helps make our main programs files clean and easy to read. Once our classes work as we want them to, we can leave those files alone and focus on the higher-level logic of our main program.

### Storing Multiple Classes in a Module

We can store as many classes as we need in a single module, although each class in a module should be related somehow. For example, classes `Battery` and `ElectricCar` both help represent cars, so we can add them to the module `car.py`

```python
"""A set of classes used to represent gas and electric cars."""

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

class Battery:
    """
    A simple attempt to model a battery for an electric car
    """
    def __init__(self, battery_size=40):
        """
        Initialize the battery's attributes
        """
        self.battery_size = battery_size

    def describe_battery(self):
        """
        Print a statement describing the battery size
        """
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """
        Print a statement about the range this battery provides
        """
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This can can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """
    Represent aspects of a car, specific to electric vehicles
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()
```

Now, we can make a new file; `my_electric_car.py` that imports the `ElectricCar` class and make an electric car:

```python
from car import ElectricCar

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

# Output:
# 2024 Nissan Leaf
# This car has a 40-kWh battery.
# This car can go about 150 miles on a full charge.
```

### Importing Multiple Classes from a Module

You can import as many classes as you need into a program file. If we want to make a regular car and electric car in the same file, we need to import both classes, `Car` and `ElectricCar`:


```python
from car import Car, ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# Output:
# 2024 Ford Mustang
# 2024 Nissan Leaf
```

### Importing an Entire Module

We can import an entire module and then access the classes we need using the dot notation. This approach is simple and results in code that is easy to read. 

```python
import car

my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
```

We first import the entire car module. Then access the classes we need through the module_name.ClassName syntax. We again create a Ford Mustang and a Nissan Leaf.

### Importing All Classes from a Module

We can import every class from a module using the syntax: `from module_name import *`

This method is however not recommended for two reasons:

- It is helpful to be able to read the import statements at the top of a file and get a clear sense of which classes a program uses. With this approach it is unclear which classes we are using from the module. 

- This approach can lead to confusion with names in the file. If we accidentally import a class with the same name as something else in the program, we can create errors that are hard to diagnose.

So, we are better off importing the entire module and using the `module_name.ClassName` syntax. We will not see all the classes used at the top of the file, but we will see clearly where the module is used in the program, and even avoid potential naming conflicts when importing all the classes.

### Importing a Module into a Module

We may want to spread out our classes over several modules to keep any one file from growing too large and avoid storing unrelated classes in the same module. When we store our classes in several modules, we may find that a class in one module depends on a class in another module. When this happens, we can import the required class into the first module. 

For example, lt us store the `Car` class in one module and the `ElectricCar` and `Battery` classes in a separate module. We will make a new module called `electric_car.py` replacing the `electric_car.py` file we created earlier, and copu just the `ElectricCar` and `Battery` classes into this file:

```python
"""A set of classes that can be used to represent electric cars."""

from car import Car

class Battery:
    """
    A simple attempt to model a battery for an electric car
    """
    def __init__(self, battery_size=40):
        """
        Initialize the battery's attributes
        """
        self.battery_size = battery_size

    def describe_battery(self):
        """
        Print a statement describing the battery size
        """
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """
        Print a statement about the range this battery provides
        """
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This can can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """
    Represent aspects of a car, specific to electric vehicles
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()
```

The class `ElectricCar` needs access to its parent class `Car`, so we import `Car` directly into the module. If we forget this line, Python will raise an error when we try to import the `electric_car` module. We must ensure the `Car` module contains only the `Car` class:


```python
"""A class that can be used to represent a car."""

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
```

Now, we can import from each module separately and create whatever kind of car we need:

```python
from car import Car
from electric_car import ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_lead.get_descriptive_name())
```

The two above are outputted as:

2024 Ford Mustang
2024 Nissan Lead

### Using Aliases

Aliases can be helpful when using modules to organize our projects' code. We can use aliases when importing classes as well. 

We can for example, give `ElectricCar` an alias in the import statement

```python
from electric_car import ElectricCar as EC

my_leaf = EC('nissan', 'leaf', 2024)
```

We can also give a module an alias. For example, importing an entire `electric_car` module using an alias:

```python
import electric_car as ec

my_leaf = ec.ElectricCar('nissan', 'leaf', 2024)
```

## Python Standard Library

The `Python Standard Library` is a set of modules included with every Python installation. 

You can always use any function or class in the standard library by including a simple import statement at the top of your file, i.e.

```python
from random import randint

randint(1, 6)
```

```python
from random import choice

food = ['meat', 'carrot broth', 'peanut broth', 'sweet potatoes']
first_up = choice(food)
first_up

# 'meat'
```

## Styling Classes

1. Class names should be written in `CamelCase`. To do this, capitalize the first letter of each word in the name, and do not use underscores. Instance and module names should be written in lowercase, with underscores between words.

2. Every class should have a docstring immediately following the class definition. The docstring should be a brief description of what the class does, and we should follow the same formatting conventions we used for writing docstrings in functions. Each module should also have a docstring describing what the classes in a module can be used for.

3. We can use blank lines to organize code, one between methods, and two between classes.

4. If we need to import a module from the standard library and a module that we wrote, place the import statement for the standard library module first. Then add a blank line and the import statement for the module we wrote. In programs with multiple import statements, this conversion makes it easier to see where the different modules used in the program come from.


## Polymorphism

The word `polymorphism` means many forms, and in programming, it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

An example of a Python function that can be used on different objects in the `len()` function:

1. `String`

For strings, `len()` returns the number of characters:

```python
x = "Hello World!"

print(len(x))

Output:
12
```

2. `Tuple`

For tuples, `len()` returns the number of items in the tuple:

```python
mytuple = ("apple", "banana", "cherry")

print(len(mytuple))

Output:
3
```

3. `Dictionary`

For dictionaries, `len()` returns the number of key/value pairs in the dictionary:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))

Output:
3
```

For Polymorphism in Class methods, we can have multiple classes with the same method name.

For example, say we have three classes: `Car`, `Boat`, and `Plane`, and they all have a method called `move()`:

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()

Output:

Drive!
Sail!
Fly!
```

Because of polymorphism we can execute the same method for all three classes.

When inheriting classes, we can still use polymorphism since the child classes inherits the parent methods, but cana still override them:

```python
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       # Create a Car object
boat1 = Boat("Ibiza", "Touring 20") # Create a Boat object
plane1 = Plane("Boeing", "747")     # Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

Output:

Ford
Mustang
Move!
Ibiza
Touring 20
Sail!
Boeing
747
Fly!
```

## Encapsulation

Encapsulation is about protecting data inside a class. 

It means keeping data (proprties) and methods together in a class, while controlling how the data can be accessed from outside the class. 

This prevents accidental changes to our data and hides the internal details of how our class works.

We use encapsulation to: Protect data, validate data, ensure flexibility in that, internal implementation can change without affecting external code, and allow for greater control over our data.

### Private Properties

We can use the double underscore __ prefix to make properties private:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

p1 = Person("Me", 25)
print(p1.name)
print(p1.__age) # This will cause an error

Output:
# >>> print(p1.name)
# Me
# >>> print(p1.__age)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Person' object has no attribute '__age'
```

To access a private property, we can create a getter method:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return self.__age

p1 = Person("Me", 25)
print(p1.name)
print(p1.get_age())

Output:
# >>> print(p1.name)
# Me
# >>> print(p1.get_age())
# 25
```

To modify a pribate property, we can create a setter method. The setter method can also validate the value before setting it:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

p1 = Person("Me", 25)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age())

Output:
# >>> print(p1.get_age())
# 25
# >>> p1.set_age(26)
# >>> print(p1.get_age())
# 26
```

### Private Methods

We can also make methods private using double underscore prefix:

```python
class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, num):
        if not isinstance(num, (int, float)):
            return False
        return True

    def add(self, num):
        if self.__validate(num):
            self.result += num
        else:
            print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)

Output:
15
```

If we try and call `calc.__validate(5)` in the above example, it would return an error. Private methods cannot be called directly from outside the class. 

### Name Mangling

Name mangling is how Python implements private properties and methods.

When we use double underscores __, Python automatically renames it internally by adding `__ClassName` in front. For example, `__age` becomes `_Person__age`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age) # Not recommended!

Output:
>>> print(p1._Person__age) # Not recommended!
30
```

Note: While you can access private properties using the mangled name, it's not recommended. It defeats the purpose of encapsulation.