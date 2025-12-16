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

Here, we expand writing tests for classes.

### A Variety of Assertions

So far, we have worked with just one kind of assertion: a claim that a string has a specific value. 

When writing a test, we can make any claim that can be expressed as a conditional statement. If the condition is `True` as expected, our assumption about how that part of our program behaves would be confirmed; we can be confident that no errors exist. 

If the condition we assume is `True` is actually `False`, the test will fail and we will know there is an issue to resolve. 

The following table shows the commonly used assertion statements in tests.

| Assertion                    | Claim                                       |
|------------------------------|---------------------------------------------|
| `assert x == y`              | Assert that two values are equal            |
| `assert x != y`              | Assert that two values are not equal        |
| `assert x`                   | Assert that x evaluates to True             |
| `assert x > y`               | Assert that x is greater than y             |
| `assert x < y`               | Assert that x is less than y                |
| `assert x >= y`              | Assert that x is greater than or equal to y |
| `assert x <= y`              | Assert that x is less than or equal to y    |
| `assert not x`               | Assert that x evaluates to False            |
| `assert element in list`     | Assert that an element is in a list         |
| `assert element not in list` | Assert that an element is not in a list     |

### A Class to Test

Testing a class is similar to testing a function since much of the work involves testing the behavior of the methods in the class. However, there are a few differences. 

Consider a class that helps administer anonymous surveys:

```python
class AnonymousSurvey:
    """
    Collect anonymous answers to a survey question
    """

    def __init__(self, question):
        """
        Store a question, and prepare to store responses
        """
        self.question = question
        self.responses = []

    def show_question(self):
        """
        Show the survey question
        """
        print(self.question)

    def store_response(self, new_response):
        """
        Store a single response to the survey
        """
        self.responses.append(new_response)

    def show_results(self):
        """
        Show all the responses that have been given
        """
        print("Survey results: ")
        for response in self.responses:
            print(f"- {response}")
```

To create an instance from this class, all we have to provide is a question. Once we have an instance representing a particular survey, we display the question with `show_question()`, store a response using `store_response()` and show results with `show_results()`.

```python
from survey import AnonymousSurvey

# Define a question, and make a survey
question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question
language_survey.show_question()
print("Enter 'q' at any time to quit. \n")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# Show the survey results
print("\n Thank you to everyone who participated in the survey!")
language_survey.show_results()
```

Upon running the program above, we get the results:

```
What language did you first learn to speak?
Enter 'q' at any time to quit. 

Language: English
Language: Swahili
Language: Kimeru
Language: q

 Thank you to everyone who participated in the survey!
Survey results: 
- English
- Swahili
- Kimeru
```

If we sought to improve our current program, we could allow for more responses by writing a method to list only unique responses and to report how many times each response was given, or we could even write another class to manage non-anonymous surveys.

Implementing such changes would risk affecting the current behavior of the class. It is possible that while trying to allow each user to enter multiple responses, we could accidentally change how single responses are handled. 

To ensure we do not break existing behavior as we develop this module, we can write tests for the class.

### Testing the AnonymousSurvey class

The following test verifies a single response to the survey question:

```python
from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses
```

After running our test, we get the following results:

```python
piusm@pius-home:~/dev-projects/analytics-engineering/python/11-testing_your_code/practice$ pytest
================================= test session starts ===================================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0
rootdir: /home/piusm/dev-projects/analytics-engineering/python/11-testing_your_code/practice
collected 1 item
                                                                                                                                                              

test_survey.py .                                                                      [100%]
=================================== 1 passed in 0.01s ====================================
```

The test passed and we can then proceed to test if the function can store more than one response. 

```python
from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses():
    """Test that three individual responses are stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['Ennglish', 'Swahili', 'Kimeru']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
```

When we run the test file again, both tests pass:

```python
piusm@pius-home:~/dev-projects/analytics-engineering/python/11-testing_your_code/practice$ pytest
================================== test session starts ===================================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0
rootdir: /home/piusm/dev-projects/analytics-engineering/python/11-testing_your_code/practice
collected 2 items        

test_survey.py .                                                                   [100%]

==================================== 2 passed in 0.01s ====================================
piusm@pius-home:~/dev-projects/analytics-engineering/python/11-testing_your_code/practice$ 
```

However, as these tests are repetitive, we can use another feature of `pytest` to make them more efficient.

### Using Fixtures

While we created a new instance of `AnonymousSurvey` in each test function, in a real-world project, this would be problematic.

In testing, a `fixture` helps set up a test environment. Often this means creating a resource that is used by more than one test. We create a fixture in `pytest` by writing a function with the decorator `@pytest.fixture`. A `decorator` is a directive placed just before a function definition; Python applies this directive to the function before it runs, to alter how the function code behaves. 

```python
import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """
    A survey that will be available to all test functions
    """
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response("English")
    assert "English" in language_survey.responses


def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ["Ennglish", "Swahili", "Kimeru"]
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
```

We now add a decorator that is defined in `pytest`. We apply the `@pytest.fixture` decorator to the new function `language_survey()` which builds an `AnonymousSurvey` object and returns the new survey.

The updated test functions now have the parameter `language_survey`. When a parameter in a test function matches the name of a function with the `@pytest.fixture` decorator, the fixture will be run automatically and the return value will be passed to the test function. 

In this example, the function `language_survey()` supplies both `test_store_single_response()` and `test_store_three_responses()` with a `language_survey` instance. 

Upon running the test file again, the tests will still pass.