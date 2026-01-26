# Simple function

# def morning_message():
#     """Display a morning message"""
#     print( "Good morning" )

# morning_message()

# def morning_message(first_name, last_name):
#     """Display a customized morning message"""
#     full_name = f"{first_name.title()} {last_name.title()}"
#     message = "Good morning "
#     return message + full_name

# message = morning_message(first_name="pius", last_name="mutuma")
# print(message)

# def return_user(first_name, last_name, age=None):
#     """Return a dictionary of information about a person"""
#     user = {
#         "first": first_name,
#         "last": last_name
#     }
#     if age:
#         user['age'] = age

#     return user

# user1 = return_user("Me", "You", 25)
# print(user1)

# Function + a while loop - initial iteration


# def get_formatted_name(first_name, last_name, age=None):
#     """Return a well formatted name"""
#     full_name = f"{first_name} {last_name}, aged {age}"
#     return full_name.title()


# while True:
#     print("\nPlease tell me your name: ")
#     print("(Enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == "q":
#         break

#     l_name = input("Last name: ")
#     if l_name == "q":
#         break

#     u_age = input("Enter your age (or press Enter to skip): ")
#     if u_age == "q":
#         break

#     u_age = u_age if u_age else None

#     formatted_name = get_formatted_name(f_name, l_name, u_age)
#     print(f"\nHello, {formatted_name}")


# # Function + a while loop
# def get_formatted_name(first_name, last_name, age=None):
#     """Return a well formatted name"""
#     if age:
#         full_name = f"{first_name} {last_name}, aged {age}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()


# while True:
#     print("\nPlease tell me your name: ")
#     print("(Enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == "q":
#         break

#     l_name = input("Last name: ")
#     if l_name == "q":
#         break

#     u_age = input("Enter your age (or press Enter to skip): ")
#     if u_age == "q":
#         break

#     if u_age.strip():
#         try:
#             u_age = int(u_age)
#         except ValueError:
#             print("Invalid age. Please enter age as a number.")
#             continue
#     else:
#         u_age = None

#     formatted_name = get_formatted_name(f_name, l_name, u_age)
#     print(f"\nHello, {formatted_name}")


def greet_someone(names):
    """Print a greeting for each user in a list."""

    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


name_list = ["Me", "Wewe"]
greet_someone(name_list)

# Taking an input, storing the name and returning a greeting

users = []


def greet_someone(names):
    """Print a greeting for each user in a list."""

    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


while True:
    name = input(
        "\nPlease enter your name (or 'q' at any time to quit or 'done' when done entering your name): "
    )

    if name == "q":
        break

    if name == "done":
        break

    users.append(name)

greet_someone(users)
