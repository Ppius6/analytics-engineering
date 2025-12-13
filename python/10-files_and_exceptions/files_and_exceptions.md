# Files and Exceptions

Here, we explore `exceptions`, which are special objects Python creates to manage errors that arise while a program is running. We will also explore the `json` module, which allows us to save user data so that it is not lost when your program is running.

Learning to handle exceptions will help us deal with situations in which files do not exists and deal with other problems that can cause programs to crash.

## Reading from a File

A huge amount of data is available in text files. Text files can contain weather data, traffic data, socioeconomic data, literary works, and more. We could write a program that reads in the contents of a text file and rewrites the file with formatting that allows a browser to display it. When we want to work with the information in a text file, the initial step is to read the file into memory. We can then work through all of the file's contents at once or work through the contents line by line.

### Reading the Contents of a File

We could start with a file with a few lines of text in it. For example, a file that contains `pi` to 30 decimal places, with 10 decimal places per line;

To open the file, read it, and print the contents of the file:

```python
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)

Output:
3.1415926535
  8979323846
  2643383279
```

`Path` helps tell Python the path to the file. It is the exact location of a file or folder on a system. Python provides a module called `pathlib` that makes it easier to work with files and directories, no matter which operating system you or your program's users are working with. A module that provides specific functionality like this is often called a `library`, hence the name `pathlib`

`read_text()` is used to read the entire contents of the file. The contents of the file are returned as a single string, which we assign to the variable `contents`. 

We can use `rstrip()` to remove or strip any extra whitespace characters from the right side of a string, or `lstrip()` to the left of a string.

```python
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip() # We use method chaining instead of calling, contents = contents.rstrip() 
print(contents)
```

### Relative and Absolute File Paths

When we pass a simple filename like `pi_digits.txt` to `Path`, Python looks in the directory where the file that is currently being executed is stored. 

To avoid any errors when looking up files, we must provide the correct path to the files, which can be done in two ways:

1. A `relative file path` tells Python to look for a given location relative to the directory where the currently running program file is stored. 

```python
path = Path('practice/pi_digits.txt')
```

2. An `absolute file path` would tell Python where exactly the file is on our computer. If we have put our text files in other folder except the main folder which we are working with, passing the relative file path will not work as Python will only look for that location inside the main folder. So, we need an absolute path to clarify where we want Python to look

```python
path = Path('/home/piusm/dev-projects/analytics-engineering/python/10-files_and_exceptions/practice/pi_digits.txt')
```

### Accessing a File's Lines

While working with a file, we will often want to examine each line of the file. We might be looking for certain information in the file, or may want to modify the text in the file in some way. 

For example, we might want to read through a file of weather data and work with any line that includes the word `sunny` in the description of that day's weather. In a news report, we might look for any line with the tage `<headline>` and rewrite that line with a specific kind of formatting. 

We can use the `splitlines()` method to turn a long string into a set of lines, and then use a for loop to examine each line from a file, one at a time:

```python
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(lines)

Output:
3.1415926535
  8979323846
  2643383279
```

The output is the same as before since we have not modified any of the lines.

### Working with a File's Contents

There's a lot of things you can choose to do with the data. 

First, we can try and build a single string containing all the digits in the file with no whitespace in it:

```python
from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))

Output:
3.1415926535  8979323846  2643383279
36
```

As the file contains whitespace, we could use `lstrip()` to string the left side whitespaces:

```python
from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

Output:
3.141592653589793238462643383279
32
```

### Large Files: One Million Digits

We will pass a file with `pi` in 1,000,000 decimal places.

```python
from pathlib import Path

path = Path("one-million.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

Output:
3.14159265358979323846264338327950288419716939937510...
1000002
```

Python has no inherent limit to how much data you can work with - Just how much data your system can handle.

### Is Your Birthday Contained in Pi?

```python
from pathlib import Path

path = Path("one-million.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the format mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

Output:
Enter your birthday, in the format mmddyy: 100120
Your birthday appears in the first million digits of pi!
```

## Writing to a File

One of the simplest ways to save data is to write it to a file as the output is still available after we close the terminal containing our program's output. 

### Writing a Single Line

We can use `write_text()` method to write to a file once we have a path defined. The method takes a single argument: the string that we want to write to the file.

```python
from pathlib import Path

path = Path('programming.txt')
path.write_text("I love programming.")
```

### Writing Multiple Lines

The `write_text()` method does a few things behind the scenes. If the file that `path` points to does not exists, it creates that file. After writing the string to the file, it makes sure the file is closed properly. 

```python
from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents)
```

The output of the file upon opening it would be:

```
I love programming.
I love creating new games.
I also love working with data.
```

## Exceptions

