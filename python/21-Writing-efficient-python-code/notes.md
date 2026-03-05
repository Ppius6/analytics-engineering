# Writing Efficient Python Code

Efficient Python code is not just about making your code run faster, but also about writing code that is more readable and maintainable. More often, we are guided by the principles outlined in the `Zen of Python` which emphasizes readability and simplicity. 

These principles are:

```
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
```

Writing efficient code often involves using built-in functions and libraries, which are optimized for performance. For example, using list comprehensions instead of traditional loops can often lead to more concise and faster code.

```python

# Using a for loop
squares = []
for x in range(10):
    squares.append(x**2)

# Using a list comprehension
squares = [x**2 for x in range(10)]
```

In addition to using built-in functions, it's also important to consider the algorithmic complexity of your code. Choosing the right data structures and algorithms can significantly improve the performance of your code.

For example, if you need to check for the presence of an item in a list, using a set can be more efficient than using a list, as sets have O(1) average time complexity for lookups, while lists have O(n) time complexity.

```python
# Using a list
my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
    print("Found")

# Using a set
my_set = {1, 2, 3, 4, 5}
if 3 in my_set:
    print("Found")
```

## Examining Running Time

We can time our code to measure how long it takes to execute. This helps in identifying bottlenecks and optimizing performance. 

The `%timeit` magic command can be used to time a single line of code, while the `%%timeit` magic command can be used to time a block of code.

In a script or a Jupyter notebook, you can use the `time` module to measure the execution time of your code. When using a terminal, we can use the `timeit.timeit()` function to time a block of code.

```python
# Timing a single line of code
%timeit ls = [x**2 for x in range(10)]

# Timing a block of code
%%timeit
squares = []
for x in range(10):
    squares.append(x**2)
```

We can specify the number of runs/loops to execute the code using `-r` and `-n` options with `%timeit`. By default, it runs the code 7 times and takes the best result.

```python

# Timing with specific number of runs and loops
%timeit -r 5 -n1000 ls = [x**2 for x in range(10)]

```

To save the output, we can use the `-o` option with `%timeit`, which returns a `TimeitResult` object that contains the timing results.

```python

times = %timeit -o ls = [x**2 for x in range(10)]

print(times)

```

## Code Profiling

Code profiling is a technique used to analyze the performance of a program by measuring the time spent on each function or line of code. It offers detailed statistics on frequency and duration of function calls, which helps in identifying bottlenecks and optimizing performance.

The package used is `line_profiler`, which can be installed using pip:

```bash

pip install line_profiler

```

We could use `%timeit` to time a block of code, but it does not provide detailed information about which lines of code are taking the most time. Also, `%timeit` runs the code multiple times to get an average time and the standard deviation, which can be useful for getting a general idea of the performance of the code, but it does not provide detailed information about which lines of code are taking the most time.

To use `line_profiler`, we first load the extension in a Jupyter notebook:

```python

%load_ext line_profiler

```

Then, we use the magic command `%lprun` for line by line profiling. We can specify the function we want to profile and the code block we want to execute.

```python

%load_ext line_profiler

%lprun -f convert_units convert_units(heroes, hts, wts)

```

This will give us a detailed report of the time taken by each line of code in the `convert_units` function, which can help us identify any bottlenecks and optimize our code accordingly. The report will show the number of hits, time taken, and percentage of total time for each line of code in the function.

## Memory Profiling

Memory profiling is a technique used to analyze the memory usage of a program. It helps in identifying memory leaks and optimizing memory usage. The package used for memory profiling is `memory_profiler`, which can be installed using pip:

```bash
pip install memory_profiler

```

To use `memory_profiler`, we first load the extension in a Jupyter notebook:

```python

%load_ext memory_profiler

```

Then, we have to load the function we want to profile and then execute the code block we want to profile.

```python

%load_ext memory_profiler

from my_module import my_function

%mprun -f my_function my_function(a, b, c)

```

