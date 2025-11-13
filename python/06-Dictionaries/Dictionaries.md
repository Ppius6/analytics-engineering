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