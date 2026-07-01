RUN_SIZE = 4


def insertion_sort(arr, left, right):
    """Sorts a small chunk of the array (like sorting cards in your hand)"""
    for i in range(left + 1, right + 1):
        # Pick up the current card
        current_item = arr[i]
        j = i - 1

        # Keep shifting larger cards to the right to make room for our current card
        while j >= left and arr[j] > current_item:
            arr[j + 1] = arr[j]
            j -= 1

        # Put the card in its correct spot
        arr[j + 1] = current_item


def merge(arr, left, mid, right):
    left_copy = arr[left : mid + 1]
    right_copy = arr[mid + 1 : right + 1]

    i = 0
    j = 0
    k = left

    # Stitch them back together in order
    while i < len(left_copy) and j < len(right_copy):
        if left_copy[i] <= right_copy[j]:
            arr[k] = left_copy[i]
            i += 1

        else:
            arr[k] = right_copy[j]
            j += 1

        k += 1

    # Grab any leftovers
    while i < len(left_copy):
        arr[k] = left_copy[i]
        i += 1
        k += 1

    while j < len(right_copy):
        arr[k] = right_copy[j]
        j += 1
        k += 1


def tim_sort(arr):
    n = len(arr)

    # Sort individual small RUNS using Insertion Sort
    for i in range(0, n, RUN_SIZE):
        # Using min() just in case the final run is smaller than RUN_SIZE
        end = min(i + RUN_SIZE - 1, n - 1)
        insertion_sort(arr, i, end)
        print(f"Sorted run from index {i} to {end}: {arr[i:end+1]}")

    # Start Merging the runs together
    size = RUN_SIZE
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)

            # If there is actually a right half to merge with, merge
            if mid < right:
                merge(arr, left, mid, right)
                print(f"Merged chunks into: {arr[left:right+1]}")

        size *= 2  # Double the size of the chunks we are merging

    return arr


# Testing the algorithm
my_list = [5, 21, 7, 23, 19, 1, 3, 9, 12, 14, 2, 6]
print(f"Original: {my_list}\n")
final_sorted = tim_sort(my_list)
print(f"\nFinal: {final_sorted}")
