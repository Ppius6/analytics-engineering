def recursive_binary_search(arr, target, low, high):

    # Failure base case
    # The search space has collapsed, and the target is not here
    if low > high:
        print(
            f"Base case reached: low ({low}) is greater than high ({high}). Target not found."
        )
        return -1

    # Calculate the middle index
    mid = (low + high) // 2
    mid_value = arr[mid]

    print(
        f"Searching indices {low} through {high}. Mid index is {mid} (Value: {mid_value})"
    )

    # Success base case
    if mid_value == target:
        print(f"-> Base case reached: Found target {target} at index {mid}!")
        return mid_value

    # Target is smaller
    elif target < mid_value:
        print(f"-> {target} < {mid_value}. Discarding right half. Recursing...")
        # The return keyworkd ensures the final answer bubbles all the way back up the stack
        return recursive_binary_search(arr, target, low, mid - 1)

    # Target is larger
    else:
        print(f"-> {target} > {mid_value}. Discarding left half. Recursing...")
        return recursive_binary_search(arr, target, mid + 1, high)


my_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_number = 72

print(f"Target list: {my_list}")
print(f"Looking for: {target_number}\n")

# To start the recursion, we must provide the initial low (0) and high (length - 1)
final_index = recursive_binary_search(my_list, target_number, 0, len(my_list) - 1)

print(f"\nFinal Result: Target found at index {final_index}")
