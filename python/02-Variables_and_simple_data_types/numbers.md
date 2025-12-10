## Numbers (Nangos)

Numbers are used to represent quantities, measurements, or values in various contexts. In programming, numbers can be integers, floating-point numbers, or complex numbers. They can be used in mathematical operations, comparisons, and data manipulation.

### Types of Numbers

- **Integers**: You can add, subtract, multiply, and divide integers. For example:
  ```python
  a = 5
  b = 3
  c = 2
  print(a + b)  # Output: 8
  print(a - b)  # Output: 2
  print(a * b)  # Output: 15
  print(a / b)  # Output: 1.6666666666666667
  print(a // b)  # Output: 1 (floor division)
  print(a % b)  # Output: 2 (modulus)
  print(a ** b)  # Output: 125 (exponentiation)
  print(a + b * c)  # Output: 11 (order of operations)
  ```

- **Floats**: Python calls any number with a decimal point a float, same as other programming languages. It refers to the fact that a decimal point can appear at any position in a number. Floats can be used without worrying about how they behave.
  ```python
  a = 0.1
  b = 0.2
  print(a + b)  # Output: 0.3
  print(a * b) # Output: 0.02
  print(a / b)  # Output: 0.5
  print(a - b)  # Output: -0.1
  ```

- **Integers and Floats**: When you divide any two numbers, even if they are integers that result in a whole number, Python will return a float. For example:
  ```python
  a = 4
  b = 2
  print(a / b)  # Output: 2.0
  ```
  If you mix an integer and a float in an operation, you will get a float as the result:
  ```python
  print(1 + 2.0)  # Output: 3.0
  print(2 * 3.0)  # Output: 6.0
  print(3.0 / 2)  # Output: 1.5
  ```

### Underscores in Numbers

When writing long numbers, you can group digits using underscores for better readability:
  ```python
    a = 1_000_000
    print(a)  # Output: 1000000
  ```
  However, Python ignores underscores in numbers.


### Multiple Assignments
You can assign values to more than one variable using just a single line of code. This helps shorten the programs and make them easier to read. 

```python
a, b, c = 1, 2, 3
print(a, b, c)  # Output: 1 2 3
```
### Constants
A `constant` is a variable whose value stays the same throughout the life of a program. In Python, there is no built-in way to create constants, but you can use uppercase variable names to indicate that a variable should be treated as a constant. For example:

```python
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)  # Output: 5000
```

When you want to treat a variable as a constant, you can use uppercase letters and underscores to separate words. This is a convention in Python to indicate that the variable should not be changed.