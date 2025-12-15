# Testing your Code

When we write a function or a class, we can also write tests for that code. Testing proves that our code works as it is supposed to in response to all kinds of input it is designed to receive.

We will learn how to use `pytest` to test our code. It is a collection of tools that will help us write our first tests quickly and simply while supporting our tests as they grow in complexity along with our projects.

## Installing pytest with pip

Most Python developers depend on `third-party packages`, which are developed outside the core Python language. 

However, we should not blindly trust every third-party package, but we also should not be put off by the fact that a lot of important functionality is implemnented through such packages.

`pip` is used to install third-party packages. This tool is regularly updated to address potential security issues. 

```python
python -m pip install --upgrade pip
```

`python -m pip` tells Python to run the module pip. `install --upgrade` tells pip to update a package that has already been installed. `pip`, the last part, specifies which third-party package should be updated.

We can always use `python -m pip install --upgrade package_name` to update any third-party package installed on our system.

`pytest` can be installed using `python -m pip install --user pytest`. Here we use the `--user` flag which tells Python to install this package for the current user only. 

## Testing a Function

We can test the following code:

```python
# name_function.py
def get_formatted_name(first, last):
    """
    Generate a neatly formatted full name
    """
    full_name = f"{first} {last}"
    return full_name.title()
```

To check our function works, we can make a program that uses this function.

```python
from name_function import get_formatted_name

print("Enter 'q' at any time to quit. ")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("\nPlease give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")

Output:
Enter 'q' at any time to quit. 

Please give me a first name: I
Please give me a last name: You
        Neatly formatted name: I You.

Please give me a first name: I
Please give me a last name: Me
        Neatly formatted name: I Me.

Please give me a first name: q
```

The result work as expected. 

However, assuming we modify our program's functionality and add a middle name, we would want to make sure that we do not break the way the function handles names that have only a first and last name.

`pytest` provides an automated way of testing our function, and the result will give us the confidence that the function will work when given the kinds of names we have written tests for.

### Unit Tests and Test Cases

One of the simplest kinds of test is a `unit test`. It verifies that one specific aspect of a function's behavior is correct. A `test case` is a collection of unit tests that together prove that a function behaves as it is supposed to, within the full range of situations you expect it to handle.

A good test case considers all the possible kinds of input a function could receive and includes tests to represent each of these situations. A test case with full coverage includes a full range of unit tests covering all the possible ways you can use a function.

### A Passing Test

With `pytest`, writing our first unit test is pretty straightforward. We will write a single test function. The test function will call the function we are testing, and make an assertion about the value that is returned. If our assertion is correct, the test will pass; if the assertion is incorrect, the test will fail.

```python
# test_name_function.py
from name_function import get_formatted_name

def test_first_last_name():
    """
    Do names like 'Janis Joplin' work?
    """
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
```

When defining the test function, we need to start with the word `test`, followed by an underscore. Any function that starts with `test_` will be discovered by `pytest`, and will be run as part of the testing process.

Also, test names should be longer and more descriptive than a typical function name. We will never call the function ourselves; `pytest` will find the function and run it for us. 

The `assert` function is a claim about a condition. Here, we are claiming that the value of `formatted_name` should be `'Janis Joplin'`

### Running a Test

When running this test, we will have `pytest` run the test file for us. To do this, we open a terminal window and navigate to the folder with the test file and enter the command `pytest`. The result should be as shown below.

```python
piusm@pius-home:~/dev-projects/analytics-engineering/python/11-testing_your_code$ pytest
======================== test session starts ================================================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0
rootdir: /home/piusm/dev-projects/analytics-engineering/python/11-testing_your_code
collected 1 item   

test_name_function.py .                                                                 [100%]
========================= 1 passed in 0.01s =================================================
```

The single dot after the name of the file tells us that a single test passed, and the 100% makes it clear that all of the tests have been run. 

The output indicates that the function `get_formatted_name()` will always work for names that have a first and last name, unless we modify the function. Upon modifying the main function, we can run the test again.

### A Failing Test

In our previous program:

