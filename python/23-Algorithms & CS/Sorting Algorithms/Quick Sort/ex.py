def quick_sort(arr):

    # If it is an empty list, or a list with 1 item, it is already sorted
    if len(arr) <= 1:
        return arr

    # Picking a pivot
    # We will grab the last item in the list
    pivot = arr.pop()

    # Partition into two piles
    left_pile = []
    right_pile = []

    for item in arr:
        if item <= pivot:
            left_pile.append(item)
        else:
            right_pile.append(item)

    print(f"Pivot {pivot} | Left: {left_pile} | Right: {right_pile}")

    sorted_left = quick_sort(left_pile)
    sorted_right = quick_sort(right_pile)

    return sorted_left + [pivot] + sorted_right


my_l = [8, 3, 1, 7, 0, 10, 2]

sorted_my_l = quick_sort(my_l)

print(f"Final sorted list {sorted_my_l}")
