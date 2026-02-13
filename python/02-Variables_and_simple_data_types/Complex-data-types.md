# Complex data types

## Named Tuples

`Named tuples` are immutable objects that give each position in a tuple a meaningful name. They are like lightweight classes without methods.

```python

from collections import namedtuple

# Define a namedtuple
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create instances
person1 = Person('Alice', 30, 'New York')
person2 = Person(name='Bob', age=25, city='London')

# Access by attribute name (cleaner than index)
print(person1.name)  # 'Alice'
print(person1[0])    # Also works: 'Alice'

# Iterate
for value in person1:
    print(value)

# Immutable - cannot modify
# person1.name = 'Charlie'  # ❌ AttributeError
```

We can use them when we need a simple, immutable data structure with named fields. They are great for returning multiple values from functions or lightweight data containers.

## Data Classes

`Data classes` are mutable classes that automatically generate special methods like `__init__`, `__repr__`, and `__eq__`. They are more feature-rich than namedtuples.

```python

from dataclasses import dataclass, field
from typing import List

@dataclass
class Person:
    name: str
    age: int
    city: str = "Unknown" # Default value
    hobbies: List(str) = field(default_factory = List)

# Create instance
person = Person('Alice', 30)
print(person)  # Person(name='Alice', age=30, city='Unknown', hobbies=[])

# Mutable - can modify
person.age = 31
person.hobbies.append('reading')

# Automatic __repr__ for nice printing
print(person)  # Person(name='Alice', age=31, city='London', hobbies=['reading'])

# Automatic __eq__ for comparison
person2 = Person('Alice', 31, 'London', ['reading'])
print(person == person2)  # True (compares all fields)

```

We use them when we need mutable objects with type hints, automatic methods, and clean initialization. They are better for complex data structures than namedtuples.

## Counter

`Counter` counts hashable objects and stores results in a dictionary-like format. It is designed specifically for frequency counting.

```python

from collections import Counter

# Count characters in a string
text = "hello world"
char_count = Counter(text)
print(char_count) # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ...})

# Count elements in a list
fruits = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
fruit_count = Counter(fruits)
print(fruit_count)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Most common elements
print(fruit_count.most_common(2))  # [('apple', 3), ('banana', 2)]
print(fruit_count.most_common(1)[0][0])  # 'apple'

# Total count
print(sum(fruit_count.values()))  # 6

# Access count (returns 0 for missing keys, unlike dict)
print(fruit_count['orange'])  # 0 (doesn't raise KeyError)

# Update counts
fruit_count.update(['apple', 'date'])
print(fruit_count)  # Counter({'apple': 4, 'banana': 2, 'cherry': 1, 'date': 1})

# Arithmetic operations
counter1 = Counter(['a', 'b', 'a'])  # Counter({'a': 2, 'b': 1})
counter2 = Counter(['a', 'c'])       # Counter({'a': 1, 'c': 1})
print(counter1 + counter2)  # Counter({'a': 3, 'b': 1, 'c': 1})
print(counter1 - counter2)  # Counter({'a': 1, 'b': 1}) (removes common items)

```

We use `Counter` when we need to count frequencies of items, much more convenient than manually using a regular dictionary.

## DefaultDict

`DefaultDict` is a dictionary that returns a default value for missing keys instead of raising a `KeyError`

```python

from collections import defaultdict

# Regular dict - raises KeyError
regular_dict = {}
# print(regular_dict['missing'])  # ❌ KeyError

# defaultdict with int (default value is 0)
int_dict = defaultdict(int)
print(int_dict['missing'])  # 0 (no error)

# defaultdict with list (default value is [])
list_dict = defaultdict(list)
list_dict['fruits'].append('apple')
list_dict['fruits'].append('banana')
list_dict['vegetables'].append('carrot')
print(list_dict)  # defaultdict(<class 'list'>, {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']})

# defaultdict with set (default value is set())
set_dict = defaultdict(set)
set_dict['colors'].add('red')
set_dict['colors'].add('blue')
print(set_dict)  # defaultdict(<class 'set'>, {'colors': {'red', 'blue'}})

# Custom default factory with lambda
default_dict = defaultdict(lambda: 'N/A')
print(default_dict['unknown'])  # 'N/A'

# Practical example: grouping items
data = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot')]
groups = defaultdict(list)
for category, item in data:
    groups[category].append(item)
print(groups)  # defaultdict(<class 'list'>, {'fruit': ['apple', 'banana'], 'vegetable': ['carrot']})

```

