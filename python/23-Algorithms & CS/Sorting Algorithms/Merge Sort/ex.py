def merge_sort(arr):

    # Base case
    # If the list is 1 item or empty, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle value and slice the array into two halves
    mid = len(arr) // 2

    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively chop the left and right halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)


def merge(left, right):
    merged_result = []

    i = 0
    j = 0

    # Compare the items at the front of both lists
    # Append the smaller one to our result list

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_result.append(left[i])
            i += 1
        else:
            merged_result.append(right[j])
            j += 1

    # If one list empties out before the other,
    # grab whatever is left in the remaining list and attach it to the end
    merged_result.extend(left[i:])
    merged_result.extend(right[j:])

    return merged_result


my_list = [38, 27, 43, 3, 9, 82, 10, 12, 12.5]

sorted_list = merge_sort(my_list)

print(f"Sorted list: {sorted_list}")
