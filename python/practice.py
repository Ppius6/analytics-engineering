name = "Pius"
print(f"Hello {name}, would you like to learn some Python today?")

print(name.lower())

author = "Friedrich Nietzsche"
print(f'{author} once said, "He who has a why to live can bear almost any how"')

author = "Friedrich Nietzsche"
message = "He who has a why to live can bear almost any how"
print(f'{author} once said, "{message}"')

me = " Mutuma  "
print(me.rstrip())
print(me.lstrip())
print(me.strip())

f_name = "Pius Mutuma"
print(f"\tPius\nMutuma")

filename = "python_notes.txt"
clean_url = filename.removesuffix(".txt")
print(clean_url)

names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(f"Hello, {name}! When are we meeting up for lunch?")


motorcycles = ["Honda", "Yamaha", "Suzuki", "BMW"]

for _ in motorcycles:
    print("I would like to own a " + _ + " motorcycle.")

dinner_guests = ["Alice", "Bob", "Charlie"]
for guest in dinner_guests:
    print(
        f"Heya, {guest}! You are invited for some Nyama Choma this weekend at my place. Hope you can make it!"
    )

dinner_guests = ["Alice", "Bob", "Charlie"]
print(f"{dinner_guests[1]} cannot make it for the Nyam Choms this weekend.")

dinner_guests[1] = "David"
for guest in dinner_guests:
    print(
        f"Heya, {guest}! You are invited for some Nyama Choma this weekend at my place. Hope you can make it!"
    )

dinner_guests.insert(0, "Eve")
dinner_guests.insert(2, "Frank")
dinner_guests.append("Grace")
for g in dinner_guests:
    print(
        f"Heya, {g}! You are invited for some Nyama Choma this weekend at my place. Hope you can make it!"
    )

print("I can only invite two people for dinner.")
while len(dinner_guests) > 2:
    removed_guest = dinner_guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")
for g in dinner_guests:
    print(
        f"Heya, {g}! You are still invited for some Nyama Choma this weekend at my place. Hope you can make it!"
    )

print(len(dinner_guests))


locations = ["Ethiopia", "South Africa", "Namibia", "Georgia", "Afghanistan"]

print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations.reverse())
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

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

usernames = ["admin", "user1", "user2", "user3", "user4"]

for name in usernames:
    if name == "admin":
        print(f"Hello {name}, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")

current_users = ["user1", "user2", "user3", "user4", "user5"]

new_users = ["nuser1", "nuser2", "nuser3", "user4", "user5"]

for user in new_users:
    if user in current_users:
        print("Enter a new username")
    else:
        print("Your username is available")

numbers = list(range(1, 10))

for num in numbers:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")


pius = {"first_name": "Pius", "last_name": "Mutuma", "age": 25, "city": "Meru"}

for k, v in pius.items():
    print(f"{k}: {v}")

print(pius["first_name"])
print(pius["last_name"])
print(pius["age"])
print(pius["city"])

fav_nums = {
    "Pius": 1,
    "Alice": 7,
    "Bob": 3,
    "Charlie": 42,
}

for k, v in fav_nums.items():
    print(f"{k}'s favorite number is {v}.")

# or
for name in fav_nums:
    print(f"{name}'s favorite number is {fav_nums[name]}.")


# A loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you'll add that topping to their pizza.

prompt = "Kindly enter the pizza toppings"
prompt += "(Enter 'quit' after you finish to stop.) "

while True:
    topping = input(prompt)

    if topping == "quit":
        break
    else:
        print(f"I will add {topping} to your pizza.")

# 2 - Movie Tickets

prompt = "Please enter your age to determine the cost of your movie ticket."
prompt += "(Enter 'quit' to exit.) "

while True:
    age = input(prompt)

    if age.lower() == "quit":
        break
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif 3 <= age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")

unconfirmed_users = ["alice", "brian", "candace"]
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


# School to go

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which school would you like to attend? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

print("\n -- Polling results --")
for name, response in responses.items():
    print(f"{name} would like to attend {response}.")


# 1. Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as "I made your tuna sandwich." As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ["tuna", "ham", "veggie", "turkey"]
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()

    print(f"I made your {order}.")
    finished_sandwiches.append(order)

print("The following sandwiches have been made: ")
for orders in finished_sandwiches:
    print(orders)

sandwich_orders = [
    "tuna",
    "pastrami",
    "ham",
    "pastrami",
    "veggie",
    "pastrami",
    "turkey",
]
finished_sandwiches = []

print("The deli has run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order}.")
    finished_sandwiches.append(order)

