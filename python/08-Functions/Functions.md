# Functions

Functions are reusable blocks of code that perform a specific task. They help to organize code, make it more readable, and allow for code reuse.

## Defining a Function

This is a simple function named `greet_user()` that prints a greeting:

```python
def greet_user():
    """
    Display a simple greeting.
    """
    print("Hello!")

# Call the function
greet_user()
# Output: Hello!
```

We use the keyword `def` to inform Python that we are defining a function which tells Python the name of the function and if applicable, what kind of information the function needs to do its job. The parentheses hold that information. In this case, the name of the function is `greet_user()` and it needs no information to do its job, so its parentheses are empty, but are regardless required. Finally, the definition ends in a colon.

Any indented lines that follow `def greet_user():` make up the body of the function. The text on the second line is a comment known as a `docstring`, which describes what the function does. When Python generates documentation for the functions in our programs, it looks for a string immediately after the function's definition. These strings are usually enclosed in triple quotes which lets us write multiple lines.

The line `print("Hello!")` is the only line of actual code in the body of the function, so `greet_user():` has just one job: `print("Hello!")`. 

When we want to use this function, we have to call it. A `function call` tells Python to execute the code in the function. To call a function, we write the name of the function, followed by any necessary information in parentheses.

### Passing information to a Function

If we modify our `greet_user()` function slightly, we can greet the user by name. We can enter `username` in the parentheses of the function's definition at `def greet_user()` which would allow the function to accept any value of username we specify. The function would now expect us to provide a value of `username` every time we call it.

```python
def greet_user(username):
    """
    Display a simple greeting.
    """
    print(f"Hello, {username.title()}!")

greet_user('Jessie')
# Output: Hello, Jessie!
```

Likewise, entering a different name, such as Pius, would print out `Hello, Pius!`

### Arguments and Parameters

In the previous example, we defined our `greet_user()` function to require a value for the variable `username` which then upon calling the function, we gave it the information, a person's name, to print the right greeting.

The variable `username` is an example of a `parameter`, which is a piece of information the function needs to do its job. The value `Jessie` in `greet_user('Jessie')` is an example of an argument. 

An `argument` is a piece of information that is passed from a function call to a function. When we call the function, we place the value we want the function to work with in parentheses.

### Try It Yourself

1. A function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.

```python
def display_message():
    """
    Display a message of what I am learning about in this chapter
    """
    print("I am learning everything and anything about functions in this chapter!")

display_message()
```

2. Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as `One of my favorite books is Alice in Wonderland`. Call the function, making sure to include a book title as an argument in the function call.

```python
def favorite_book(book_title):
    """
    Display a favorite book
    """
    print(f"One of my favorite books is {book_title.title()}.")

favorite_book("Alice in wonderland")
```

## Passing Arguments

A function definition can have multiple parameters, and may therefore need multiple arguments. We can pass arguments to our functions in various ways: `positional arguments` which need to be in the same order the parameters were written; `keyword arguments` where each argument consists of a variable name and a value; and lists and dictionaries of values.

### Positional Arguments

When we call a function, Python must match each argument in the function call with a parameter in the function definition. The simplest way to do this is based on the order of the arguments provided. Values matched up this way are known as `positional arguments`. 

Consider the function below that displays information about pets. The function tells us what kind of animal each pet is and the pet's name, as shown below:

```python
def describe_pet(animal_type, pet_name):
    """
    Display information about a pet.
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('dog', 'simba')
# Output: 
# I have a dog.
# My dog's name is Simba.
```

For the above to work, we supply our function `describe_pet()` with two variables for the two parameters which then prints out the output about the pet being described.

#### Multiple Function Cals

We can call a function as many times as needed. Describing a second, different pet requires just one more call to `describe_pet():`

```python
def describe_pet(animal_type, pet_name):
    """
    Display information about a pet.
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('dog', 'simba')
describe_pet('cat', 'rembo')
# Output: 
# I have a dog.
# My dog's name is Simba.

# Output: 
# I have a cat.
# My cat's name is Rembo.
```

#### Order Matters in Positional Arguments

We can get unexpected results if we mix up the order of the arguments in a function call when using positional arguments:

```python
def describe_pet(animal_type, pet_name):
    """
    Display information about a pet.
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('simba', 'dog')
# Output: 
# I have a simba.
# My simba's name is Dog.
```

### Keyword Arguments

A `keyword argument` is a name-value pair that you pass to a function. We directly associate the name and the value within the argument, so when we pass the argument to the function, there is no confusion of which value to pass where. 


```python
def describe_pet(animal_type, pet_name):
    """
    Display information about a pet.
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='dog', pet_name='simba')
# Output: 
# I have a dog.
# My dog's name is Simba.
```

### Default Values

When writing a function, we can define a `default value` for each parameter. So, if an argument for a parameter is provided in the function call, Python uses the argument value and if not, it uses the parameter's default value. 

For example, we could define our `animal_type` as a `dog` in default;

```python
def describe_pet(pet_name, animal_type='dog'):
    """
    Display information about a pet.
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('simba')
# Output: 
# I have a dog.
# My dog's name is Simba.
```

Note that we have also changed the order of the parameters in the function definition since the default value makes it unnecessary to specify a type of animal as an argument. So, we are left with `pet_name` as the only parameter and Python will still interpret this as a positonal argument so if the function is called with just a pet's name, that argument will match with the first parameter listed in the function's definition. This is the reason the first parameter needs to be `pet_name`.

### Equivalent Function Calls