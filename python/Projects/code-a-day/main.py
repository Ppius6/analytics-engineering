# 19-06-2026
# Finding the gcd


def find_gcd(a, b):

    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


result = find_gcd(48, 18)
print(f"The GCD of 48 and 18 is {result}")

# 19-06-2026
# Bubble sort algorithm


def bubble_sort(arr):
    # Get the total number of items in the list
    n = len(arr)

    # Outer loop: Go through the list 'n' times
    for i in range(n):

        # Inner loop: Look at adjacent items
        # We subtract 'i' because the last 'i' elements are already sorted
        # We subtract 1 to avoid checking past the end of the list
        for j in range(0, n - i - 1):

            # If the left item is greater than the right item ...
            if arr[j] > arr[j + 1]:

                # ... Swap them
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


list_1 = [3, 2, 7, 9]

sorted_list = bubble_sort(list_1)
print(f"Sorted list: {sorted_list}")

# 20-06-2026