print("The following sandwiches have been made: ")
for orders in finished_sandwiches:
    print(orders)

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
    if repeat.lower() == "no":
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responsess.items():
    print(f"{name} would like to go to {response}.")


def make_shirt(size, message):
    print(f"The message of the shirt of size {size} is {message}")


make_shirt("L", "I love Python")


def make_shirt(size="L", message="I love Python"):
    print(f"The message of the shirt of size {size} is {message}")


make_shirt()
make_shirt("M")
make_shirt("S", "I love JavaScript")


def describe_city(name, country="Kenya"):
    print(f"{name} is in {country}.")


describe_city("Nairobi")
describe_city("Mombasa")
describe_city("Kisumu", "Kenya")


def city_country(city, country):
    city = input("Enter city name: ")
    country = input("Enter country name: ")

    return f"{city.title()}, {country.title()}"


print(city_country("city", "country"))


def make_album(artist, title):
    album = {"artist": artist, "title": title}
    return album


albums = make_album("me", "wimbo")
print(albums)


def make_album(artist, title, tracks=None):
    album = {"artist": artist, "title": title}

    if tracks:
        album["tracks"] = tracks
    return album


albums = make_album("me", "wimbo", tracks=10)
print(albums)


## WHile loop
def make_album(artist, title):
    album = {"artist": artist, "title": title}
    return album


while True:
    print("\nEnter q at any time to quit")

    artist = input("Enter the artist name: ")
    if artist.lower() == "q":
        break

    title = input("Enter the title of the album: ")
    if title.lower() == "q":
        break

    albumz = make_album(artist, title)
    print(albumz)

# 1
messages = ["Hey, you.", "Ni mimi", "Unanikumbuka?"]


def show_message(message):
    for message in messages:
        print(message)


show_message(messages)

# 2 - Start with a copy of your program from Exercise 8-10. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.

messages = ["Hey, you.", "Ni mimi", "Unanikumbuka?"]
sent_messages = []


def send_messages(messages_list):
    """
    Print each message and move it to sent_messages list.
    """
    while messages_list:
        current_message = messages_list.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


send_messages(messages)

print("\nMessages in the original list:")
print(messages)

print("\nMessages in the sent_messages list:")
print(sent_messages)

# 3 - Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.

messages = ["Hey, you.", "Ni mimi", "Unanikumbuka?"]
sent_messages = []


def send_messages(messages_list):
    """
    Print each message and move it to sent_messages list.
    """
    while messages_list:
        current_message = messages_list.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


send_messages(messages[:])  # Pass a copy of the list

print("\nMessages in the original list:")
print(messages)

print("\nMessages in the sent_messages list:")
print(sent_messages)

# 8-12 - Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time.


def make_sandwich(*items):
    """
    Print a summary of the sandwich that is being ordered.
    """
    print(f"\nMaking a sandwich with the following additions:")
    for item in items:
        print(f"- {item}")


make_sandwich("lettuce", "tomato", "bacon")
make_sandwich("turkey", "cheese")

# 8-13 - User Profile: Start with a copy of user_profile.py from page 153. Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.


def build_profile(first, last, **user_info):
    """
    Build a dictionary containing everything about me.
    """
    user_info["first_name"] = first
    user_info["last_name"] = last

    return user_info


my_profile = build_profile(
    "Pius", "Mutuma", location="Meru", field="Engineering", hobby="Reading"
)
print(my_profile)

# 8-14 - Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as color and optional features. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True). Print the dictionary that’s returned to make sure all the information was stored correctly.


def make_car(manufacturer, model_name, **car_info):
    """
    Build a car profile
    """
    car_info["manufacturer"] = manufacturer
    car_info["name"] = model_name

    return car_info


car = make_car("subaru", "outback", color="blue", tow_package=True)


class Dog:
    """
    A simple attempt to model a dog
    """

    def __init__(self, name, age):
        """
        Initialize name and age attributes
        """
        self.name = name
        self.age = age

    def sit(self):
        """
        Simulate a dog sitting in response to a command
        """
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """
        Simulate rolling over in response to a command
        """
        print(f"{self.name} rolled over!")


