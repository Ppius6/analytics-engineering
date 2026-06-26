
# Merge Sort

It operates on a simple premise of: __A list of 1 item is already sorted__.

Instead of trying to sort a masisve list all at once, like `Bubble Sort` does, `Merge Sort` uses recursion to brutally chop the list in half, over and over, until it is left with tiny lists of 1 item. Then, it looks at two tiny lists, compares their items, and merges them together into a sorted 2-item list. It repeats this merging process, building a larger and larger sorted lists, until the entire original list is put back together in sorted order.

## An Number Example

Let us sort the following list of numbers using `Merge Sort`:

```
[38, 27, 43, 3, 9, 82, 10]
```

Phase 1: The Divide

The computer blindly chops the lists in half until it hits the Base Case (lists of lenghth 1).

    - [38, 27, 43, 3, 9, 82, 10] is chopped into [38, 27, 43, 3] and [9, 82, 10]
    - [38, 27, 43, 3] is chopped into [38, 27] and [43, 3]
    - [38, 27] is chopped into [38] and [27] and the base case is hit.

Phase 2: The Conquer / Merge

Now, the computer stiches the pieces back together, sorting them as it merges them. 

    - Looking at [38] and [27], it compares the two numbers and puts them in order: [27, 38] as 27 is smaller than 38.

        - Merged: [27, 38]

    - Looking at [43] and [3], it compares the two numbers and puts them in order: [3, 43] as 3 is smaller than 43.

        - Merged: [3, 43]

    - Now, merging the two newly sorted lists: [27, 38], and [3, 43], 

        - It compares 27 and 3, and puts 3 first.
        - Then it compares 27 and 43, and puts 27 next.
        - Then it compares 38 and 43, and puts 38 next.
        - Finally, it adds the remaining number, 43.

        - Merged: [3, 27, 38, 43]
        
    - The other half of the original list, [9, 82, 10], is also merged in a similar fashion:

        - [9] and [82] are compared and merged into [9, 82].
        - Then [9, 82] is merged with [10]:

            - It compares 9 and 10, and puts 9 first.
            - Then it compares 82 and 10, and puts 10 next.
            - Finally, it adds the remaining number, 82.

            - Merged: [9, 10, 82] 

The result of the final merge is a fully sorted list:

```
[3, 9, 10, 27, 38, 43, 82]
```