Python uses special objects called `exceptions` to manage errors that arise during a program's execution. Whenever an error occurs that makes Python unsure of what to do next, it creates an exception object. If we write code that handles the exception, the program will continue running and if not, the program fails and shows a `traceback` which includes a report of the raised exception.

Exceptions are handled with `try-except` blocks. It asks Python to do something, but it also tells Python what to do if an exception is raised. This helps the program to continue running even if things start to go wrong.

### ZeroDivisionError Exception

If we divide a number by zero, Python would raise an error. Besides, it is impossible to divide a number by zero.

```python
print(4/0)

Output:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

The error reported in the traceback, `ZeroDivisionError` is an exception object which Python creates in response to a situation where it cannot do as asked of it.

### Using try-except Blocks

A try-except block would help us handle an exception. For example, if Python would face the error reported above, we can give it further instructions on what to do in such an event

```python
try:
    print(4/0)
except ZeroDivisionError:
    print("You cannot divide by zero!")

Output:
You cannot divide by zero!
```

If the code in the try block would work, Python would skip over the except block. But if it fails, it looks for an excpet block whose error matches the one that was raised, and runs the code in that block. 

In our case, it runs the except block since it is not possible to divide 4 by 0.

### Using Exceptions to Prevent Crashes

Handling errors correctly is important when the program has more work to do after the error occurs, and this happens in programs that prompt users for input. 

Considering the following simple calculator that does only division:

```python
print("Give me two numbers, and I will divide them.")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

Output:
First number: 2

Second number: 0
Traceback (most recent call last):
  File "<stdin>", line 8, in <module>
ZeroDivisionError: division by zero
>>> 
```

In the above program, in case it encounters any error, such as dividing by zero, it would crash.

### The else Block

To make the program more error resistant, we can wrap the line that might produce error in a `try-except` block. 

```python
print("Give me two numbers, and I will divide them.")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by 0!")
    else:
        print(answer)

Output:

First number: 2

Second number: 0
You cannot divide by 0!

First number: q
```

### Hnalding the FileNotFoundError Exeption

A common issue when working with files is handling missing files. We can handle such situations using a `try-except` block, too.

```python
from pathlib import Path

path = Path('alice.txt')
contents = path.read_text(encoding='utf-8')
```

The `encoding` argument is needed when the system's default encoding does not match the encoding of the file that is being read. For instance, it is more likely to happen when reading from a file that was not created on our system. 

Python cannot read from a missing file, so it raises an exception:

```python
>>> contents = path.read_text(encoding='utf-8')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.12/pathlib.py", line 1029, in read_text
    with self.open(mode='r', encoding=encoding, errors=errors) as f:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/pathlib.py", line 1015, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
```
Here, we get a `FileNotFoundError` which is useful in understanding what kind of exception to use in the `except` block that we will write.

Looking back, we see which line and specific line of code that caused the error. The rest of the traceback shows some code from the libraries that are involved in opening and reading from files. 

To handle the error that is being raised, the `try` block will begin with the line that was identified as problematic in the traceback. 

```python
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")

Output:
... 
Sorry, the file alice.txt does not exist.
>>> 
```

### Analyzing Text

We can analyze text files containing entire books. 

For example, we can pull in the text of `Alice in Wonderland` and try to count the number of words in the text. To do this, we will use the string method `split()` which by default splits a string wherever it finds any whitespace:

```python
from pathlib import Path

