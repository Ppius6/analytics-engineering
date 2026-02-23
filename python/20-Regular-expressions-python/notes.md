# Regular Expressions in Python

## Introduction to String manipulation

Strings are a fundamental data type in Python, and they are used to represent text. As a Python developer or data scientist, you will often need to manipulate strings to extract information, clean data, or perform various transformations. Regular expressions (regex) are a powerful tool for working with strings, allowing you to search, match, and manipulate text based on specific patterns.

Python recognizes any sequence of characters as a string, and you can create strings using single quotes (`'...'`), double quotes (`"..."`), or triple quotes (`'''...'''` or `"""..."""`).

Python has built-in functions to handle strings.

We can use the `len()` function to get the length of a string, and we can access individual characters using indexing. For example:

```python

my_string = "Hello, World!"
print(len(my_string))  # Output: 13

```

In the example above, even the space and punctuation are counted as characters, resulting in a length of 13.

We can also use the function `str()` to convert other data types to strings. For example:

```python

number = 42
string_number = str(number)
print(string_number)  # Output: '42'

```

We can concatenate strings using the `+` operator. For example:

```python

greeting = "Hello"
name = "Pius"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)  # Output: 'Hello, Pius!'

```

We can also directly access the position of characters in a string using indexing. For example:

```python

my_string = "Hello, World!"
print(my_string[0])  # Output: 'H'
print(my_string[7])  # Output: 'W'

```

We can also use slicing to access a range of characters in a string. For example:

```python

my_string = "Hello, World!"
print(my_string[0:5])  # Output: 'Hello'
print(my_string[7:12])  # Output: 'World'

```

When slicing strings, the syntax is `string[start:end]`, where `start` is the index of the first character to include, and `end` is the index of the first character to exclude. If you omit `start`, it defaults to 0, and if you omit `end`, it defaults to the length of the string.

Also, the first position is inclusive, while the second position is exclusive. This means that the character at the `start` index is included in the result, but the character at the `end` index is not.

Slide slicing also accepts a third parameter, `step`, which allows you to specify the step size for slicing. The formula is `string[start:end:step]`.

For example:

```python

my_string = "Hello, World!"
print(my_string[0:12:2])  # Output: 'Hlo ol'
print(my_string[1:12:2])  # Output: 'el,Wrd'

```

## String Manipulation Methods

Python provides a variety of built-in string methods that allow you to manipulate and transform strings in different ways. Here are some commonly used string methods:

The `lower()` method converts all characters in a string to lowercase. For example:

```python

my_string = "Hello, World!"
print(my_string.lower())  # Output: 'hello, world!'

```

The `upper()` method converts all characters in a string to uppercase. For example:

```python

my_string = "Hello, World!"
print(my_string.upper())  # Output: 'HELLO, WORLD!'

```

The `capitalize()` method capitalizes the first character of a string and converts the rest to lowercase. For example:

```python

my_string = "hello, world!"
print(my_string.capitalize())  # Output: 'Hello, world!'

```

The `title()` method capitalizes the first character of each word in a string. For example:

```python
my_string = "hello, world!"
print(my_string.title())  # Output: 'Hello, World!'

```

The `strip()` method removes leading and trailing whitespace from a string. For example:

```python

my_string = "   Hello, World!   "
print(my_string.strip())  # Output: 'Hello, World!'

```

The `split()` method splits a string into a list of substrings based on a specified delimiter. For example:

```python

my_string = "Hello, World!"
print(my_string.split(", "))  # Output: ['Hello', 'World!']

```

If `maxsplit` is provided, the string will be split at most `maxsplit` times. For example:

```python
my_string = "Hello, World, Python!"
print(my_string.split(", ", 1))  # Output: ['Hello', 'World, Python!']

```

If we have a string with the escape character `\n`, we can use the `splitlines()` method to split the string into a list of lines. For example:

```python

my_string = "Hello, World!\nWelcome to Python."
print(my_string.splitlines())  # Output: ['Hello, World!', 'Welcome to Python.']

```

We can also concatenate strings using the `join()` method, which takes an iterable of strings and joins them together with a specified separator. For example:

```python

my_list = ['Hello', 'World', 'Python']
separator = ', '
result = separator.join(my_list)
print(result)  # Output: 'Hello, World, Python'

```

When cleaning strings, we can use `strip()`, `lstrip()`, and `rstrip()` methods to remove unwanted characters from the beginning and end of a string. For example:

```python

my_string = "   Hello, World!   "
print(my_string.strip())  # Output: 'Hello, World!'
print(my_string.lstrip())  # Output: 'Hello, World!   '
print(my_string.rstrip())  # Output: '   Hello, World!'

```

The `find()` method helps search a target string for a specified substring and returns the index of the first occurrence. If the substring is not found, it returns -1. For example:

```python
my_string = "Hello, World!"
print(my_string.find("World"))  # Output: 7
print(my_string.find("Python"))  # Output: -1

```

Note that there are two optional arguments, `start` and `end`, which can be used to specify the range of indices to search within the string. For example:

```python

my_string = "Hello, World!"
print(my_string.find("o", 5))  # Output: 8
print(my_string.find("o", 5, 10))  # Output: -1
print(my_string.find("o", 0, 5))  # Output: 4

```

The `replace()` method allows you to replace occurrences of a specified substring with another substring. For example:

```python

my_string = "Hello, World!"
new_string = my_string.replace("World", "Python")
print(new_string)  # Output: 'Hello, Python!'

```

We can also use the `index()` method to find the index of the first occurrence of a specified substring. However, unlike `find()`, if the substring is not found, `index()` raises a `ValueError` instead of returning -1. For example:

```python

my_string = "Hello, World!"
print(my_string.index("World"))  # Output: 7
print(my_string.index("Python"))  # This will raise a ValueError

```

The `count()` method counts the number of occurrences of a specified substring in a string. For example:

```python
my_string = "Hello, World! Hello, Python!"
print(my_string.count("Hello"))  # Output: 2
print(my_string.count("World"))  # Output: 1
print(my_string.count("Python"))  # Output: 1

```