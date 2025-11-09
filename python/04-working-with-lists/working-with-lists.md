## Working with Lists

We may want to perform operations on multiple items at once. For example, you may want to display a list of the countries you have visited separately. When you want to do the same action with every item in a list, you can use Python's `for` loop.

```python
countries = ['Tanzania', 'Ethiopia', 'Ivory Coast']
for country in countries:
    print(f"I have visited {country}.")

# Output:
# I have visited Tanzania.
# I have visited Ethiopia.
# I have visited Ivory Coast.
```

When using a `for` loop, you define a variable (in this case, `country`) that takes on the value of each item in the list (`countries`) one at a time. So, when the loop runs, `country` will first be 'Tanzania', then 'Ethiopia', and finally 'Ivory Coast'.

## More within a for Loop

You can perform more complex operations within a `for` loop. 

```python
countries = ['tanzania', 'ethiopia', 'ivory coast']
for country in countries:
    print(f"{country.title()} was amazing!")

# Output:
# Tanzania was amazing!
# Ethiopia was amazing!
# Ivory Coast was amazing!
```

In this example, we use the `title()` method to capitalize the first letter of each word in the country names before printing them.

```python
countries = ['tanzania', 'ethiopia', 'ivory coast']
for country in countries:
    print(f"{country.title()} was amazing!")
    print("I cannot wait to visit again.\n")

# Output:
# Tanzania was amazing!
# I cannot wait to visit again.

# Ethiopia was amazing!
# I cannot wait to visit again.

# Ivory Coast was amazing!
# I cannot wait to visit again.
```

## Avoiding Indentation Errors

1. Alwats indent the line after the for statement in a loop. If you forget to indent, Python will raise an `IndentationError`.

2. At times, the loop will run without any errors but will not produce the expected output. 

For example, consider the following code:

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I cannot wait to see your next trick, {magician.title()}.\n")
```

The second call to `print()` is supposed to be idented, but since Python finds at least one indented line after the `for` statement, it assumes that the loop is complete. As a result, the second `print()` statement runs only once, after the loop has finished executing. Also, since the final value of `magician` is 'carolina', she is the only one who receives the message about the next trick.

The above is a logical error, meaning that the code runs without any syntax errors, but it does not produce the expected result. 

3. Also, avoid unnecessary indentation. 

4. Do not forget the colon (`:`) at the end of the `for` statement. Omitting the colon will raise a `SyntaxError`.

## Numerical Lists

There are various reasons that one may want to store a set of numbers. For example, you may need to keep track of the positions of each character in a game, or you may want to store the ages of a group of people. In data visualization, one may always work with sets of numbers, such as temperatures, population sizes, or sales figures.

### `range()` function

Python's `range()` function makes it easy to generate a series of numbers. 

```python
for value in range(0, 5):
    print(value)
# Output:
# 0
# 1
# 2
# 3
# 4
```

Note that the `range()` function starts at the first number provided (0 in this case) and stops just before the second number provided (5 in this case). Therefore, the output includes numbers from 0 to 4.

You can also pass just a single value to `range()`, and it will start from 0 by default:

```python
for value in range(5):
    print(value)
# Output:
# 0
# 1
# 2
# 3
# 4
```

### Using `range()` to Make a List of Numbers

You can use the `list()` function to convert the output of `range()` into a list:

```python
numbers = list(range(5))
print(numbers)
# Output:
# [0, 1, 2, 3, 4]
```

We can also use the `range()` function to tell Python to skip numbers in a given range. Here, we pass a third argument to `range()`, which indicates the step size:

```python
even_numbers = list(range(start=2, stop=11, step=2))
print(even_numbers)
# Output:
# [2, 4, 6, 8, 10]
```

You may also want to make a list of the first 10 square numbers. 

```python
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
# Output:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

In the above example, we start by creating an empty list called `squares`. Then we tell Python to loop through each value from 1 to 10. So, inside the loop, the current value is raised to the power of 2 and stored in the variable `square`. Finally, we append the value of `square` to the list `squares`. After the loop is complete, we print the list of square numbers. The above code can also be simplified as follows:


```python
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
# Output:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### List Comprehensions

A `list comprehension` allows you to generate a list in a single line of code, making it more concise and often easier to read. It combines the for loop and the creation of new elements into one line, and automatically appends each new element to the list. 

```python
squares = [value ** 2 for value in range(1, 11)]
print(squares)
# Output:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