path = Path('Alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")

Output:
The file alice.txt has about 29594 words.
```

### Working with Multiple Files

When working with multiple files, we can move the bulk of our program to a function called `count_words()` for example, which makes it easier to run the analysis.

```python
from pathlib import Path

def count_words(path):
    """
    Count the approximate number of words in a file.
    """
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddharta.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    path = Path(filename)
    count_words(path)

Output:

The file alice.txt has about 29594 words.
Sorry, the file siddharta.txt does not exist.
The file moby_dick.txt has about 215864 words.
The file little_women.txt has about 189142 words.
```

In the program above, the names of the files are stored as simple strings. Each string is then converted to a `Path` object, before the call to `count_words()`. 

If the file is unavailable, we let the user know that the file does not exist using the `try-except` block without the program failing. 

### Failing Silently

To make a program fail silently, we can write a try block as usual, but we can explicitly tell Python to do nothing in the except block. Python has a `pass` statement that tells it to do nothing in a block:

```python
def count_words(path):
    """
    Count the approximate number of words in a file
    """
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
```

The only difference between falling silently and the previous code returning a statement is that when a `FileNotFoundError` is raised, the code in the `except` block runs, but nothing happens. No traceback is produced, and there is no output in response to the error that was raised. 

For instance, the output would be:

```
The file alice.txt has about 29594 words.
The file moby_dick.txt has about 215864 words.
The file little_women.txt has about 189142 words.
```

The pass statement can also act as a placeholder. It is a reminder that we are choosing to do nothing at a specific point in our program's execution and that we might want to do something there later.

### Deciding which Errors to Report

1. If users know which texts are supposed to be analyzed, they might appreciate a message informing them why some texts were not analyzed. 

2. If users expect to see some results but do not know which books are supposed to be analyzed, they might not need to know that some texts were unavailable.

## Storing Data

Most times, we will need to store data, mostly what the users provide in data structures such as lists and dictionaries. When users close a program, we will almost always want to save the information they entered. A simple way to do this involves storing the data using the `json` module. 

The `json` module allows us to conver simple Python data structures into JSON-formatted strings, and then load the data from that file the next time the program runs. We can also use `json` to share data between different Python programs. Even better, the JSON data format is not specific to Python, so we can share data we store in the JSON format wioth other people working with other programming languages. 

### Using `json.dumps()` and `json.loads()`

We can write a short program that stores a set of numbers and another program that reads these numbers back into memory. The first program will use `json.dumps()` to store the set of numbers, and the second program will use `json.loads()`.

The `json.dumps()` function takes one argument: a piece of data that should be converted to the JSON format. The function returns a string, which we can then write to a data file:

```python
from pathlib import Path
import json

numbers = [2, 3, 4, 5, 6, 11, 333]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)
```

Here, we first import the `json` module, and then create a list of numbers to work with. Then we choose a filename in which to store the list of numbers. It is customary to use the file extension `.json` to indicate that the data in the file is stored in the JSON format. 

Next, we use the `json.dumps()` function to generate a string containing the JSON representation of the data we are working with. Once we have this string, we write it to the file using the same `write_text()` method we used earlier.

The program would output our file `numbers.json` with the numbers we specified.

Now, we can use `json.loads()` to read the list back into memory:

```python
from pathlib import Path
import json

numbers = [2, 3, 4, 5, 6, 11, 333]

path = Path('numbers.json')
contents = path.read_text()

numbers = json.loads(contents)

print(numbers)
```

### Saving and Reading User-Generated Data

We can begin with storing the user's name:

```python
from pathlib import Path
import json

username = input("What is your name? ")

path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"We will remember you when you come back, {username}!")

Output:
What is your name? Pius
We will remember you when you come back, Pius!
```

Now, let us write a new program that greets a user whose name has already been stored:

```python
from pathlib import Path
import json

path = Path('username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")

Output:
Welcome back, Pius!
```

We can combine the above two programs into one file. We want to retrieve the user's username from memory if possible; if not, we will prompt for a username and store it in `username.json` for next time. We could write a `try-except` block here to respond appropriately if `username.json` does not exist, but instead we will use a handy method from the `pathlib` module:

```python
from pathlib import Path
import json

path = Path('username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")

    path = Path('username.json')
    contents = json.dumps(username)
    path.write_text(contents)

    print(f"We will remember you when you come back, {username}!")

Output:
What is your name? Pius
We will remember you when you come back, Pius!
```

The `exists()` method returns True if a file or folder exists and False if it does not. Here, we use `path.exists()` to find out if a username has already been stored. If it exists, we load the username and print a personalized greeting to the user.

If the file does not exist, we prompt for a username and store the value that the user enters. We also print the familiar message that we will remember them when they come back.

### Refactoring

`Refactoring` involves breaking up our code into a series of functions that have specific jobs, which is when we recognize that we can improve the code. 

It makes our code cleaner, easier to understand, and easier to expand.

For example:

```python
from pathlib import Path
import json

def greet_user():
    """
    Greet the user by name.
    """
    path = Path('username.json')

    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        path = Path('username.json')
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We will remember you when you come back, {username}!")

greet_user()
```

We can further refactor the code, so that it is not doing so many different tasks, for example, by moving the code for retrieving a stored username to a separate function:

```python
from pathlib import Path
import json

def get_stored_username(path):
    """
    Get stored username if available
    """
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def greet_user():
    """
    Greet the user by name.
    """
    path = Path('username.json')

    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        path = Path('username.json')
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We will remember you when you come back, {username}!")

greet_user()
```

Our new function `get_stored_username` retrieves a stored username and returns the username if it finds one. If it does not exist, the function returns `None`, a good practice as a function should either return the value we are expecting or it should return `None`.

We should factor one more block of code out of `greet_user()`, such that if the username does not exist, we should move the coe that prompts for a new username to a function dedicated to that purpose:

```python
from pathlib import Path
import json

def get_stored_username(path):
    """
    Get stored username if available
    """
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """
    Prompt for a new username
    """
    username = input("What is your name? ")
    path = Path('username.json')
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """
    Greet the user by name.
    """
    path = Path('username.json')

    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We will remember you when you come back, {username}!")

greet_user()
```