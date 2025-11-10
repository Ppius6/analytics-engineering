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

## Working with Parts of a List

### Slicing a List

To slice a list, you would specify the index of the first and last elements you would want to work with. Same as the `range()` function, the first index is inclusive, while the last index is exclusive.

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# Output:
# ['charles', 'martina', 'michael']
```

The example below omits the first index, so Python starts from the beginning of the list:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
# Output:
# ['charles', 'martina', 'michael', 'florence']
```

You can also omit the last index, and Python will slice the list up to the end:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
# Output:
# ['michael', 'florence', 'eli']
```

You can use negative indexing to slice a list from the end:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
# Output:
# ['michael', 'florence', 'eli']
```

### Looping through a Slice

You can also use a slice in a `for` loop if you want to loop through a subset of the elements in a list. 

Here, we loop through the first three players in the list and print their names as part of a simple roster:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
# Output:
# Here are the first three players on my team:
# Charles
# Martina
# Michael
```

Slices are powerful. For example, you can use slices to process your data in chunks of a specific size, display information in a series of pages with an appropriate amount of information on each page, or get a player's top three scores by sorting the list in decreasing order and taking a slice that includes just the first three scores.

### Copying a List

You may want to start with an existing list and make an entirely new list based on the first one. 

To do this, we make use of `[:]` to create a slice that includes the entire list:

```python
counties = ['Meru', 'Nairobi', 'Kisumu', 'Mombasa']
counties_ke = counties[:]
print("Original list:", counties)
print("Copied list:", counties_ke)
# Output:
# Original list: ['Meru', 'Nairobi', 'Kisumu', 'Mombasa']
# Copied list: ['Meru', 'Nairobi', 'Kisumu', 'Mombasa']
```

Now, if we modify the new list, the original list remains unchanged:

```python
counties = ['Meru', 'Nairobi', 'Kisumu', 'Mombasa']
counties_ke = counties[:]
counties_ke.append('Machakos')
print("Original list:", counties)
print("Modified copied list:", counties_ke)
# Output:
# Original list: ['Meru', 'Nairobi', 'Kisumu', 'Mombasa']
# Modified copied list: ['Meru', 'Nairobi', 'Kisumu', 'Mombasa', 'Machakos']
```

Note that if we had assigned `counties_ke = counties` without the slice, both variables would point to the same list in memory. Therefore, changes made to `counties_ke` would also affect `counties`. Using the slice `[:]` creates a new list in memory, allowing us to modify it independently.

## Tuples

Lists work well for storing collections of items that can change throughout the life of a program. However, there are times when you want to create a list of items that cannot be changed. In Python, we call these immutable lists `tuples`.

To define a tuple, you use parentheses `()` instead of square brackets `[]`:

```python
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# Output:
# 200
# 50
```

However, when we try to modify an element of a tuple, Python raises a `TypeError`:

```python
dimensions = (200, 50)
dimensions[0] = 250
# Output:
# TypeError: 'tuple' object does not support item assignment
```

When looping through a tuple, you can use a `for` loop just like with a list:

```python
dimensions = (200, 50)
for dim in dimensions:
    print(dim)
# Output:
# 200
# 50
```

Although you cannot modify a tuple directly, you can reassign a variable that holds a tuple to a new tuple:

```python
dimensions = (200, 50)
print("Original dimensions:")
for dim in dimensions:
    print(dim)

dimensions = (400, 100)
print("\nModified dimensions:")
for dim in dimensions:
    print(dim)
# Output:
# Original dimensions:
# 200
# 50
# 
# Modified dimensions:
# 400
# 100
```

Compared to lists, tuples are simple data structures. They are useful when you want to ensure that the data remains constant throughout the program.

## Styling Python Code

When writing Python code, it is important to follow certain styling conventions to ensure that your code is readable and maintainable. Here are some key points to consider:

1. Use 4 spaces per indentation level. Avoid using tabs, as they can lead to inconsistent indentation across different editors.

2. Most Python programmers recommend that each line should be less than 80 characters. Historically, this limit was set to accommodate older terminals and editors. While modern screens can handle longer lines, keeping lines shorter improves readability. However, PEP 8 recommends that lines should be limited to 79 characters for code and 72 characters for comments and docstrings. However, the guideline is not set in stone, and you may adjust it based on your project's needs.

3. Use blank lines to separate functions and classes, and to separate sections of code within functions. This helps to visually organize your code.

4. When naming variables, functions, and classes, use descriptive names that convey the purpose of the item. Use lowercase letters and underscores for variable and function names (e.g., `my_variable`, `calculate_sum`), and use CamelCase for class names (e.g., `MyClass`, `DataProcessor`).

5. Include comments in your code to explain complex logic or decisions. Use inline comments sparingly and ensure they are clear and concise.

