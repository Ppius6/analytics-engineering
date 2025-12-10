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

### Using `continue` in a Loop

Instead of breaking out of a loop entirely without executing the rest of its code, we can use the `continue` statement to return to the beginning of the loop, based on the result of a conditional test. 

For example, consider a loop that counts from 1 to 10 but prints only the odd numbers in that range:

```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)
```

First, we set `current_number` to 0. Because it is less than 10, Python enters the while loop. Once inside the loop, we increment the count by 1, so `current_number` is now 1. The `if` statement then checks the modulo of `current_number` and 2. If the result is 0, meaning `current_number` is divisible by 2 (i.e., it is even), the `continue` statement tells Python to ignore the rest of the loop and return to the beginning of the loop for the next iteration. If the number is odd, Python reaches the `print()` statement and prints the value of `current_number`. This process continues until `current_number` reaches 10.

When we run this program, the output looks like this:

```
1
3
5
7
9
```

### Avoiding Infinite Loops

Every while loop needs a way to stop running so it will not continue to run forever. For example, this counting loop should count from 1 to 5:

```python
x = 1
while x <= 5:
    print(x)
    x += 1
```

If we omit the line `x += 1`, the loop will run forever because the condition `x <= 5` will always be true as the value of x will start at 1 but never change. 

This is called an infinite loop. An infinite loop continues to execute as long as the program is running, which can cause the program to become unresponsive.

It is important to test every while loop and make sure the loop stops when you expect it to. If we want the program to end when the users enters a certain input value, run the program and enter that value. If the program does not end, scrutinize the way the program handles the value that should cause the loop to exit. Also, make sure at least one part of the program can make the loop's condition False or cause it to reach a `break` statement.

## Try it Yourself

1. Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you'll add that topping to their pizza.

```python
prompt = "Kindly enter the pizza toppings you would like to have."
prompt += "(Enter 'quit' after you finish to stop.) "

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else:
        print(f"I will add {topping} to your pizza.")
```

2. A movie theater charges different ticket prices depending on a person's age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop that prompts users for their age and then tells them the cost of their movie ticket. 

```python
prompt = "Please enter your age to determine the cost of your movie ticket."
prompt += "(Enter 'quit' to exit.) "

while True:
    age = input(prompt)
    
    if age.lower() == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif 3 <= age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")
```

3. Write a loop that never ends, and run it. (To end the loop, press Ctrl-C or close the window displaying the output.)

```python
x = 1
while x <= 3:
    print(x)
    x += 1 # This prevents the infinite loop
```

## Using a while Loop with Lists and Dictionaries

So far, we have only worked with only one piece of user information at a time. We received the user's input and then printed the input or a response to it.

However, we can use a while loop to collect as much input as we need and store that information in a list or dictionary for further processing later on. To modify a list as we work through it, we can use the `while` loop to move items from one list to another. 

### Moving Items from One List to Another

Consider a list of newly registered but unverified users of a website. After we verify these users, how can we move them to a list of verified users? One way would be to use a while loop to pull users from the list of unconfirmed users as we verify them and then add them to a separate list of confirmed users.

```python
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```
    
We begin with a list of `unconfirmed_users` and an empty list of `confirmed_users` to store the verified users. The while loop runs as long as there are unconfirmed users in the list. Inside the loop, we use the `pop()` method to remove the last user from the `unconfirmed_users` list and store it in the variable `current_user`. We then print a message indicating that we are verifying that user and add them to the `confirmed_users` list using the `append()` method. Once all users have been verified, we print out the list of confirmed users.

When we run this program, the output looks like this:

```
Verifying user: Candace
Verifying user: Brian
Verifying user: Alice

The following users have been confirmed:
Candace
Brian
Alice
```

### Removing All Instances of Specific Values from a List

We earlier used `remove()` to delete a specific value from a list. The `remove()` function worked because the value we were interested in appeared only once in the list. But what if we want to remove all instances of a value from a list?

In the example below, we have a list of pets that includes several instances of the value 'cat'. We can use a while loop to remove all instances of 'cat' from the list:

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)
```

We start with a list of `pets` that contains several 'cat' entries. The while loop checks if 'cat' is still in the `pets` list. If it is, the `remove()` method deletes the first occurrence of 'cat' from the list. This process continues until there are no more 'cat' entries left in the list. Finally, we print the modified list.

When we run this program, the output looks like this:

```
['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
['dog', 'dog', 'goldfish', 'rabbit']
```

### Filling a Dictionary with User Input

We can prompt for as much input as we need in each pass through a while loop. For example, we can make a polling program for the participant's name and response. We then store the data we gather in a dictionary, because we want to connect each response with a particular user.

```python
responses = {}

polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
```

The program first defines an empty dictionary called `responses` and sets a flag `polling_active` to `True` to indicate that the polling is active. As long as `polling_active` is `True`, Python will run the code in the while loop.

Within the loop, the user is prompted to enter their name and a mountain they would like to climb. The information is stored in the responses dictionary, and the user is asked whether or not to keep the poll running. If the user enters 'no', the flag `polling_active` is set to `False`, which causes the loop to end.

After the loop ends, the program prints the results of the poll by iterating through the `responses` dictionary and displaying each participant's name along with their chosen mountain.

When we run this program, the output might look like this:

```
What is your name? Alice
Which mountain would you like to climb someday? Everest
Would you like to let another person respond? (yes/no) yes

What is your name? Bob
Which mountain would you like to climb someday? Kilimanjaro
Would you like to let another person respond? (yes/no) no

--- Poll Results ---
Alice would like to climb Everest.
Bob would like to climb Kilimanjaro.
```

## Try it Yourself

1. Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as "I made your tuna sandwich." As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

```python
sandwich_orders = ['tuna', 'ham', 'veggie', 'turkey']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    
    print(f"I made your {order}.")
    finished_sandwiches.append(order)
    
print("The following sandwiches have been made: ")
for orders in finished_sandwiches:
    print(orders)
```

2. Using the list sandwich_orders from the previous exercise, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

```python
sandwich_orders = ['tuna', 'pastrami', 'ham', 'pastrami', 'veggie', 'pastrami', 'turkey']
finished_sandwiches = []

print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order}.")
    finished_sandwiches.append(order)

print("The following sandwiches have been made: ")
for orders in finished_sandwiches:
    print(orders)
```
3. Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.

```python
responsess = {}

polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    # Store the response in the dictionary.
    responsess[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responsess.items():
    print(f"{name} would like to go to {response}.")
```