my_dog = Dog("Willie", 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")


class Dog:
    """
    A simple attempt to model a dog
    """

    def __init__(self, name, age):
        """
        Initialize name and age attributes
        """
        self.name = name
        self.age = age

    def sit(self):
        """
        Simulate a dog sitting in response to a command
        """
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """
        Simulate rolling over in response to a command
        """
        print(f"{self.name} rolled over!")


my_dog = Dog("Willie", 6)
your_dog = Dog("Steve", 4)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")


# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.


class Restaurant:
    """
    Print some information about a restaurant
    """

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize the restaurant name and cuisine types
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """
        Print some information about a restaurant
        """
        print(f"The restaurant is called {self.restaurant_name}")
        print(f"The {self.restaurant_name} offers this cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        """
        Print if the restaurant is open or closed
        """
        print(f"The {self.restaurant_name} is open.")


restaurant = Restaurant("Kwa Mathe", "Chapati Ndodo")
restaurant_1 = Restaurant("Kwa Mathe", "Chafua")
restaurant_2 = Restaurant("Kwangu", "Nyama")

# Print the two attributes individually
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

print(restaurant_1.restaurant_name)
print(restaurant_1.cuisine_type)

print(restaurant_2.restaurant_name)
print(restaurant_2.cuisine_type)

# Call both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()


class User:
    """
    Hold a user's information and greet them.
    """

    def __init__(self, first_name, last_name):
        """
        Initialize the first and last name
        """
        self.firt_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """
        Print a user's summary
        """
        print(f"This user is known as {self.firt_name} {self.last_name}")

    def greet_user(self):
        """
        Greet a user
        """
        print(f"Hello, {self.firt_name} {self.last_name}!")


user = User("Pius", "Mutuma")
user_1 = User("Me", "You")

user.describe_user()
user.greet_user()


class Car:

    def __init__(self, make, model, year):
        """
        Initialize attributes to describe a car
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """
        Return a neatly formatted descriptive name
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """
        Print a statement showing the car's mileage
        """
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
print(my_new_car.read_odometer())


class Car:

    def __init__(self, make, model, year):
        """
        Initialize attributes to describe a car
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """
        Return a neatly formatted descriptive name
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """
        Print a statement showing the car's mileage
        """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value
        """
        self.odometer_reading = mileage


my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
print(my_new_car.read_odometer())


class Car:

    def __init__(self, make, model, year):
        """
        Initialize attributes to describe a car
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """
        Return a neatly formatted descriptive name
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """
        Print a statement showing the car's mileage
        """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer! Mchezo wa Taoni!")

    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading
        """
        self.odometer_reading += miles


my_used_car = Car("audi", "a4", 2024)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
print(my_used_car.read_odometer())

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# From the restaurant exercise, add an attribute: number_served with a default value of 0. Create an instance and print the number of customers the restaurant has served, and then change this value and print it again.


class Restaurant:
    """
    Print some information about a restaurant
    """

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize the restaurant name and cuisine types
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numbers_served = 0

    def describe_restaurant(self):
        """
        Print some information about a restaurant
        """
        print(f"The restaurant is called {self.restaurant_name}")
        print(f"The {self.restaurant_name} offers this cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        """
        Print if the restaurant is open or closed
        """
        print(f"The {self.restaurant_name} is open.")

    def set_number_served(self, customers):
        """
        Set the number of served customers
        """
        self.numbers_served = customers

    def increment_number_served(self, customers):
        """
        Increment the number of served customers
        """
        self.numbers_served += customers

    def read_total_customers(self):
        """
        Return total served customers
        """
        print(f"There are a total of {self.numbers_served} customers served.")


restaurant = Restaurant("Kwa Mathe", "Chapati Ndodo")

print(restaurant.read_total_customers())

print(restaurant.set_number_served(10))

print(restaurant.read_total_customers())

print(restaurant.increment_number_served(4))

print(restaurant.read_total_customers())

# Add an attribute with login_attempts - increment_login_attempts() that increments the value of login_attempts by 1, reset_login_attempts() to reset the value of login_attempts to 0


class User:
    """
    Hold a user's information and greet them.
    """

    def __init__(self, first_name, last_name):
        """
        Initialize the first and last name
        """
        self.firt_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """
        Print a user's summary
        """
        print(f"This user is known as {self.firt_name} {self.last_name}")

    def greet_user(self):
        """
        Greet a user
        """
        print(f"Hello, {self.firt_name} {self.last_name}!")

    def increment_login_attempts(self):
        """
        Increment the number of login attempts
        """
        self.login_attempts += 1

    def reset_login_attempts(self):
        """
        Reset the number of login attempts
        """
        self.login_attempts = 0


user = User("Pius", "Mutuma")
user_1 = User("Me", "You")

user.describe_user()
user.greet_user()

print(user.login_attempts)
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)


class Car:

    def __init__(self, make, model, year):
        """
        Initialize attributes to describe a car
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """
        Return a neatly formatted descriptive name
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """
        Print a statement showing the car's mileage
        """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer! Mchezo wa Taoni!")

    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading
        """
        self.odometer_reading += miles


class ElectricCar(Car):
    """
    Represent aspects of a car, specific to electric vehicles
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        """
        super().__init__(make, model, year)


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())


class Car:

    def __init__(self, make, model, year):
        """
        Initialize attributes to describe a car
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """
        Return a neatly formatted descriptive name
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """
        Print a statement showing the car's mileage
        """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer! Mchezo wa Taoni!")

    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading
        """
        self.odometer_reading += miles


class ElectricCar(Car):
    """
    Represent aspects of a car, specific to electric vehicles
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """
        Print a statement describing the battery size
        """
        print(f"This car has a {self.battery_size}-kWh battery")


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()


class Car:

    def __init__(self, make, model, year):
        """
        Initialize attributes to describe a car
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """
        Return a neatly formatted descriptive name
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """
        Print a statement showing the car's mileage
        """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer! Mchezo wa Taoni!")

    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading
        """
        self.odometer_reading += miles


class Battery:
    """
    A simple attempt to model a battery for an electric car
    """

    def __init__(self, battery_size=40):
        """
        Initialize the battery's attributes
        """
        self.battery_size = battery_size

    def describe_battery(self):
        """
        Print a statement describing the battery size
        """
        print(f"This car has a {self.battery_size}-kWh battery")


class ElectricCar(Car):
    """
    Represent aspects of a car, specific to electric vehicles
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()


class Car:

    def __init__(self, make, model, year):
        """
        Initialize attributes to describe a car
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """
        Return a neatly formatted descriptive name
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """
        Print a statement showing the car's mileage
        """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer! Mchezo wa Taoni!")

    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading
        """
        self.odometer_reading += miles


class Battery:
    """
    A simple attempt to model a battery for an electric car
    """

    def __init__(self, battery_size=40):
        """
        Initialize the battery's attributes
        """
        self.battery_size = battery_size

    def describe_battery(self):
        """
        Print a statement describing the battery size
        """
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """
        Print a statement about the range this battery provides
        """
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This can can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """
    Represent aspects of a car, specific to electric vehicles
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

# 9.6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IcecreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 166). Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IcecreamStand, and call this method.


class Restaurant:
    """
    Print some information about a restaurant
    """

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize the restaurant name and cuisine types
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numbers_served = 0

    def describe_restaurant(self):
        """
        Print some information about a restaurant
        """
        print(f"The restaurant is called {self.restaurant_name}")
        print(f"The {self.restaurant_name} offers this cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        """
        Print if the restaurant is open or closed
        """
        print(f"The {self.restaurant_name} is open.")

    def set_number_served(self, customers):
        """
        Set the number of served customers
        """
        self.numbers_served = customers

    def increment_number_served(self, customers):
        """
        Increment the number of served customers
        """
        self.numbers_served += customers

    def read_total_customers(self):
        """
        Return total served customers
        """
        print(f"There are a total of {self.numbers_served} customers served.")


class IcecreamStand(Restaurant):
    """
    Display available ice cream flavors
    """

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the restaurant class
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanilla", "Strawberry"]

    def display_flavors(self):
        """
        Print the available ice cream flavors
        """
        print(f"The available ice cream flavors are: {', '.join(self.flavors)}")


ice_cream_stand = IcecreamStand("Kwa Mathe", "Chapati Ndodo")

print(ice_cream_stand.restaurant_name)
print(ice_cream_stand.cuisine_type)
ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
ice_cream_stand.set_number_served(10)
ice_cream_stand.increment_number_served(4)
ice_cream_stand.read_total_customers()
ice_cream_stand.display_flavors()


# 9.7 - Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 170). Add an attribute called privileges that stores a list of strings representing the administrator’s privileges like "can add post", "can delete post", "can ban user". Write a method called show_privileges() that lists the administrator’s privileges. Create an instance of Admin, and call your method.


class User:
    """
    Hold a user's information and greet them.
    """

    def __init__(self, first_name, last_name):
        """
        Initialize the first and last name
        """
        self.firt_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """
        Print a user's summary
        """
        print(f"This user is known as {self.firt_name} {self.last_name}")

    def greet_user(self):
        """
        Greet a user
        """
        print(f"Hello, {self.firt_name} {self.last_name}!")


class Admin(User):
    """
    Represent the features of an admin, a special kind of user with more roles
    """

    def __init__(self, first_name, last_name):
        """
        Initialize the attributes of the parent class, User
        """
        super().__init__(first_name, last_name)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can close channel",
        ]

    def show_privileges(self):
        """
        Show the privileges of an admin user
        """
        print(f"The available privileges of an admin user are {self.privileges}")


admin_pizzo = Admin("Pius", "Mutuma")
admin_pizzo.show_privileges()
print(admin_pizzo.firt_name)
print(admin_pizzo.last_name)


# Separating restaurant into modules


class Restaurant:
    """
    Print some information about a restaurant
    """

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize the restaurant name and cuisine types
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numbers_served = 0

    def describe_restaurant(self):
        """
        Print some information about a restaurant
        """
        print(f"The restaurant is called {self.restaurant_name}")
        print(f"The {self.restaurant_name} offers this cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        """
        Print if the restaurant is open or closed
        """
        print(f"The {self.restaurant_name} is open.")

    def set_number_served(self, customers):
        """
        Set the number of served customers
        """
        self.numbers_served = customers

    def increment_number_served(self, customers):
        """
        Increment the number of served customers
        """
        self.numbers_served += customers

    def read_total_customers(self):
        """
        Return total served customers
        """
        print(f"There are a total of {self.numbers_served} customers served.")


class IcecreamStand(Restaurant):
    """
    Display available ice cream flavors
    """

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the restaurant class
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanilla", "Strawberry"]

    def display_flavors(self):
        """
        Print the available ice cream flavors
        """
        print(f"The available ice cream flavors are: {', '.join(self.flavors)}")


ice_cream_stand = IcecreamStand("Kwa Mathe", "Chapati Ndodo")

print(ice_cream_stand.restaurant_name)
print(ice_cream_stand.cuisine_type)
ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
ice_cream_stand.set_number_served(10)
ice_cream_stand.increment_number_served(4)
ice_cream_stand.read_total_customers()
ice_cream_stand.display_flavors()


# 9-13. Dice


class Die:
    """
    Some information about a die
    """

    def __init__(self, sides=6):
        """
        Initilize a die with sides
        """
        self.sides = sides

    def roll_die(self):
        """
        Roll a die and print a random number between 1 and number of sides the die has
        """
        from random import randint

        result = randint(1, self.sides)
        print(result)


# Make a 6-sided die and roll it 10 times
die = Die(6)
die.roll_die()

for roll_num in range(10):
    die.roll_die()

# 20 sided die and roll it 10 times
die = Die(20)

for roll_num in range(20):
    die.roll_die()

# 9-14. Lottery


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("Boeing", "747")  # Create a Plane object

for x in (car1, boat1, plane1):
    x.move()


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("Boeing", "747")  # Create a Plane object

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age


p1 = Person("Me", 25)
print(p1.name)
print(p1.__age)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age


p1 = Person("Me", 25)
print(p1.name)
print(p1.get_age())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")


p1 = Person("Me", 25)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age())


class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, num):
        if not isinstance(num, (int, float)):
            return False
        return True

    def add(self, num):
        if self.__validate(num):
            self.result += num
        else:
            print("Invalid number")


calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age


p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age)  # Not recommended!


from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()
print(contents)

# 10-11 - Favorite Number: Write a program that prompts for the user’s favorite number. Use json.dump() to store this number in a file. Write a separate program that reads this value back in and prints the message, "I know your favorite number! It’s _____."

import json
from pathlib import Path

number = input("What is your favorite number? ")

path = Path("favorite_number.json")
contents = json.dumps(number)
path.write_text(contents)

number = path.read_text()
favorite_number = json.loads(number)
print(f"I know your favorite number! It's {favorite_number}")

# 10-12 - Favorite Number Remembered: Write a program that prompts for the user’s favorite number. If the number has already been stored, retrieve it and print the message, "I know your favorite number! It’s _____." If not, prompt for the number and store it in a file. Run the program twice to see that it works.
import json
from pathlib import Path

path = Path("favorite_number.json")

if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}")
else:
    number = input("What is your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    print("I'll remember that for next time!")

# 10-13 - User Dictionary: Expanding the amount of information stored about a user. Before printing a welcome message in greet_user(), ask the user if this is the correct username. If it is not, call get_new_username() to get the correct username.

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
    path = Path("username.json")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """
    Greet the user by name.
    """
    path = Path("username.json")

    username = get_stored_username(path)

    correct = input(f"Is your name {username}? (y/n) ")
    if correct.lower() != "y":
        username = None
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We will remember you when you come back, {username}!")


greet_user()
