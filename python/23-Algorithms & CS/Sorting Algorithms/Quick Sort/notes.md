
# Quick Sort

It is often the fastest sorting algorithm in practice and is heavily used in real-world programming languages under the hood.

## Concept

Instead of chopping the list strictly in the middle, `Quick Sort` picks one number to act as a __Pivot__. Then, it organizes the rest of the list around that pivot. 

- Every number _smaller_ than the pivot is moved to its left.
- Every number _larger_ than the pivot is moved to its right.

At this point, the pivot is in its absolute final, correct, sorted position. The algorithm then recursively does the exact same thing to the left and right sublists until the entire list is sorted.

## Example

Let us sort this list of numbers using `Quick Sort`:

```
[8, 3, 1, 7, 0, 10, 2]
```

Pass 1:

1. Pick a pivot. Let us pick 3. 

2. Then, partition the rest. Compare the list to 3. 

    - Smaller than 3: [1, 0, 2]
    - Larger than 3: [8, 7, 10]

3. The current state is now: [1, 0, 2] + [3] + [8, 7, 10]

4. As it stands, pivot 3 is in its final position. Now, we recursively sort the left and right sublists.

Pass 2: Recursion on the left

1. Look at the left sublist: [1, 0, 2]. Pick a pivot. Let us pick 0.

2. Partition the rest. Compare the list to 0.

    - Smaller than 0: []
    - Larger than 0: [1, 2]

3. The current state is now: [] + [0] + [1, 2] with pivot 0 in its final position. Now, we recursively sort the left and right sublists.

Pass 3: Recursion on the right

1. Look at the right sublist: [1, 2]. Pick a pivot. Let us pick 1.

2. Partition the rest. Compare the list to 1.

    - Smaller than 1: []
    - Larger than 1: [2]

3. The current state is now: [] + [1] + [2] with pivot 1 in its final position. Now, we recursively sort the left and right sublists.

4. Look at the right sublist: [2]. Since it is a single item, it is already sorted. The recursion ends here.

Pass 4: Recursion on the right

1. Look at the right sublist: [8, 7, 10]. Pick a pivot. Let us pick 7.

2. Partition the rest. Compare the list to 7.

    - Smaller than 7: []
    - Larger than 7: [8, 10]

3. The current state is now: [] + [7] + [8, 10] with pivot 7 in its final position. Now, we recursively sort the left and right sublists.

4. Look at the right sublist: [8, 10]. Pick a pivot. Let us pick 8.

5. Partition the rest. Compare the list to 8.

    - Smaller than 8: []
    - Larger than 8: [10]

6. The current state is now: [] + [8] + [10] with pivot 8 in its final position. Now, we recursively sort the left and right sublists. [10] is a single item, so it is already sorted. The recursion ends here.

7. Final Merge: 

```
[0] + [1] + [2] + [3] + [7] + [8] + [10] which results in [0, 1, 2, 3, 7, 8, 10]
```

