# Dictionaries

Here, we will explore how to use Python's dictionaries, which allow us to connect pieces of related information. We will also learn how to access the complex nested data in dictionaries, loop through them, and modify their contents.

This is useful when seeking to model a variety of real-world objects more accurately. We will be able to create a dictionary representing a person and then store as much information as we want about that person. 

## Creating a Dictionary

Consider storing information about a country. We can use a dictionary to hold various attributes of the country:

```python
country = {"name": "Kenya", "population": 53771296, "capital": "Nairobi"}

print(country) # Output: {'name': 'Kenya', 'population': 53771296, 'capital': 'Nairobi'}
```

We can access individual values using their keys:

```python
print(country["name"]) # Output: Kenya
print(country["population"]) # Output: 53771296
print(country["capital"]) # Output: Nairobi
```

## Working with Dictionaries

A `dictionary` in Python is a collection of `key-value pairs`. Each `key` is connected to a `value`, and you can use the key to access the corresponding value.

The value can be a number, string, list, or even another dictionary.

In the example before, the keys are `"name"`, `"population"`, and `"capital"`, while the values are `"Kenya"`, `53771296`, and `"Nairobi"` respectively.

A `key-value pair` is written as `key: value`, and is a set of values associated with each other. When we provide a key, Python returns the corresponding value. 

Every key is connected to its value by a colon `:`. Multiple key-value pairs are separated by commas `,` and the entire dictionary is enclosed in curly braces `{}`.

The simplest version of a dictionary has just one key-value pair:

```python
single_pair_dict = {"key": "value"}

print(single_pair_dict) # Output: {'key': 'value'}
```

### Accesing Values in a Dictionary

When we want to access a value associated with a specific key in a dictionary, we give the name of the dictionary followed by the key in square brackets `[]`.

```python
country = {"name": "Kenya", "population": 53771296, "capital": "Nairobi"}

print(country["name"]) # Output: Kenya
print(country["population"]) # Output: 53771296
print(country["capital"]) # Output: Nairobi
```

`Kenya` is the value associated with the key `"name"`, `53771296` is the value for the key `"population"`, and `"Nairobi"` is the value for the key `"capital"`.

We can expand to use statements that utilize these values:

```python
country = {"name": "Kenya", "population": 53771296, "capital": "Nairobi"}
population = country["population"]
print(f"The population of {country['name']} is {population}.")

# Output: The population of Kenya is 53771296.
```

### Adding New Key-Value Pairs

Dictionaries are dynamic structures and you can add new key-value pairs to them at any time. To add a new key-value pair, we can give the name of the dictionary followed by the new key in square brackets `[]`, and assign it a value using the assignment operator `=`.

```python
country = {"name": "Kenya", "population": 53771296, "capital": "Nairobi"}
country["currency"] = "Kenyan Shilling"
country["activity"] = "Agriculture"
print(country) # Output: {'name': 'Kenya', 'population': 53771296, 'capital': 'Nairobi', 'currency': 'Kenyan Shilling', 'activity': 'Agriculture'}
```

Dictionaries will always retain the order in which they were defined. When we print a dictionary or loop through its elements, we will see the elements in the same order they were added to the dictionary.

### Starting with an Empty Dictionary

We can also begin with an empty dictionary and seek to add new items in our dictionary. First, we define a dictionary with an empty set of braces and add each key-value pair on its own line. 

```python
countries = {}
countries["name"] = "Kenya"
countries["currency"] = "KES"

print(countries) # Output: {'name': 'Kenya', 'currency': 'KES'}
```

We would mostly use empty dictionaries when storing user-supplied dara in a dictionary or when writing code that generates a large number of key-value pairs automatically.

### Modifying Values in a Dictionary

To modify a value in a dictionary, we give the name of the dictionary with the key in square brackets and then the new value you want associated with that key. For example, we may want to change the country from `Kenya` to `Rwanda` and currency from `KES` to `Franc`.

```python
country = {"name": "Kenya", "currency": "KES"}
print(f"The currency for {country["name"]} is {country["currency"]}")
# Output: The currency for Kenya is KES

country["name"] = "Rwanda"
country["currency"] = "Franc"
print(f"The currency for {country["name"]} is {country["currency"]}")
# Output: The currency for Rwanda is Franc
```

Building a more interesting example, we can track the position of an alien that can move at different speeds. We will store a value representing the alien's current speed and then use it to determine how far to the right the alien should move:

```python
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# First, move the alien to the right
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")
```

In the above example, since the `speed` is `medium`, the `x_position` is incremented by 2.

### Removing Key-Value Pairs

