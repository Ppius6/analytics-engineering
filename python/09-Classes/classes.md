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