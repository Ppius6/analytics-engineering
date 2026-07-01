
# Heap Sort

`Heap Sort` is a highly efficience sorting algorithm that relies on a special data structure called a `Binary Heap`. It is excellent for memory management since it sorts the array "in-place" (it does not need to create new left and right piles like Quick Sort or Merge Sort). 

However, it is important to understand the concepts of `Heaps` and `Heapify` before we can fully grasp how Heap Sort works.

Given a list of numbers, we can visualize it as a branching tree. Each number is a "node" in the tree, and each node can have up to two "children" (left and right). The `Heap` is a special kind of binary tree that satisfies the `Heap Property`. In a `Max Heap`, every parent node is greater than or equal to its children. Conversely, in a `Min Heap`, every parent node is less than or equal to its children.

Given a list `[A, B, C, D, E]` denoted by positions `[1, 2, 3, 4, 5]`, we should note that:

- If a node is at position `i`, its left child is at position `2 * i` and its right child is at position `2 * i + 1`.

For example, given the tree:

```
        A
       / \
      B    C
     / \   / \
    D   E  F   G
```

To check node `B` at position 2, we can find its left child `D` at position `2 * 2 = 4` and its right child `E` at position `2 * 2 + 1 = 5`. `D` and `E` positions are indeed 4 and 5, respectively. 

## Types of Heaps

### Max Heap

In a `Max Heap`, the parent node is always greater than or equal to its children. The largest element is always at the root of the tree.

### Min Heap

In a `Min Heap`, the parent node is always less than or equal to its children. The smallest element is always at the root of the tree.

## The Logical Concept

Imagine a strict corporate hierarchy where every manager must have a higher rank than their subordinates. This structure is called a `Max Heap`. In a Max Heap, the highest-ranking manager, or CEO in this case, is mathematically guaranteed to be the absolute largest number in the entire dataset.

Heap sort works in two distinct phases:

1. Phase 1 (Build the Heap):

    - Here, we rearrange the chaotic list so that it forms a perfect Max Heap Hierarchy. This is done by starting from the last non-leaf node and moving upwards, ensuring that each parent node is greater than its children.

2. Phase 2 (Sort the Heap):

    - Once we have a Max Heap, we can start sorting. The largest element (the CEO) is at the root of the heap. We swap it with the last element in the array and then reduce the size of the heap by one. After that, we "heapify" the root node to ensure that the Max Heap property is maintained. This process is repeated until all elements are sorted.

## The Math

How do we represent a branching tree using just a flat Python list? Using Math! If we are looking at a "manager" at index `i`, we can find their left and right subordinates (children) using the following formulas:

- Left Child Index: `2 * i + 1`
- Right Child Index: `2 * i + 2`

### An Example

We can sort the following list of numbers using Heap Sort:

```
[4, 10, 3, 5, 1]
```

1. Phase 1: Build the Max Heap

    - The computer looks at the array as a tree and "heapifies" it from the bottom up to ensure managers are bigger than employees.
    
    - 10 is larger than 4, 5, and 1. After heapifying, our array transforms into a valid Max Heap: [10, 5, 3, 4, 1].
    (Notice that the absolute maximum, 10, is now at index 0).

2. Phase 2: Extract and Sort

    - Swap: Swap the CEO (10) with the last item (1).

        List: [1, 5, 3, 4, 10]
        
    - The 10 is now locked! We ignore it for the rest of the algorithm.
    
    - Heapify: The new CEO 1 is smaller than its employees (5 and 3). It must sink. 5 is the largest employee, so it promotes 5 to CEO. 1 swaps with 5, and then 1 swaps with 4.
    
    - List: [5, 4, 3, 1, 10] (A valid Max Heap again for the remaining 4 items).
    
    - Swap: Swap the new CEO (5) with the last available spot (1).
    
        List: [1, 4, 3, 5, 10]

    - Heapify: The 1 sinks again. 4 rises to the top.
        
        List: [4, 1, 3, 5, 10]

    - Swap: Swap CEO 4 with the last available spot (3).
    
        List: [3, 1, 4, 5, 10]

    - Heapify: 3 is already larger than 1. No sinking needed.
    
    - Swap: Swap 3 with 1.
    
        Final List: [1, 3, 4, 5, 10]. Perfectly sorted!