When you no longer need a piece of information that is stored in a dictionary, you can use the `del` statement to completely remove a key-value pair. 

All `del` needs is the name of the dictionary and the key that you want to remove. 

To remove the key `currency` from the country dictionary, along with its value:

```python
country = {"name": "Kenya", "currency": "KES"}
print(country) # Output: {'name': 'Kenya', 'currency': 'KES'}

del country["currency"]
print(country) # Output: {'name': 'Kenya'}
```

### A Dictionary of Similar Objects

Dictionaries are useful for storing information about many similar objects. For example, we can create a dictionary to store information about multiple countries:

```python
countries = {
    "Kenya": "Nairobi",
    "Uganda": "Kampala",
    "Tanzania": "Dodoma",
    "Rwanda": "Kigali"
}
print(countries)
# Output: {'Kenya': 'Nairobi', 'Uganda': 'Kampala', 'Tanzania': 'Dodoma', 'Rwanda': 'Kigali'}

print(f"The capital of Uganda is {countries['Uganda']}.") 
# Output: The capital of Uganda is Kampala
```

### Using get() to Access Values

Using keys in square brackets to retrieve the value you are interested in from a dictionary might cause a potential problem if the key we ask for does not exist. This will raise a `KeyError` and stop the program from running.

The `get()` method allows us to provide a default value to return if the requested key does not exist, preventing a `KeyError`.

```python
country = {"name": "Kenya", "population": 53771296}
capital = country.get("capital", "Capital not found")
print(capital) # Output: Capital not found
```

## Looping Through a Dictionary

A single Python dictionary can contain just a few key-value pairs or millions of pairs. Since the amounts of data can be large, Python lets us loop through the dictionary to access each key-value pair.

### Looping Through All Key-Value Pairs

Let us explore the example of a dictionary designed to store information about a user on a website. The dictionary below would store one person's username, first name, and last name:

```python
user_0 = {
    "username": "john_doe",
    "first_name": "John",
    "last_name": "Doe"
}
```

We can use a `for` loop to iterate through the dictionary and print each key-value pair:

```python
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```
This will output:

```
Key: username
Value: john_doe
Key: first_name
Value: John
Key: last_name
Value: Doe
```

To write a for loop for a dictionary, we create names for the two variables that will hold the key and value in each key-value pair: `for key, value in dictionary.items():` or even `for k, v in dictionary.items():`.

The next part of the loop utilzes the `.items()` method, which returns a sequence of key-value pairs. The for loop then assigns each of these pairs to the two variables we defined earlier, allowing us to access both the key and value in each iteration.

### Looping Through All the Keys in a Dictionary

The `keys()` method is useful when we do not need to work with all the values in a dictionary. For example, we can loop through the keys in the `user_0` dictionary:

```python
for key in user_0.keys():
    print(key)
```
This will output:

```
username
first_name
last_name
```

Looping through the keys is actually the default behavior when looping through a dictionary. This code will produce the same result as above:

```python
for key in user_0:
    print(key)
```

In example below, we will print a message to a couple of friends about the languages they speak. We will loop through the keys in the `favorite_languages` dictionary and print a message to each person:

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title() # Accessing the value using the key
        print(f"\t{name.title()}, I see you love {language}!")
```

In the above example, we make a list of friends that we want to print a message to. Inside the loop, we print each person's name. Then, we check whether the name we are working with is in the list friends. If it is, we determine the person's favorite language using the name of the dictionary and the current value of name as the key. We then print a special greeting, including a reference to their language of choice. 

We can also use the `keys()` method to check whether a particular person took the poll:

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
# Output: Erin, please take our poll!
```

### Looping Through a Dictionary's Keys in a Particular Order

Looping through a dictionary returns the items in the same order they were inserted. We may want to loop through a dictionary in a different order. 

