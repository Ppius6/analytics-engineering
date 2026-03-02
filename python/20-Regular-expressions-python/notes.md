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

## Formatting Strings

Python provides several ways to format strings, allowing you to create dynamic and customized output. The common formatting methods include:

- Positional formatting using the `format()` method

- f-strings (formatted string literals)

- Template strings from the `string` module

### Positional Formatting with `format()`

Here, we place placeholders in the string using curly braces `{}` and then call the `format()` method to fill in those placeholders with values in the format `text{}.format(value)`.

For example:

```python

print("Hello, {}!".format("Pius"))  # Output: 'Hello, Pius!'

```

You can also use multiple placeholders and specify the order of values using indices. We can chose to specify the index of the values for the case of even reordering them oor just specify the values in the order they appear in the string.

For example:

```python

print("Hello, {0}!, Welcome to {1}".format("Pius", "Python"))  # Output: 'Hello, Pius!, Welcome to Python'

```

#### Named placeholders

Here, we can use named placeholders in the string and pass the values as keyword arguments to the `format()` method. For example:

```python

tool = "Python"
name = "Pius"

print("Hello, {name}!, Welcome to {tool}".format(name=name, tool=tool))  # Output: 'Hello, Pius!, Welcome to Python'

```

For cases where we have dictionaries, we can use the following style:

```python

my_dict = {"name": "Pius", "tool": "Python"}
print('Hello, {data[name]}!, Welcome to {data[tool]}'.format(data=my_dict))  # Output: 'Hello, Pius!, Welcome to Python'

```

#### Format specifiers

Format specifiers allow you to control the formatting of values in the output string. They are specified after a colon `:` within the placeholder. We specify the data type to be used: `{index:specifier}`.

For example:

```python
print("The value of pi is approximately {:.2f}".format(3.14159))  # Output: 'The value of pi is approximately 3.14'

print("Only {1} of the students out of a total of {0} passed the exam.".format(100, 85))  # Output: 'Only 85 of the students out of a total of 100 passed the exam.'
```

When formatting datetime, we can use the `datetime` module to format date and time values. For example:

```python
from datetime import datetime
print("Current date and time: {:%Y-%m-%d %H:%M:%S}".format(datetime.now()))  # Output: 'Current date and time: 2024-06-01 12:34:56'

```

### f-strings (Formatted String Literals)

f-strings, introduced in Python 3.6, provide a more concise and readable way to format strings. They are defined by prefixing the string with the letter `f` or `F` and using curly braces `{}` to embed expressions directly within the string.

For example:

```python

name = "Pius"
tool = "Python"
print(f"Hello, {name}!, Welcome to {tool}")  # Output: 'Hello, Pius!, Welcome to Python'

```

There are several allowed conversions for f-strings, including:

- `!s`: Converts the value to a string using `str()`
- `!r`: Converts the value to a string using `repr()`
- `!a`: Converts the value to a string using `ascii()`

For example:

```python

value = "Hello, World!"
print(f"Using str(): {value!s}")  # Output: 'Using str(): Hello, World!'
print(f"Using repr(): {value!r}")  # Output: 'Using repr(): 'Hello, World!''
print(f"Using ascii(): {value!a}")  # Output: 'Using ascii(): 'Hello, World!''

```

We have several format specifiers for f-strings as well, which are similar to those used with the `format()` method. They include:

- `e`: Exponential scientific notation, i.e., 1.23e+02
- `d`: Digit, i.e., 123
- `f`: Floating-point decimal format, i.e., 123.45
- `s`: String format, i.e., 'Hello'
- `x`: Hexadecimal format, i.e., 0x7b
- `b`: Binary format, i.e., 0b1111011
- `o`: Octal format, i.e., 0o173
- `c`: Character format, i.e., 'A' for 65

```python

from datetime import datetime
my_today = datetime.now()

print(f"Current date and time: {my_today:%Y-%m-%d %H:%M:%S}")  # Output: 'Current date and time: 2024-06-01 12:34:56'

```

#### Index lookups

