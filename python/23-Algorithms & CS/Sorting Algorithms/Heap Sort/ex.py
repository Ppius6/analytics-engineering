def heapify(arr, n, i):

    # 'n' is the size of the heap we are currently looking at
    # 'i' is the index of the "manager" node we are currently checking

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if the left employee exists and is strictly greater than the manager
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if the right employee exists and is strictly greater than whoever is currently largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the manager (i) was NOT the largest, we must swap them with the largest employee
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Since the manager just sank down a level, we must recursively check
        # if they need to keep sinking further down the tree
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build the max heap
    # Start from the middle of the array and work backward to the front, calling heapify() on each node to build a perfect hierarchy.
    # (Math note: n//2 - 1 is the indext of the last node that has children)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    print(f"After phase 1 (Max Heap Built): {arr}")

    # Phase 2 - Extract and Sort
    # One by one, extract the largest element from the top and lock it at the end
    for i in range(n - 1, 0, -1):
        # Swap the CEO (index 0) with the current last available spot (index i)
        arr[i], arr[0] = arr[0], arr[i]

        # The new CEO at index 0 is probably weak. Let them skink to their correct position among the remaining unsorted elements (size 'i')
        heapify(arr, i, 0)

    return arr


my_l = [4, 20, 49, 2, 1]

sorted_l = heap_sort(my_l)

print(f"\nFinal Sorted list: {sorted_l}")
