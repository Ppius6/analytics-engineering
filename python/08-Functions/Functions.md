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

Since positional arguments, keyword arguments, and default values can all be used together, we will often have several equivalent ways to call a function. For example, in `def describe_pet(pet_name, animal_type='dog'):` the argument always needs to be provided for `pet_name`, and this value can be provided using the positional or keyword format. If the animal being described is not a dog, an argument for `animal_type` must be included in the call, and this argument can also be specified using the positional or keyword format.

So, all of the following calls would work for this function:


```python
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='willie')
```

Each of the above function calls would have the same output as the previous examples.

### Avoiding Argument Errors

The common error that may arise is unmatched arguments. They occur when you provide fewer or more arguments than a function needs to do its work. 

For example, failing to pass an argument to `describe_pet()` in this example;

```python
def describe_pet(pet_name, animal_type='dog'):
    """
    Display information about a pet.
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet()
```

gives a `TypeError: describe_pet() missing 1 required positional argument: 'pet_name'`

## Return Values

A function can also process some data and then return a value or a set of values. The value the function returns is called a `return value`. The return statement takes a value from inside a function and sends it back to the line that called the function. Return values allow us to move much of our program's grunt work into functions, which can simplify the body of our program.

### Returning a Simple Value

Looking at the function below that takes a first and last name, and returns a neatly formatted full name:

```python
def get_formatted_name(first_name, last_name):
    """
    Return a full name, neatly formatted.
    """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Output: Jimi Hendrix
```

The code above takes the inputs and formats the full name by adding a space between them and later converting them to title case. 

NOTE: When you call a function that returns a value, you need to provide a variable that the returned value can be assigned to. In this case, the returned value is assigned to the variable `musician`

### Making an Argument Optional

It may make sense at times to make an argument optional, so that people using the function can choose to provide extra information only if they want to. We can make use of default values to make an argument optional. 

For example, we may want to expand `get_formatted_name()` to handle middle names as well. 

```python
def get_formatted_name(first_name, middle_name, last_name):
    """
    Return a full name, neatly formatted.
    """
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'lee', 'hendrix')
print(musician)
```

However, to make it optional to add a `middle_name` argument, we can give it an empty default value and ignore the argument unless the user provides a value, and also move it to the end of the list of parameters.

```python
def get_formatted_name(first_name, last_name, middle_name=''):
    """
    Return a full name, neatly formatted.
    """
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('jimi', 'lee', 'hendrix')
print(musician)
```

In the above code, we add a conditional check to see if a middle name has been provided. If it evaluates to `True`, it adds the provided middle name to form the full name, otherwise, it returns the provided first and last name as the empty middle name will fail the if test and the else block will run. 

### Returning a Dictionary

A function can return any kind of value we may want it to. In the example below, we take in parts of a name and return a dictionary representing a person:

```python
def build_person(first_name, last_name):
    """
    Return a dictionary of information about a person.
    """
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('me', 'you')
print(musician)

# Output: {'first': 'me', 'last': 'you'}
```
We can optionally extend it to accept optional values like a middle name, age, occupation, or any other information we may have to store about a person.

```python
def build_person(first_name, last_name, age=None):
    """
    Return a dictionary of information about a person.
    """
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('me', 'you', age=30)
print(musician)

#Output: {'first': 'me', 'last': 'you', 'age': 30}
```

### Using a Function with a while Loop

We can integrate while loops to build on our previous function

```python
def get_formatted_name(first_name, last_name):
    """
    Return a full name, neatly formatted.
    """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
```

## Passing a List

We may find it useful to pass a list to a function, which can be names, numbers, or more complex objects such as dictionaries. When we pass a list to a function, the function gets direct access to the contents of the list. 

Say we have a list of users and want to print a greeting to each user. The following example sends a list of names to a function called `greet_users()` which greets each user individually:

```python
def greet_users(names):
    """
    Print a simple greeting to each user in the list.
    """
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['Pius', 'Chris', 'Mutuma', 'Douglas']
greet_users(usernames)

# Output:
# Hello, Pius!
# Hello, Chris!
# Hello, Mutuma!
# Hello, Douglas!
```