```python

family = {"dad": "John", "mom": "Jane", "child": "Pius"}

print("Hello, {family['child']}!, Welcome to Python".format(family=family))  # Output: 'Hello, Pius!, Welcome to Python'

```

or

```python

family = {"dad": "John", "mom": "Jane", "child": "Pius"}
print(f"Hello, {family['child']}!, Welcome to Python")  # Output: 'Hello, Pius!, Welcome to Python'

```

### Template Strings

The `string` module provides a `Template` class that allows you to create template strings with placeholders. You can use the `substitute()` method to replace the placeholders with actual values. For example:

```python

from string import Template
template = Template("Hello, $name!, Welcome to $tool")
result = template.substitute(name="Pius", tool="Python")
print(result)  # Output: 'Hello, Pius!, Welcome to Python'

```

We can i.e., add `$$` to include a literal dollar sign in the output. For example:

```python

from string import Template
template = Template("The price is $$ $price")
result = template.substitute(price=10)
print(result)  # Output: 'The price is $10'

```

The `Template` class also provides a `safe_substitute()` method, which works similarly to `substitute()`, but instead of raising a `KeyError` when a placeholder is missing, it leaves the placeholder unchanged in the output. For example:

```python

from string import Template

template = Template("Hello, $name!, Welcome to $tool")
result = template.safe_substitute(name="Pius")
print(result)  # Output: 'Hello, Pius!, Welcome to $tool'

```

`str.format()` are good to start with in most cases, but f-strings are generally more concise and easier to read, especially when embedding expressions directly within the string. Template strings can be useful when you want to create templates that can be reused with different values, but they are less commonly used than the other two methods.

## Regular Expressions

A REGular EXpression (regex) is a string containing a combination of normal characters and special meta-characters that describes patterns to find text or positions within a text. Regular expressions are used for searching, matching, and manipulating strings based on specific patterns.

In `r'st\d\s\w{3, 10}`,

- `r` indicates that the string is a raw string, which means that backslashes are treated as literal characters and not as escape characters.
- `st` matches the literal characters "st".
- `\d` matches any digit (0-9).
- `\s` matches any whitespace character (space, tab, newline).
- `\w{3, 10}` matches any word character (alphanumeric or underscore) that occurs between 3 and 10 times.

The `re` module in Python provides functions for working with regular expressions. 

To find all matches of a pattern in a string, we can use the `re.findall()` function: `re.findall(pattern, string)`. This function returns a list of all non-overlapping matches of the pattern in the string. For example:

```python
import re

re.findall(r'\d+', 'The price is 100 dollars and 50 cents.')  # Output: ['100', '50']

re.split(r"!", "Hello! How are you?")  # Output: ['Hello', ' How are you?']

re.sub(r'\s+', ' ', 'This   is   a   test.')  # Output: 'This is a test.'

```

Quantifiers in regular expressions specify how many times a character or group should be matched. Some common quantifiers include:

- `*`: Matches 0 or more occurrences of the preceding element.
- `+`: Matches 1 or more occurrences of the preceding element.
- `?`: Matches 0 or 1 occurrence of the preceding element.
- `{n}`: Matches exactly n occurrences of the preceding element.
- `{n,}`: Matches n or more occurrences of the preceding element.
- `{n,m}`: Matches between n and m occurrences of the preceding element.

For example:

```python

import re

re.findall(r'\d*', 'The price is 100 dollars and 50 cents.')  # Output: ['', '', '', '', '', '', '100', '', '', '', '', '50', '', '', '', '', '']

re.findall(r'\d+', 'The price is 100 dollars and 50 cents.')  # Output: ['100', '50']

re.findall(r'\d?', 'The price is 100 dollars and 50 cents.')  # Output: ['', '', '', '', '', '', '1', '0', '0', '', '', '', '5', '0', '', '', '', '', '']

re.findall(r'\d{3}', 'The price is 100 dollars and 50 cents.')  # Output: ['100']

re.findall(r'\d{2,}', 'The price is 100 dollars and 50 cents.')  # Output: ['100', '50']

re.findall(r'\d{1,3}', 'The price is 100 dollars and 50 cents.')  # Output: ['100', '50']

```

