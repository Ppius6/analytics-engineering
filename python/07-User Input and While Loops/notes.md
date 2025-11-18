# User Input and While Loops

Most programs are written to solve an end user's problem. But, we need to get some information from the user. 

For example, say someone wants to find out whether they are old enough to vote. If we write a program to answer this question, we need to know the user's age before we can give them an answer. 

## `input()` Function

The `input()` function pauses our program and waits for the user to enter some text. Once Python receives the user's input, it assigns that input to a variable to make it convenient to work with later in the program.

For example, we ask the user to enter some text, then display that text back to them:

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

When this program runs, it displays the prompt inside the `input()` function. The program then waits for the user to type something and press Enter. Once they do, the text they entered is stored in the variable `message`, and we print it back to them.

The output might look like this:

```
Tell me something, and I will repeat it back to you: Hello, Python!
Hello, Python!
```

### Writing Clear Prompts

Whenever we use the `input()` function, we should include a clear, easy-to-follow prompt that tells the user exactly what kind of information we want from them. This makes it easier for the user to understand what they need to do.

For example, instead of a vague prompt like "Enter something:", we can use a more specific prompt like "Please enter your favorite programming language:".

```python
favorite_language = input("Please enter your favorite programming language: ")
print("Your favorite programming language is " + favorite_language + ".")
```

Note: It is important to add a space at the end of the prompts (after the colon in the preceding examples) so that there is a space between the prompt and the user's input.

Our program's output might look like this:

```
Please enter your favorite programming language: Python
Your favorite programming language is Python.
```

We may want to write a prompt that is longer than one line. We can therefore assign our prompt to a variable and pass that variable to the `input()` function which allows us to build our prompt over several lines.

```python
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("Hello, " + name + "!")
```

The first line assigns the first part of the message to the variable `prompt`. In the second line, the operator `+=` takes the string that was assigned to `prompt` and adds the new string onto the end. Our prompt now spans two lines, again with space after the question mark for clarity.

When we run this program, the output looks like this:

```
If you tell us who you are, we can personalize the messages you see.
What is your first name? Alice
Hello, Alice!
```

### Using `int()` to Accept Numerical Input

By default, the `input()` function always returns user input as a string. If we want to work with numerical input, we need to convert that string to a number using the `int()` function (for integers) or the `float()` function (for floating-point numbers).

For example, if we want to ask the user for their age and then calculate the year they were born, we can do it like this:

```python
age = input("How old are you? ")
age = int(age) # Convert the input string to an integer
birth_year = 2025 - age
print("You were born in " + str(birth_year) + ".")
```

When we run this program, the output might look like this:

```
How old are you? 30
You were born in 1995.
```

### The Modulo Operator

The modulo operator (`%`) is a useful mathematical operator which divides one number by another number and returns the remainder. For example:

```python
print(7 % 3)  # Output: 1 - 7 divided by 3 is 2 with a remainder of 1
print(10 % 4) # Output: 2 - 10 divided by 4 is 2 with a remainder of 2
print(12 % 5) # Output: 2 - 12 divided by 5 is 2 with a remainder of 2
```

NOTE: The modulo operator does not tell us how many times one number fits into another; it only tells us what the remainder is after division.

When one number is divisible by another number, the remainder is 0, so the modulo operator always returns 0. We can use this fact to determine if a number is even or odd.

```python
number = input("Enter a number, and I will tell you if it is even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
```

When we run this program, the output might look like this:

```
Enter a number, and I will tell you if it is even or odd: 7
The number 7 is odd.
```

## Introducing While Loops

The `for loop` takes a collection of items and executes a block of code once for each item in the collection. A `while loop`, on the other hand, runs as long as a certain condition is true.

We can use a `while loop` to count up through a series of numbers. For example, the following while loop counts from 1 to 5:

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

In this example, we start by setting the variable `current_number` to 1. The `while` statement checks whether `current_number` is less than or equal to 5. If it is, the code inside the loop runs, printing the current number and then incrementing `current_number` by 1. This process repeats until `current_number` is greater than 5. The += operator is shorthand for `current_number = current_number + 1`. The code stops running once the value of `current_number` exceeds 5.

When we run this program, the output looks like this:

```
1
2
3
4
5
```

### Letting the User Choose When to Quit

We can use a `while loop` to let the user decide when to quit the program. For example, we can create a program that repeatedly asks the user for input until they type 'quit':

```python
prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\n(Enter 'quit' to end the program.) "
message = ""
while message.lower() != 'quit':
    message = input(prompt)

    if message.lower() != 'quit':
        print(message)
```

In this program, we set up a prompt that tells the user how to quit. We initialize the variable `message` to an empty string. The `while` loop checks if `message` is not equal to 'quit' (case insensitive). Inside the loop, we get input from the user and print it back to them. The loop continues until the user types 'quit'.

When we run this program, the output might look like this:

```
Tell me something, and I will repeat it back to you.
(Enter 'quit' to end the program.) Hello!
Hello!

Tell me something, and I will repeat it back to you.
(Enter 'quit' to end the program.) How are you?
How are you?

Tell me something, and I will repeat it back to you.
(Enter 'quit' to end the program.) quit
```

The program ends when the user types 'quit'.

### Using a Flag

In a game, several different events can end a game. When the player runs out of ships, their game runs out, or the cities they were supposed to protect are all destroyed. It needs to end if any of these events happen. If many possible events might occur to stop the program, trying to test all these conditions in one while statement can get complicated.

For a program that should run only as long as many conditions are true, we can define one variable that determines whether or not the entire program is active. This kind of variable is called a flag. A flag acts as a signal to the program. When the flag is set to True, the program runs; when it is set to False, the program stops.

For example, 

```python
prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\n(Enter 'quit' to end the program.) "

active = True
while active:
    message = input(prompt)

    if message.lower() == 'quit':
        active = False
    else:
        print(message)
```

Here, we set the variable `active` to `True` so the program starts in an active state. Doing so makes the while statement simpler because no comparison is made in the while statement itself; the logic is taken care of in other parts of the program. As long as the `active` flag remains `True`, the loop continues. If the user types 'quit', we set `active` to `False`, which causes the loop to end.

When we run this program, the output behaves the same way as before, allowing the user to enter messages until they decide to quit.

```

Tell me something, and I will repeat it back to you.
(Enter 'quit' to end the program.) rr
rr

Tell me something, and I will repeat it back to you.
(Enter 'quit' to end the program.) rr
rr

Tell me something, and I will repeat it back to you.
(Enter 'quit' to end the program.) quit
```

The program ends when the user types 'quit'.

### Using `break` to Exit a Loop

To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the `break` statement. It directs the flow of your program; you can use it to control which lines of code are executed and which are skipped, so the program only executes code that you want it to, when you want it to.

For example, consider this program that asks a user about places they have visited. We can stop the while loop in this program by calling break as soon as the user enters 'quit':

```python
prompt = "\nPlease enter the name of a city you have visited."
prompt += "\n(Enter 'quit' to end the program.) "

while True:
    city = input(promt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
```

In this program, we use `while True:` to create an infinite loop that will continue until we explicitly break out of it. Inside the loop, we check if the user entered 'quit'. If they did, we call `break` to exit the loop immediately. If they entered anything else, we print a message about the city they mentioned.

When we run this program, the output might look like this:

```
Please enter the name of a city you have visited.
(Enter 'quit' to end the program.) Addis Abeba
I'd love to go to Addis Abeba!

Please enter the name of a city you have visited.
(Enter 'quit' to end the program.) Nairobi
I'd love to go to Nairobi!

Please enter the name of a city you have visited.
(Enter 'quit' to end the program.) quit
```