We can use them when we need a dictionary that provides default values automatically. It eliminates the need for `.get()` calls or checking if a key exists.

```python

from collections import namedtuple, Counter, defaultdict
from dataclasses import dataclass

# Track user visits
@dataclass
class User:
    user_id: int
    name: str

Visit = namedtuple('Visit', ['user_id', 'page', 'timestamp'])

visits = [
    Visit(1, '/home', '2024-01-01'),
    Visit(2, '/about', '2024-01-01'),
    Visit(1, '/products', '2024-01-02'),
    Visit(1, '/home', '2024-01-02'),
]

# Count page visits
page_visits = Counter(visit.page for visit in visits)
print(page_visits)

# Group visits by user
user_visits = defaultdict(list)
for visit in visits:
    user_visits[visit.user_id].append(visit)
print(user_visits[1])

```

A real-world example;

Without the above data structures;

```python

# Raw lists and tuples - confusing!
orders = [
    [101, 'Alice', 'pending', 1500, '2024-01-01'],
    [102, 'Bob', 'completed', 2500, '2024-01-02'],
    [103, 'Charlie', 'pending', 800, '2024-01-01'],
]

# Which index is what? Easy to make mistakes
for order in orders:
    print(f"Order {order[0]} by {order[1]}: ${order[3]}")  # Works, but unclear
    
# Bug waiting to happen
def process_orders(orders):
    for order in orders:
        if order[2] == 'completed':
            charge_customer(order[1], order[3])  # Mixing up indices = bugs!

```

with `NamedTuples` (clear & immutable):

```python

from collections import namedtuple

Order = namedtuple('Order', ['order_id', 'customer', 'status', 'amount', 'date'])

orders = [
    Order(101, 'Alice', 'pending', 1500, '2024-01-01'),
    Order(102, 'Bob', 'completed', 2500, '2024-01-02'),
    Order(103, 'Charlie', 'pending', 800, '2024-01-01'),
]

# Crystal clear what each field is
for order in orders:
    print(f"Order {order.order_id} by {order.customer}: ${order.amount}")

# No confusion - self-documenting
def process_orders(orders):
    for order in orders:
        if order.status == 'completed':
            charge_customer(order.customer, order.amount)  # Obvious!

# Immutable - good for data that shouldn't change
# order.status = 'shipped'  # ❌ AttributeError - protection against accidental changes

```

With `DataClasses`, which are mutable and flexible;

```python

from dataclasses import dataclass
from datetime import datetime

@dataclass
class Order:
    order_id: int
    customer: str
    status: str
    amount: float
    date: str
    
    # Add behavior/methods
    def is_completed(self):
        return self.status == 'completed'
    
    def apply_discount(self, discount_percent):
        self.amount *= (1 - discount_percent / 100)

orders = [
    Order(101, 'Alice', 'pending', 1500, '2024-01-01'),
    Order(102, 'Bob', 'completed', 2500, '2024-01-02'),
    Order(103, 'Charlie', 'pending', 800, '2024-01-01'),
]

# Use methods for business logic
for order in orders:
    if order.is_completed():
        charge_customer(order.customer, order.amount)

# Mutable - can update orders
order = orders[0]
order.status = 'shipped'
order.apply_discount(10)  # 10% discount
print(order)  # Order(order_id=101, customer='Alice', status='shipped', amount=1350.0, date='2024-01-01')

```