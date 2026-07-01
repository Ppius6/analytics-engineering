
# Tim Sort

It is a hybrid algorithm. It is the default sorting algorithm in Python when one calls the built-in `sorted()` function or the `.sort()` method on lists. 

Tim Sort is derived from merge sort and insertion sort. It is designed to perform well on many kinds of real-world data.

## How it works

Tim Sort recognizes that `Merge Sort` is great at merging lists, but terrible and slow at chopping the list into smaller pieces. On the other hand, `Insertion Sort` is great at chopping the list into smaller pieces, but terrible and slow at merging lists.

So, Tim Sort does both:

1. It divides the massive array into smaller blocks called "runs" (which are either already sorted or will be sorted using insertion sort - usually 32 or 64).

2. It sorts each small "Run" using insertion sort.

3. It takes the sorted runs and stitches them together using merge sort.

## Example

Let us sort the following list of numbers using `Tim Sort`:

```
[5, 21, 7, 23, 19, 1, 3, 9]
```

We will set our run size to 4 for this example.

Phase 1: Insertion Sort on Small Runs

1. The computer chops the list into runs of size 4:

    - [5, 21, 7, 23]

2. It uses Insertion sort to quickly organize this tiny chunk.

    - [5, 21, 7, 23] is sorted into [5, 7, 21, 23]

3. The computer slices the next 4 items: 

    - [19, 1, 3, 9]

4. It uses Insertion sort to quickly organize this tiny chunk.

    - [19, 1, 3, 9] is sorted into [1, 3, 9, 19]

The current array state is now:

```
[5, 7, 21, 23, 1, 3, 9, 19]
```

Phase 2: Merge Sort on Sorted Runs

Now, we use the classic Merge Sort algorithm to merge the two sorted runs together. The computer looks at Run 1 and Run 2. 

- It compares 5 and 1: 1 is smaller. 
- It compares 5 and 3: 3 is smaller.
- It compares 5 and 9: 5 is smaller.
- It compares 7 and 9: 7 is smaller.

The merging continues until both runs are empty. The final merged array is:

```
[1, 3, 5, 7, 9, 19, 21, 23]
```

By stopping the "chopping" phase early and sorting small chunks directly, Tim Sort saves the computer massive amounts of memory and recursive function calls!

