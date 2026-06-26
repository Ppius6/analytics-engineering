def factorial(x):

    # Base case
    # Prevents the function from calling itself forever.

    if x <= 1:
        print(f"Reached base case: factorial({x}) = 1")
        return 1

    # Recursive case
    # This function calls itself, but with a smaller number (n - 1)
    print(f"Calculating {x}! -> Waiting for {x} * factorial({x-1})")

    # Store the result of the recursive call in a variable
    # so we can print it before returning it
    sub_answer = factorial(x - 1)

    current_answer = x * sub_answer

    print(f"Resolving {x}! -> {x} * {sub_answer} = {current_answer}")

    return current_answer


final_result = factorial(4)