A way to do this is to sort the keys as they are returned in the for loop. We can use the `sorted()` function to get a copy of the keys in order:

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(fovorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
```

The above tells Python to get all the keys in the dictionary and sort them before starting the loop. The output will be:

```
Edward, thank you for taking the poll.
Jen, thank you for taking the poll.
Phil, thank you for taking the poll.
Sarah, thank you for taking the poll.
```

### Looping Through All Values in a Dictionary

If we are only interested in the values that a dictionary contains, we can use the `values()` method to return a list of values without their keys. For example, we can loop through all the values in the `favorite_languages` dictionary:

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for language in favorite_languages.values():
    print(language.title())

# Output:
Python
C
Ruby
Python
```

The for statement here pulls each value from the dictionary and assigns it to the variable `language`, which we then print.

However, it pulls all the values from the dictionary without checking for repeats. If we want to see each language chosen only once, we can use a `set`, which is an unordered collection of unique elements:

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for language in set(favorite_languages.values()):
    print(language.title())

# Output:
Python
C
Ruby
```

Here, the `set()` function takes the list of values returned by the `values()` method and removes any duplicates, so each language is printed only once.

## Nesting 

We may want to store multiple dictionaries in a list, or a list of items as a value in a dictionary. This is called `nesting` which allows us to nest dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary.

### A List of Dictionaries

Sometimes we may want to store a collection of similar objects. For example, we can store multiple items, each representing a country, in a list:

```python
country_1 = {"name": "Kenya", "population": 53771296, "capital": "Nairobi"}
country_2 = {"name": "Uganda", "population": 45741000, "capital": "Kampala"}
country_3 = {"name": "Tanzania", "population": 59734218, "capital": "Dodoma"}
countries = [country_1, country_2, country_3]
for country in countries:
    print(country)
```

This will output:

```
{'name': 'Kenya', 'population': 53771296, 'capital': 'Nairobi'}
{'name': 'Uganda', 'population': 45741000, 'capital': 'Kampala'}
{'name': 'Tanzania', 'population': 59734218, 'capital': 'Dodoma'}
```

We can create a list of aliens with a code that automatically generates each alien.

```python
aliens = []

for alien_num in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")  # Indicate that there are more aliens

# Output:
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
...
```

We can configure the points of our aliens;


```python
aliens = []

for alien_n in range(30):
    new_alien = {'color': 'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)

# Output:
# {'color': 'yellow', 'points': 10, 'speed': 'medium'}
# {'color': 'yellow', 'points': 10, 'speed': 'medium'}
# {'color': 'yellow', 'points': 10, 'speed': 'medium'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
```

### A List in a Dictionary

Instead of putting a dictionary inside a list, it is sometimes useful to put a list inside a dictionary. 

In the example velow, two kinds of information are stored for eacg pizza: a type of crust and a list of toppings. The list of toppings is a value associated with the key toppings. To use the items in the list, we give the name of the dictionary and the key toppings, as we would any value in the dictionary. Instead of returning a single value, we get a list of toppings.

```python
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings: ")

for topping in pizza['toppings']:
    print(f"\t{topping}")

# Output:
You ordered a thick-crust pizza with the following toppings:
        mushrooms
        extra cheese
```

We can always nest a list inside a dictionary anytime we want more than one value to be associated with a single key in a dictionary. In our programming example, we can store each person's responses in a list allowing them to choose more than one favorite language.

```python
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
```

The value associated with each name in favorite_languages is now a list. Note that some people have one favorite language and others have multiple favorites. When we loop through the dictionary, we use the variable name languages to hold each value from the dictionary, because we know that each value will be a list. Inside the main dictionary loop, we use another for loop to run through each person's list of favorite languages. Now each person can list as many favorite languages as they like. 

```
# Output:
Jen's favorite languages are:
        Python
        Rust

Sarah's favorite languages are:
        C

Edward's favorite languages are:
        Rust
        Go

Phil's favorite languages are:
        Python
        Haskell
```

We could refine it further, to include an if statement at the beginning of the dictionary's for loop to see whether each person has more than one favorite language by examining the value of len(languages). If a person has more than one favorite, the output would stay the same. If the person has only one favorite language, we could change the wording to reflect that. For example, we could say, "Sarah's favorite language is C."

### A Dictionary in a Dictionary

We can nest a dictionary inside another dictionary, but the code can get complicated quickly. For example, if we have several users for a website, each with a unique username, we can use the usernames as the keys in a dictionary. We can then store information about each user by using a dictionary as the value associated with their username. 

In the following listing, we store three pieces of information about each user: their first name, last name, and location. We will then access this information by looping through the usernames and dictionary of information associated with each username:

```python
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
```

Here, we first define a dictionary called `users` that contains two users. Each username is a key in the `users` dictionary, and the value associated with each username is another dictionary that holds the user's first name, last name, and location.

When we loop through the `users` dictionary, we use two variables: `username` to hold the key (the username) and `user_info` to hold the value (the nested dictionary). Inside the loop, we access the first name, last name, and location from the `user_info` dictionary and print them in a formatted way.

When accessing the inner dictionary, the variable user_info which contains the dictionary of user information, has three keys: 'first', 'last', and 'location'. We use these keys to get the corresponding values for each user.

# Output:
```
Username: aeinstein
    Full name: Albert Einstein
    Location: Princeton

Username: mcurie
    Full name: Marie Curie
    Location: Paris
```