The function loops through the list it receives and prints a greeting to each user. Outside of the function, we define a list of users and then pass the list `usernames` to `greet_users()` in the function call.

### Modifying a List in a Function

When we pass a list to a function, the function can modify the list. Any changes made to the list inside the function's body are permanent allowing us to work efficiently even when we are dealing with large amounts of data. 

Consider a company that creates 3D printed models of designs that users submit. Designs that need to be printed are stored in a list, and after being printed they are moved to a separate list. 

```python
# Start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models
print("\nThe following models have been printed:")
for completed_design in completed_models:
    print(completed_design)

# Output:
# Printing model: dodecahedron
# Printing model: robot pendant
# Printing model: phone case

# The following models have been printed:
# odecahedron
# robot pendant
# phone case
```

We begin with a list of designs that need to be printed. The while loop simulates printing each design by removing a design from the end of the list, storing it in current_design, and displaying a message that the current design is being printed. It then adds the design to the list of completed models. 

The code can be further divided into two functions, each of which does a specific job; the first one printing the designs, the second one summarizing the prints that have been made.

```python
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """
    Show all the models that were printed.
    """
    print("\nThe following models have been printed:")
    for completed_design in completed_models:
        print(completed_design)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Output:
# Printing model: dodecahedron
# Printing model: robot pendant
# Printing model: phone case

# The following models have been printed:
# dodecahedron
# robot pendant
# phone case
```

### Preventing a Function from Modifying a List

We may want to prevent a function from modifying a list. For example, say we start with a list of unprinted designs and write a function to move them to a list of completed models, as in the previous example. 

We may decide that even though we have printed all the designs, we want to keep the original list of unprinted designs for our records. But because we moved all the design names out of `unprinted_designs`, the list is now empty, and the empty list is the only version we have; the original is gone.

We can pass the function a copy of the list, not the original. Any changes the function makes to the list will affect only the copy, leaving the original list intact: `function_name(list_name[:])`, `print_models(unprinted_designs[:], completed_models)`

## Try it Yourself

Start with a copy of your program from Exercise 8-10. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.

```python
messages = ["Hey, you.", "Ni mimi", "Unanikumbuka?"]
sent_messages = []


def send_messages(messages_list):
    """
    Print each message and move it to sent_messages list.
    """
    while messages_list:
        current_message = messages_list.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


send_messages(messages)

print("\nMessages in the original list:")
print(messages)

print("\nMessages in the sent_messages list:")
print(sent_messages)

# Output
# Sending message: Unanikumbuka?
# Sending message: Ni mimi
# Sending message: Hey, you.
# >>> print("\nMessages in the original list:")

# Messages in the original list:
# >>> print(messages)
# []
# >>> print("\nMessages in the sent_messages list:")

# Messages in the sent_messages list:
# >>> print(sent_messages)
# ['Unanikumbuka?', 'Ni mimi', 'Hey, you.']
```

3 - Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.

```python
messages = ["Hey, you.", "Ni mimi", "Unanikumbuka?"]
sent_messages = []


def send_messages(messages_list[:]):
    """
    Print each message and move it to sent_messages list.
    """
    while messages_list:
        current_message = messages_list.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

send_messages(messages[:])  # Pass a copy of the list

# Output
# print("\nMessages in the original list:")
# print(messages)

# print("\nMessages in the sent_messages list:")
# print(sent_messages)

# >>> send_messages(messages[:])  # Pass a copy of the list
# Sending message: Unanikumbuka?
# Sending message: Ni mimi
# Sending message: Hey, you.
# >>> print("\nMessages in the original list:")

# Messages in the original list:
# >>> print(messages)
# ['Hey, you.', 'Ni mimi', 'Unanikumbuka?']
# >>> print("\nMessages in the sent_messages list:")

# Messages in the sent_messages list:
# >>> print(sent_messages)
# ['Unanikumbuka?', 'Ni mimi', 'Hey, you.']
```

