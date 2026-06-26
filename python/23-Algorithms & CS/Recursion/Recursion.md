# Recursion

Recursion is a programming technique where a function calls itself directly or indirectly in order to solve a problem. It works by breaking a complex problem down into smaller, more manageable subproblems of the same type. Each recursive call should bring the problem closer to a base case, which is a simple instance of the problem that can be solved without further recursion.

There are two distinct parts of a recursive function:
1. **Base Case**: This is the condition under which the recursion stops. It prevents infinite recursion and allows the function to return a value without making further recursive calls.
2. **Recursive Case**: This is where the function calls itself with modified arguments, moving closer to the base case.

## The Problem Statement

Write a recursive function to calculate the Factorial of a number.

In mathematics, the factorial of a non-negative integer $n$ (written as $n!$) is the product of all positive integers less than or equal to $n$.
For example: $4! = 4 \times 3 \times 2 \times 1 = 24$.

The Mathematical Concept

We can rewrite the factorial formula to reference itself:


$$n! = n \times (n-1)!$$

Recursive Case: To find $4!$, you do $4 \times 3!$. But wait, what is $3!$? It's $3 \times 2!$.

Base Case: We stop when we reach $1!$, because mathematically, $1! = 1$.

### The Worked Example (Step-by-Step Trace)

Let’s manually trace what happens in the computer's memory (the "Call Stack") when we ask it to calculate factorial(4).

#### Part 1: Winding down the stack (The Calls)

 - Call 1: factorial(4)
 
    - Is 4 equal to 1? No.
    
        Return: 4 * factorial(3). (The computer pauses this calculation and opens a new function for factorial 3).

- Call 2: factorial(3)
 
    - Is 3 equal to 1? No.
    
        Return: 3 * factorial(2). (Pauses again).

- Call 3: factorial(2)

    - Is 2 equal to 1? No.
    
        Return: 2 * factorial(1). (Pauses again).

- Call 4: factorial(1)

    - Is 1 equal to 1? Yes.
    
        Return: 1. (We finally hit the Base Case! No more pausing).

#### Part 2: Winding up the stack (The Returns)

Now the computer goes backward, filling in the blanks for all those paused calculations.

- Step 5: Resolve Call 3: factorial(2) was waiting for 2 * factorial(1). It now knows factorial(1) is 1.

    $2 \times 1 = 2$. It passes 2 up the chain.
    
- Step 6: Resolve Call 2: factorial(3) was waiting for 3 * factorial(2). It now knows factorial(2) is 2.

    $3 \times 2 = 6$. It passes 6 up the chain.

- Step 7: Resolve Call 1: factorial(4) was waiting for 4 * factorial(3). It now knows factorial(3) is 6.

    $4 \times 6 = 24$.

Final Output: The final answer is 24.