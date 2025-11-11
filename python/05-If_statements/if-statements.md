## If Statements

More often, programming involves examining a set of conditions and deciding which action to take based on those conditions. In Python, we use `if` statements to accomplish this.

An example of an `if` statement is shown below:

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

In the example above, we loop through a list of car brands. If the current car is a 'bmw', we print it in uppercase letters. For all other cars, we print them in title case (first letter capitalized).

### Conditional Tests

In every if statement, there is an expression that can be evaluated as `True` or `False`. If a conditional test evaluates to `True`, the code block under the `if` statement is executed. If it evaluates to `False`, the code block under the `else` statement (if present) is executed.

#### Equality Test

An equality test checks if two values are equal using the `==` operator. For example:

```python
car = 'audi'
print(car == 'audi')  # This will print True
print(car == 'bmw')   # This will print False
```

#### Ignoring Case when Checking for Equality

Testing for equality is case-sensitive. For example, two values with different capitalization are not considered equal:

```python
car = 'Audi'
print(car == 'audi')  # This will print False
```

To perform a case-insensitive comparison, you can convert both values to the same case using the `lower()` or `upper()` methods:

```python
car = 'Audi'
print(car.lower() == 'audi')  # This will print True
```

#### Inequality Test

When we want to determine whether two values are not equal, we can use the `inequality` operator `!=`:

```python
fav_food = 'carrot soup'

if fav_food != 'Pumpkin soup':
    print("That's not my favorite!")
```

#### Numerical Comparisons

Testing numerical values is similar to testing strings. You can use the following operators for numerical comparisons:

- `==` : equal to
- `!=` : not equal to
- `>`  : greater than
- `<`  : less than
- `>=` : greater than or equal to
- `<=` : less than or equal to

```python
age = 20

print(age == 20)   # True
print(age != 25)   # True
print(age > 18)    # True
print(age < 30)    # True
print(age >= 20)   # True
print(age <= 25)   # True
```

#### Multiple Conditions

You can test multiple conditions using the `and` and `or` operators.

- `and` : Both conditions must be true for the overall expression to be true.
- `or`  : At least one condition must be true for the overall expression to be true.

```python
age = 22
has_license = True
in_school = False

if age >= 18 and has_license:
    print("You can drive.")
elif age < 18 or in_school:
    print("You cannot drive.")
```

We can also wrap multiple conditions in parentheses to make the code more readable:

```python
age_0 = 22
age_1 = 18

if (age_0 >= 21) and (age_1 >= 21):
    print("Both are of legal drinking age.")
else:
    print("At least one is not of legal drinking age.")
```

#### Checking whether a Value is in a List

You can check whether a value is present in a list using the `in` keyword:

```python
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

user in banned_users  # This will return False
# or
'marie' in banned_users  # This will return False too
```

#### Checking whether a Value is not in a List

You can check whether a value is absent from a list using the `not in` keyword:

```python
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
user not in banned_users  # This will return True
# or
'marie' not in banned_users  # This will return True too
# or
if user not in banned_users:
    print(f"{user.title()}, you are free to go through!")
```

#### Boolean Expressions

A boolean expression is either `True` or `False` just like the value of a conditional expression after it has been evaluated. Boolean values help to keep track of certain conditions such as whether a game is running or wherether a user is logged in.

```python
game_active = True
can_edit = False
```

### if Stements

An `if` statement evaluates a conditional test and executes a block of code only if the test is `True`. Here is the syntax of an `if` statement:

```python
if conditional_test:
    # Code to execute if the test is True
```

For example:

```python
age = 20

if age >= 18:
    print("You are old enough to vote!")
```

#### if-else Statements

We may want to take one action when a conditional test passes and a different action in all other cases. Python's `if-else` is similar to a simple `if` statement, but the `else` statement allows us to define an action or set of actions that are executed when the conditional test fails.

```python
age = 17
if age >= 18:
    print("You can vote!")
else:
    print("Sorry, you are too young to vote.")
```

If the first conditional test passes, the first block of indented print() calls is executed. If the test fails, the code block under the `else` statement is executed. Since the age is less than 18, the conditional test fails and the code in the `else` block runs.

#### if-elif-else Chain

Often, we may need to test more than two possible situations. In these cases, we can use an `if-elif-else` chain. Python executes only one block of code in an `if-elif-else` chain. It runs the first block where the conditional test evaluates to `True` and skips the rest of the chain.

```python
age = 12

if age < 1:
    print("The train ticket is free.")
elif age < 5:
    print("The train ticket is half the price.")
else:
    print("The train ticket is full price.")
```

We can still add as many `elif` blocks as necessary to test multiple conditions:

```python
age = 65

if age < 1:
    print("The train ticket is free.")
elif age < 5:
    print("The train ticket is half the price.")
elif age < 65:
    print("The train ticket is full price.")
else:
    print("The train ticket is half the price for seniors.")
```

#### Omitting the else Block

The `else` block is not required in an `if-elif` chain. If none of the conditions are met, no code block will be executed.

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")
```

#### Testing Multiple Conditions

In the if-elif-else chain, we can test multiple conditions. If Python finds a condition that is `True`, it ignores the rest of the conditions.

```python
countries = ['usa', 'canada', 'australia', 'india', 'germany']

if 'usa' in countries:
    print("USA is in the list.")
elif 'canada' in countries:
    print("Canada is in the list.")
elif 'india' in countries:
    print("India is in the list.")
```