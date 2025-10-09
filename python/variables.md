# Variables and Simple Data Types

## Variables

Variables are used to store data that can be referenced and manipulated in a program. In Python, you can create a variable by simply assigning a value to it using the equals sign (`=`).

```python
message = "Hello, Python world!"
print(message)
```

### Naming and usage conventions
There are some rules and guidelines to be adhered tpo when using variables in Python:

- Variable names can contain only letters, numbers, and underscores (`_`). They can start with a letter or an underscore, but not with a number. An example of a valid variable name is `my_variable1` but not `1st_variable`.
- Spaces are not allowed in variable names, but underscores can be used to separate words (e.g., `my_variable`).
- Avoid using Python keywords and function names as variable names.
- Variable names should be short but descriptive. An example is `age` instead of `a`, `name` instead of `n`, and `total_price` instead of `tp`.
- Be careful when using the lowercase letter `l`, uppercase letter `O`, and the number `0` in variable names, as they can be easily confused with each other.

### Avoiding name errors when using variables

```python
message = "Hello, Python world!"
print(mesage)
```

In the code above, there is a typo in the variable name `mesage`, which will result in an error. However, the interpretor provides a traceback when a program cannot run successfully. A `traceback` is a record of where the interpretor ran into trouble when trying to execute your code.

```
Traceback (most recent call last):
    File "script.py", line 2, in <module>
        print(mesage)
NameError: name 'mesage' is not defined
```
The output indicates that the error occurred on line 2 of the script, and it specifies that the name `mesage` is not defined. This helps you identify and fix the typo in the variable name.

### Variables are labels

Variables are often described as boxes you can store values in. However, a more accurate description is that variables are labels that refer to values stored in memory. When you assign a value to a variable, you are creating a label that points to that value.

```python
message = "Hello, Python world!"
print(message)
```

In the code above, the variable `message` is a label that refers to the string value `"Hello, Python world!"`. When you print the variable, Python looks up the label and retrieves the value it points to.

Variables can be reassigned to refer to different values. For example:

```python
message = "Hello, Python world!"
print(message)
message = "Hello, Universe!"
print(message)
```

In the above program, the variable `message` is first assigned to the string `"Hello, Python world!"`. Later, it is reassigned to the string `"Hello, Universe!"`. When you print the variable after each assignment, it outputs the current value it refers to.

## Strings

A string is a sequence of characters. Anything inside quotes is considered a string in Python, and you can use either single quotes (`'`) or double quotes (`"`).

```python
"This is a string."
'This is also a string.'
```

This flexibility allows us to use quotes and apostrophes within strings.

```python
'I told my friend, "Python is my favorite programming language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
"I come from a village known as 'Mworoga'."
```

### Changing Case in a String with Methods

You can change the case of a string using methods. 

A `method` is an action that Python can perform on a piece of data.

In the example, 

```
name = "ada lovelace"
print(name.title())
```
the `title()` method is called on the string stored in the variable `name`. So the dot (`.`) after `name` tells Python to make the `title()` method act on the variable `name`.

Every method is usually followed by a set of parentheses, because methods often need additional information to do their work and this information is provided inside the parentheses. In the case of `title()`, no additional information is needed, so the parentheses are empty.

The `title()` method converts the first character of each word to uppercase and the rest to lowercase. The output of the code above will be:

```
Ada Lovelace
``` 

### Using variables in Strings

In some situations, you may want to use a variable's value inside a string. 

For example, you might want to use two variables to represent a first name and a last name, and then combine those values to display a full name.

```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
```

To insert a variable's value into a string, place the letter `f` before the opening quotation mark of the string. Then, include the variable name inside curly braces (`{}`) wherever you want the variable's value to appear in the string.

These strings are called `f-strings`, which stands for formatted string literals. 

The `f` is for `format`, because Python formars the string by replacing the name of any variable in curly braces with its value.

The output of the code above will be:

```
Ada Lovelace
```

Other uses of f-strings:

```python
first_name = "pius"
last_name = "mutuma"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
```

In the code above, the full name is used in a sentence that greets the user, and the title() method changes the name to title case.

```
Hello, Pius Mutuma!
```

The same result can be achieved by storing the greeting message in a variable before printing it:

```python
first_name = "pius"
last_name = "mutuma"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)
```

### Adding Whitespace to Strings with Tabs or Newlines

Whitespace refers to any non-printing character, such as spaces, tabs, and newlines.

Whitespace is often used to format text to make it more readable.

You can add whitespace to strings using special characters called escape characters. An escape character is a backslash (`\`) followed by the character you want to insert.

For example, to add a tab to a string, you can use the escape character `\t`:

```python
print("Python")
print("\tPython")
```

To add a newline to a string, we use the character combination `\n`:

```python
print("Languages:\nPython\nC\nJavaScript")
```
The output of the code above will be:

```
Languages:
Python
C
JavaScript
```

### Stripping Whitespace

Sometimes, you may want to remove whitespace from the beginning or end of a string. You can do this using the `strip()` method. However, we can also use `lstrip()` and `rstrip()` methods to remove whitespace from the left or right side of a string, respectively.

```python
favorite_language = "   python   "
print(favorite_language.strip())
print(favorite_language.lstrip())
print(favorite_language.rstrip())
```

The output of the code above will be:

```
python
   python
python   
```

### Removing Prefixes

While working with strings, we may want to remove a prefix from a string. An example is when working with URLs, where we may want to remove the `https://` or `http://` prefix.

You can use the `removeprefix()` method to remove a specified prefix from a string. If the string starts with the specified prefix, it will be removed; otherwise, the string will remain unchanged.

```python
url = "https://www.example.com"
cleaned_url = url.removeprefix("https://")
print(cleaned_url)
```
The output of the code above will be:

```
www.example.com
```



