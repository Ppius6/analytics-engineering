from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()
print(contents)

# Accessing a file's lines

path = Path("pi_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(lines)

# Files manipulation
# Reading the file and storing its contents in a string
from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

# Reading a file with 1 million digits of pi
from pathlib import Path

path = Path("one-million.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

# Is your birthday in pi?
from pathlib import Path

path = Path("one-million.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the format mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# Reading and printing the text two times; print the contents once by reading in the entire file, and once by storing the lines in a list and then looping over each line
from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()

# Method 1
print("Method 1 - Reading entire file:")
print(contents)

# Method 2: Store lines in a list and loop through them
print("\nMethod 2 - Looping through lines:")
for line in contents.splitlines():
    print(contents)

# Learning C: Use the replace method to replace any word in a string with a different word

from pathlib import Path

path = Path("python/10-files_and_exceptions/practice/learning_python.txt")
contents = path.read_text()

contents.replace("Python", "Ruby")


# 10.6 - Addition

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

try:
    sum = int(num1) + int(num2)
    print(f"The sum of {num1} and {num2} is {sum}.")
except ValueError:
    print("One of the inputs was not a valid number. Please enter numeric values only.")

# 10.7 - Addition Calculator
# Wrapping the code in a while loop to allow multiple calculations

while True:
    num1 = input("Enter a number (or 'q' to quit): ")
    if num1.lower() == "q":
        break

    num2 = input("Enter another number (or 'q' to quit): ")
    if num2.lower() == "q":
        break

    try:
        sum = int(num1) + int(num2)
        print(f"The sum of {num1} and {num2} is {sum}.")
    except ValueError:
        print(
            "One of the inputs was not a valid number. Please enter numeric values only."
        )