## Passing an Arbitrary Number of Arguments

We may not know how many arguments a function may need to accept. Python allows a function to collect an arbitrary number of arguments from the calling statement. 

For example, consider a function that builds a Pizza. It needs to accept a number of toppings, but we cannot know ahead of time how many toppings a person will want. So, our function would have one parameter `*toppings`, but the parameter would collect as many arguments as the calling line provides:

```python
def make_pizza(*toppings):
    """
    Print the list of toppings that have been requested.
    """
    print(toppings)

make_pizza('Veggies')
make_pizza('Veggies', 'Meat', 'Coconut')

# Output
# >>> make_pizza('Veggies')
# ('Veggies',)
# >>> make_pizza('Veggies', 'Meat', 'Coconut')
# ('Veggies', 'Meat', 'Coconut')
```

The asterisk in the parameter name tells Python to make a tuple called `toppings` with all the values this function receives. 

We can even replace the print() call with a loop that runs through the list of toppings and describes the pizza being ordered:

```python
def make_pizza(*toppings):
    """
    Summarize the pizza we are about to make.
    """
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('Veggies')
make_pizza('Veggies', 'Meat', 'Coconut')

# Output:
# Making a pizza with the following toppings:
# - Veggies
# >>> make_pizza('Veggies', 'Meat', 'Coconut')

# Making a pizza with the following toppings:
# - Veggies
# - Meat
# - Coconut
```

### Mixing Positional and Arbitrary Arguments

If we want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition. Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter.

For example, if the function needs to take in a size for the pizza, that parameter must come before the parameter `*toppings`:


```python
def make_pizza(size, *toppings):
    """
    Summarize the pizza we are about to make.
    """
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'Veggies')
make_pizza(12, 'Veggies', 'Meat', 'Coconut')

# Output:
# >>> make_pizza(16, 'Veggies')

# Making a 16-inch pizza with the following toppings:
# - Veggies
# >>> make_pizza(12, 'Veggies', 'Meat', 'Coconut')

# Making a 12-inch pizza with the following toppings:
# - Veggies
# - Meat
# - Coconut
```

Python assigns the first value it receives to the parameter size, and all the other values that come after are stored in the tupple `toppings`. The function calls include an argument for the size first, followed by as many toppings as needed.

### Using Arbitrary Keyword Arguments

We may want to accept an arbitrary number of arguments, but we may not know ahead of time what kind of information will be passed to the function. We could write functions that accept as many key-value pairs as the calling statement provides.

An example would be to build user profiles: we know we will get information about a user, but we are not sure what kind of information we would receive. 

The function `build_profile()` in the following example always takes in a first and last name, but it accepts an arbitrary number of keyword arguments as well:

```python
def build_profile(first, last, **user_info):
    """
    Build a dictionary with everything we know about a user
    """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Albert', 'Einstein', location='Nairobi', field='Physics')
print(user_profile)

# Output:
# {'location': 'Nairobi', 'field': 'Physics', 'first_name': 'Albert', 'last_name': 'Einstein'}
```

The double asterisks before the parameter `**user_info` causes Python to create a dictionary called `user_info` with all the extra name-value pairs the function reserves. Within the function, we can access the key-value pairs in user_info just as we would for any dictionary.

In the function, we add the first and last names to the user_info dictionary because we will always receive these two pieces of information from the user, and they have not been placed into the dictionary yet. Then we return the user_info dictionary to the function call line.

### Try it Yourself

8-12 - Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time.

```python
def make_sandwich(*items):
    """
    Print a summary of the sandwich that is being ordered.
    """
    print(f"\nMaking a sandwich with the following additions:")
    for item in items:
        print(f"- {item}")


make_sandwich("lettuce", "tomato", "bacon")
make_sandwich("turkey", "cheese")

# Output:
# >>> make_sandwich("lettuce", "tomato", "bacon")

# Making a sandwich with the following additions:
# - lettuce
# - tomato
# - bacon
# >>> make_sandwich("turkey", "cheese")

# Making a sandwich with the following additions:
# - turkey
# - cheese
```

