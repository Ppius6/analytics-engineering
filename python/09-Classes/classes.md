# Classes

Object-oriented programming (OOP) is one of the most effective approaches to writing software. In OOP, we write `classes` that represent real-world things and situations, and then we create `objects` based on these classes. When we write a class, we define the general behavior that a whole category of objects can have. 

When we create individual objects from the class, each object is automatically equipped with the general behavior; you can then give each object whatever unique traits you desire. 

Making an object from a class is called `instantiation`, and we work with `instances` of a class. 

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
```

When Python reads `my_dog.sit()`, it looks for the method `sit()` in the class Dog and runs that code. Same is done for `my_dog.roll_over()`. 