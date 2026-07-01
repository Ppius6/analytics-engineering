
# Bubble Sort

It is one of the simplest sorting algorithms that works by repeatedly stepping through the list to be sorted, comparing each pair of adjacent items and swapping them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which means the list is sorted. The algorithm gets its name because smaller elements "bubble" to the top of the list.

## Concept

Imagine a conveyor belt inspector looking at two items at a time. The algorithm steps through the list, comparing adjacent pairs of numbers. If the number on the left is larger than the number on the right, it __swaps__ them. 

It does this repeatedly from left to right. Because of this swapping action, the absolute largest numbers are quickly pushed all the way to the right side of the list. They "bubble" to the top, hence the name "Bubble Sort".

## An Number Example

Let us sort the following list of numbers using `Bubble Sort`:

```
[4, 2, 7, 1, 3]
```

Pass 1 (Bubbling the absolute largest number):

1. Compare 4 and 2: 4 > 2, so swap them. The list becomes: [2, 4, 7, 1, 3]

2. Compare 4 and 7: 4 < 7, so do not swap. The list remains: [2, 4, 7, 1, 3]

3. Compare 7 and 1: 7 > 1, so swap them. The list becomes: [2, 4, 1, 7, 3]

4. Compare 7 and 3: 7 > 3, so swap them. The list becomes: [2, 4, 1, 3, 7]

Pass 2 (Bubbling the second largest number):

1. Compare 2 and 4: 2 < 4, so do not swap. The list remains: [2, 4, 1, 3, 7]

2. Compare 4 and 1: 4 > 1, so swap them. The list becomes: [2, 1, 4, 3, 7]

3. Compare 4 and 3: 4 > 3, so swap them. The list becomes: [2, 1, 3, 4, 7]

Pass 3 (Bubbling the third largest number):

1. Compare 2 and 1: 2 > 1, so swap them. The list becomes: [1, 2, 3, 4, 7]

2. Compare 2 and 3: 2 < 3, so do not swap. The list remains: [1, 2, 3, 4, 7]

Pass 4 (Bubbling the fourth largest number):

1. Compare 1 and 2: 1 < 2, so do not swap. The list remains: [1, 2, 3, 4, 7]

The list is now sorted, and no further passes are needed and the last three numbers are already locked in place. The final sorted list is:

```
[1, 2, 3, 4, 7]
```

