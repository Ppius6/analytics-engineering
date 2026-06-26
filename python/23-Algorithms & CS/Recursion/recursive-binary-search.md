# Divide and Conquer: Recursive Binary Search

`Divide and Conquer` is a specific type of recursion that involves breaking a problem into smaller subproblems, solving each subproblem recursively, and then combining the solutions to solve the original problem. One of the most common examples of this technique is the `binary search` algorithm.

For a recursive binary search, our function needs to keep track of the `low` and `high` pointers.

A recursive binary search has two ways it can stop:

- `Success Base Case`: The element is found, and we return the index of the element.
- `Failure Base Case`: The element is not found, and we return -1.

## The Recursive Cases

If we have not hit a base case, the function calls itself, but it changes the arguments to permanently discard half the list:

- If the target is smaller than the middle: `return binary_search(left_half)`
- If the target is larger than the middle: `return binary_search(right_half)`

## The Worked Example (Step-by-Step Trace)

Let us trace searching for the target 8 in the list [2, 5, 8, 12, 16].

- Initial Call: search(low=0, high=4)

    Calculate mid: $(0 + 4) // 2 = 2$.

    The value at index 2 is 8.

    Wait! $8 == 8$. We instantly hit our Success Base Case on the first try. Return index 2.

Let's try a harder one. Let's search for 16 in the same list [2, 5, 8, 12, 16].

- Call 1: search(low=0, high=4)

    Mid index is 2 (Value: 8).

    16 > 8. The target is in the right half.

    Recursive Call: Trigger search(low=3, high=4) and pause Call 1.

- Call 2: search(low=3, high=4)

    Calculate mid: $(3 + 4) // 2 = 3$.

    Mid index is 3 (Value: 12).

    16 > 12. The target is in the right half again.

    Recursive Call: Trigger search(low=4, high=4) and pause Call 2.

- Call 3: search(low=4, high=4)

    Calculate mid: $(4 + 4) // 2 = 4$.

    Mid index is 4 (Value: 16).

    16 == 16. Success Base Case!

    Return index 4 back to Call 2, which returns it to Call 1, which returns it to the user.