```python
def get_formatted_name(first, middle, last):
    """
    Generate a neatly formatted full name
    """
    full_name = f"{first} {middle} {last}"
    return full_name.title()
```

This version should work for people with middle names, but when we test it, we see that we have broken the function for people with just a first and last name.

If we run `pytest`, we get:

```python
piusm@pius-home:~/dev-projects/analytics-engineering/python/11-testing_your_code/practice$ pytest
================================ test session starts ===================================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0
rootdir: /home/piusm/dev-projects/analytics-engineering/python/11-testing_your_code/practice
collected 1 item                                                                                                                                                                                                                                                                                                                                                                                                                                 

test_name_function.py F                                                                                                           [100%]
======================================== FAILURES =======================================
______________________________________________________________________________________________________________________________________________________________________________________________________________ test_first_last_name ______________________________________________________________________________________________________________________________________________________________________________________________________________

    def test_first_last_name():
        """
        Do names like 'Janis Joplin' work?
        """
>       formatted_name = get_formatted_name("janis", "joplin")
E       TypeError: get_formatted_name() missing 1 required positional argument: 'last'

test_name_function.py:8: TypeError
============================================================================================================================================================================================================ short test summary info ================================
FAILED test_name_function.py::test_first_last_name - TypeError: get_formatted_name() missing 1 required positional argument: 'last'
=============================================================================================================================================================================================================== 1 failed in 0.06s ===================================
piusm@pius-home:~/dev-projects/analytics-engineering/python/11-testing_your_code/practice$ 
```

From the result, we see that `test_first_last_name()` failed, with a specific indication on this line; `formatted_name = get_formatted_name("janis", "joplin")`. The `E` on the next line shows the actual error that caused the failure: a `TypeError` due to a missing required positional argument, `last`.

The most important information is repeated in a shorter summary at the end, so when we are running may tests, we can get a quick sense of which tests failed and why.

### Responding to a Failed Test

When a test fails, we do not change the test. If we do, our tests might pass, but any code that calls our function like the test does will suddenly stop working. Instead, we should fix the code that is causing the test to fail.

In this case `get_formatted_name()` used to require only two parameters: a first name and a last name. Now it requires a first name, a middle name, and a last name. The addition of the middle name paramneter broke the original behavior of `get_formatted_name()`. We could make the middle name optional which will now make tests for names without a middle name pass again, same as those with a middle name.

```python
def get_formatted_name(first, last, middle=''):
    """
    Generate a neatly formatted full name
    """
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
```

Running the above test works now for both kinds of names. 

```python
piusm@pius-home:~/dev-projects/analytics-engineering/python/11-testing_your_code/practice$ pytest
================================= test session starts ====================================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0
rootdir: /home/piusm/dev-projects/analytics-engineering/python/11-testing_your_code/practice
collected 1 item                                                       
test_name_function.py .                                                                  [100%]
================================== 1 passed in 0.01s ===========================================
piusm@pius-home:~/dev-projects/analytics-engineering/python/11-testing_your_code/practice$ 
```

### Adding New Tests

We could add another test for people who include a middle name.

```python
```python
# test_name_function.py
from name_function import get_formatted_name

def test_first_last_name():
    """
    Do names like 'Janis Joplin' work?
    """
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_last_middle_name():
    """
    Do names like 'Wolfgang Amadeus Mozart' work?
    """
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'
```

Upon running our updated test function, we expect it to pass:

```python
piusm@pius-home:~/dev-projects/analytics-engineering/python/11-testing_your_code/practice$ pytest
================================================================== test session starts =====================================================================

platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0
rootdir: /home/piusm/dev-projects/analytics-engineering/python/11-testing_your_code/practice
collected 2 items
                                                                                                                                                             
test_name_function.py ..                                                                                                                              [100%]

================================================================== 2 passed in 0.01s =======================================================================
piusm@pius-home:~/dev-projects/analytics-engineering/python/11-testing_your_code/practice$ 
```

The two dots indicate that the two tests passed, which is also clear from the last line of output

## Testing a Class

