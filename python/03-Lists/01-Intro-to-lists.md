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

Remember that Python uses zero-based indexing, meaning the first item in the list has an index of 0, the second item has an index of 1, and so on.

For example, to access the first item in the `bicycles` list:

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])  # Output: 'trek'
```
