def depth_first_search(graph, start_node, target_node):
    # A stack to keep track of the paths.
    # Since we are using standard Last-In, First-Out [LIFO] behavior,
    # a normal Python list works well and we do not need deque here.

    search_stack = [[start_node]]

    # A set to keep track of the people we have already checked.
    visited = set()

    print(f"Starting DFS to find '{target_node}' starting from '{start_node}'...\n")

    while search_stack:
        # Pop the path from the TOP (the end) of the stack
        # Python's pop() removes the LAST item from a list
        current_path = search_stack.pop()

        # The current person is the last person in the path
        current_node = current_path[-1]

        print(f"Checking node: {current_node}")

        # Success
        if current_node == target_node:
            print(f"\n-> SUCCESS! Found '{target_node}'.")
            return current_path

        # If not target, stack up their neighbors
        if current_node not in visited:
            visited.add(current_node)

            neighbors = graph.get(current_node, [])

            for neighbor in neighbors:
                if neighbor not in visited:
                    new_path = list(current_path)
                    new_path.append(neighbor)

                    search_stack.append(new_path)
                    print(f"   Pushed to stack: path to {neighbor}")

    # Failure base case
    print(f"\nStack is empty. '{target_node}' could not be found.")
    return None


social_network = {
    "You": ["Alice", "Bob"],
    "Alice": ["Charlie"],
    "Bob": ["Charlie", "Dave"],
    "Charlie": ["Eve"],
    "Dave": [],
    "Eve": [],
}

found_path = depth_first_search(social_network, "You", "Eve")

if found_path:
    print(f"\nPath found: {' -> '.join(found_path)}")