8-13 - User Profile: Start with a copy of user_profile.py from page 153. Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.

```python
def build_profile(first, last, **user_info):
    """
    Build a dictionary containing everything about me.
    """
    user_info["first_name"] = first
    user_info["last_name"] = last
    
    return user_info

my_profile = build_profile("Pius", "Mutuma", location="Meru", field="Engineering", hobby="Reading")
print(my_profile)

# Output:
# {'location': 'Meru', 'field': 'Engineering', 'hobby': 'Reading', 'first_name': 'Pius', 'last_name': 'Mutuma'}
```

8-14 - Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as color and optional features. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True). Print the dictionary that’s returned to make sure all the information was stored correctly.

```python
def make_car(manufacturer, model_name, **car_info):
    """
    Build a car profile
    """
    car_info["manufacturer"] = manufacturer
    car_info["name"] = model_name
    
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

# Output:
# {'color': 'blue', 'tow_package': True, 'manufacturer': 'subaru', 'name': 'outback'}
```

## Storing your Functions in Modules

Functions offer the advantage of separating blocks of code from the main program. We can go a step further by storing our functions in a separate file known as a `module` and then `importing` that module into the main program. An `import` statement tells Python to make the code in a module available in the currently running program file.

Storing our functions in a separate file allows us to hide the details of our program's code and focus on its higher-level logic, reuse functions in many different programs. When we store our functions in separate files, we can share those files with other programmers withouthaving to share our entire program. 

There are several ways to import a module:

### 1. Importing an Entire Module

To start importing functions, we first need to create a module. A `module` is a file ending in `.py` that contains the code we want to import into our program. 

For example, in the program below, `pizza.py` we will remove everything from the file except the function:

```python
def make_pizza(size, *toppings):
    """
    Summarize the pizza we are about to make
    """
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
```

Now, we will make another file in the same directory as `pizza.py` known as `making_pizza.py`. The file imports the module we just created and then makes two calls to `make_pizza():`

```python
import pizza # pizza is the name of pizza.py

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

When Python reads this file, the line `import pizza ` tells Python to open the file `pizza.py` and copy all the functions from it into this program. The code produces the same output as the original program that did not import a module.

### 2. Importing Specific Functions

We can also import a specific function from a module. The general syntax for this approach is:

`from module_name import function_name`

We can also import as many functions as we want from a module by separating each function's name with a comma:

`from module_name import function_0, function_1, function_2`

For example, if we want to import just the function we would like to use:

```python
from pizza import make_pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### 3. Using as to Give a Function an Alias

If the name of a function we are importing might conflict with an existing name in your program, or if the function name is long, we can use a short, unique alias.

```python
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
```

The general syntax for providing an alias is:

`from module_name import function_name as fn`

### 4. Using as to Give a Module an Alias

We can also provide an alias for a module name. 

Calling `p.make_pizza()` is more concise than calling `pizza.make_pizza()`


```python
import pizza as p # pizza is the name of pizza.py

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

The general syntax for this approach is:

`import module_name as mn`

### 5. Importing all Functions in a Module

We can tell Python to import every function in a module by using the asterisk (*) operator:

```python
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

The asterisk in the import statement tells Python to copy every function from the module pizza into this program file. It is recommended to however, import the necessary function(s) we are going to use to avoid getting unexpected results.

## Styling Functions

1. Functions should have descriptive names, and these names should use lowercase letters and underscores. This will help us and others understand what our code is trying to do.

2. Every function should have a comment that explains concisely what the function does. It should appear immediately after the function definition and use the docstring format.

3. If you specify a default value for a parameter, no spaces should be used on either side of the equal sign: `def function_name(parameter_0, parameter_1='default value')`. The same convention should be used for keyword arguments in function calls: `function_name(value_0, parameter_1='value')`

4. If your program or module has more than one function, you can separate each by two blank lines to make it easier to see where one function ends and the next one begins. 

5. All import statements should be written at the beginning of a file. The only exception is if you use comments at the beginning of your file to describe the overall program.


