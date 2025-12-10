## Comments (Random maneno in a code, you know...)

Programming can get complex at times as the size of the code becomes longer and more complicated. Comments (notes) can be added within the programs to describe what the code does, making it easier to understand. Comments are ignored by Python when running the program, so they do not affect the program's behavior.

Comments in Python start with a `#` symbol. Everything after the `#` on that line is considered a comment and is not executed by Python. For example:

```python
# This is a comment
print("Hello, World!")  # This prints a message to the console
```

You can also use comments to explain specific parts of your code:

```python
# This function adds two numbers
def add_numbers(a, b):
    return a + b  # Return the sum of a and b
result = add_numbers(5, 3)  # Call the function with arguments 5 and 3
print(result)  # Output: 8
```