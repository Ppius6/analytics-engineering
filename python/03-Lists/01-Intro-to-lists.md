# Lists

## Introducing Lists

Lists are quite important as they allow us to store sets of information in one place, whether you have just a few items or millions of items. Lists are quite powerful and tie together many important concepts in programming.

A `list` is a collection of items in a particular order. For example, you can make a list that includes the letters of the alphabet, the digits from 0 to 9, or the names of all the people in your family. 

As lists contain more than one element, it is a good idea to make the name of the list plural. For example, if you have a list of names, you can call it `names` or `family_members`.

In Python, square brackets `[]` indicate a list, and individual elements in the list are separated by commas. For example:

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
names = ['Mutuma', 'Kimathi', 'Wambua', 'Muthoni']

print(bicycles) # Output: ['trek', 'cannondale', 'redline', 'specialized']
print(names) # Output: ['Mutuma', 'Kimathi', 'Wambua', 'Muthoni']
```

As this may not be the output you want the users to see, let us understand how to access individual elements in a list!

### Accessing Elements in a List

Lists are ordered collections, so you can access any element in a list by telling Python the position, or `index`, of the desired item. 

To access an element in a list, write the name of the list followed by the index of the items enclosed in square brackets. 

Remember that Python uses zero-based indexing, meaning the first item in the list has an index of 0, the second item has an index of 1, and so on. Alternatively, you can also use negative indexing to access elements from the end of the list, where -1 refers to the last item, -2 to the second last, and so forth.

For example, to access the first item in the `bicycles` list:

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])  # Output: 'trek'
```

### Using individual elements from a List

You can use individual values from a list just as you would any other variable. For example, you can use f-strings to create a message based on a value from a list:

```python
cities = ['Nairobi', 'Mombasa', 'Kisumu', 'Nakuru', 'Eldoret']
message = f"Out of Kenya's cities, I have been to {cities[0]}, {cities[1]}, {cities[2]}, and {cities[3]}."
print(message) # Output: Out of Kenya's cities, I have been to Nairobi, Mombasa, Kisumu, and Nakuru.

message2 = f"Out of Kenya's cities, I have been to {cities[:4]}."
print(message2) # Output: Out of Kenya's cities, I have been to ['Nairobi', 'Mombasa', 'Kisumu', 'Nakuru'].
```

## Modifying, Adding, and Removing Elements

Mosts lists we will create are dynamic, meaning we will build a list and then add or remove elements from it as our program runs its course. For example, we can create a game in which a player has to shoot aliens our of the sky. We could store the initial set of aliens in a list, and then remove an alien from the list each time one is shot down. Each time a new alien appears on the screen, we can add it to the list. Our list of aliens will change as the game progresses.

### Modifying Elements in a List

We can modify elements just as the same way we can access an element in a list. To modify an element, we can use the name of the list followed by the index of the element we want to change, and then assign a new value to that position in the list.

With the `bicycles` list, we can change the first element from `'trek'` to `'giant'` like this:

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles[0] = 'giant'
print(bicycles)  # Output: ['giant', 'cannondale', 'redline', 'specialized']
```

### Adding Elements to a List

You may want to add a new element to a list for many reasons. For example, you might want to make new aliens appear in a game, add new data to a visualization, or add new registered users to a website you have built.

#### Appending Elements to the End of a list

We can add elements to a list. For example, we may want to add a new bicycle to our `bicycles` list. We can use the `append()` method to add an element to the end of the list:

```python
bicycles = ['giant', 'cannondale', 'redline', 'specialized']
bicycles.append('trek')
print(bicycles)  # Output: ['giant', 'cannondale', 'redline', 'specialized', 'trek']
```

We can also start with an empty list and then add items to the list using a series of `append()` calls. Using an empty list, let us for instance add sample countries to the list:

```python
countries = []
countries.append('Kenya')
countries.append('Uganda')
countries.append('Zambia')
countries.append('Rwanda')
```

Note that when using `append()`, we usually append an element at the end of the list.

#### Inserting Elements into a List

We can also add a new element at any position in your list by using the `insert()` method. We can do this by specifying the index of the new element and the value of the new item:

```python
countries = ["Kenya", "Uganda", "Rwanda"]
countries.insert(0, "Burundi")
print(countries) # Output: ["Burundi", "Kenya", "Uganda", "Rwanda"]
```

In the above example, we insert the value "Burundi" at the beginning of the list. The method `insert()` opens a space at position 0 and stores the new value at that location

```python
# Output: ["Burundi", "Kenya", "Uganda", "Rwanda"]
```

### Removing Elements from a List

You would want to remove an item or a set of items from a list. For example, when a user decides to cancel their account on a web application you created, you will want to remove that user from the list of active users. You can remove an item according to its position in the list or according to its value.

#### Removing an Item Using the del Statement

If you know the position of the item you want to remove from a list, the `del` statement can come in handy:

```python
countries = ["Burundi", "Kenya", "Uganda", "Rwanda"]
del countries[2]
print(countries) # Output: ["Burundi", "Kenya", "Rwanda"]
```

#### Removing an Item Using the pop() Method

At times, you may want to use the value of an item after you remove it from a list. 

For example, you might want to get the x and y position of an alien that was just shot down, so you can draw an explosion at that position. In a web application, you might want to remove a user from a list of active members and then add that user to a list of inactive members.

The `pop()` method removes the last item in a list, but it lets you work with that item after removing it. The term `pop` comes from thinking of a list as a stack of items and popping one item off the top of the stack. In this analogy, the top of a stack corresponds to the end of a list.

Let us pop a country from the list of motorcycles

```python
countries = ["Burundi", "Kenya", "Uganda", "Rwanda"]
popped_country = countries.pop()
print(countries) # Output: ['Burundi', 'Kenya', 'Uganda']
print(popped_country) # Output: ["Rwanda"]
```

So, how might this `pop()` method be useful? If the countries in the list are stored in chronological order, based on when we added them, or gained independence, we can use the `pop()` method to print a statement to get the result of which country gained independece last:

```python
countries = ["Burundi", "Kenya", "Uganda", "Rwanda"]
last_country = countries.pop()
print(countries) # Output: ['Burundi', 'Kenya', 'Uganda']
print(last_country) # Output: ["Rwanda"]
print(f"The last country to gain independence was {last_country.title()}.")
```

#### Popping Items from Any Position in a List

We can also use `pop()` to remove an item from any position in a list by just including the index of the item we want to remove.

```python
countries = ["Burundi", "Kenya", "Uganda", "Rwanda"]
first_country = countries.pop(0)
print(countries) # Output: ['Kenya', 'Uganda', 'Rwanda']
print(first_country) # Output: ['Burundi']
```

#### Removing an Item by Value

We may not know the position of the value we want to remove from a list. In this case, we can use the `remove()` method.

```python
countries = ["Burundi", "Kenya", "Uganda", "Rwanda"]
countries.remove('Kenya')
print(countries) # Output: ['Burundi', 'Uganda', 'Rwanda']
```

## Organizing a List