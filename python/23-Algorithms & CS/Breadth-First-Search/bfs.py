# We use deque (Double-Ended Queue) from python's collections.
# It is much faster for popping items off the front of a list than a standard Python list.
from collections import deque


def breadth_first_search(graph, start_node, target_node):
    # A queue to keep track of the paths we are checking
    # We store the path taken so far, starting with just the start_node
    search_queue = deque([[start_node]])

    # A set to keep track of people we have already checked so that we do not loop forever
    visited = set()

    print(f"Starting BFS to find '{target_node}' starting from '{start_node}'...\n")

    while search_queue:
        # Pop the first path from the FRONT of the queue (First-In, First-Out)
        current_path = search_queue.popleft()

        # The current person we are looking at is the last person in this path
        current_node = current_path[-1]

        print(f"Checking node: {current_node}")

        # Success base case
        if current_node == target_node:
            print(f"\n-> SUCCESS! Found '{target_node}'.")
            return current_path

        # If not the target, queue up their neighbors
        if current_node not in visited:
            # Mark them as visited
            visited.add(current_node)

            # Look up their friends in our graph dictionary
            neighbors = graph.get(current_node, [])

            for neighbor in neighbors:
                if neighbor not in visited:
                    # Create a new path by copying the old one and adding the neighbor
                    new_path = list(current_path)
                    new_path.append(neighbor)

                    # Add this new path to the back of the queue
                    search_queue.append(new_path)
                    print(f"   Added to queue: path to {neighbor}")

    # Failure base case
    # If the queue becomes completely empty, the person is not in the network
    print(f"\nQueue is empty. '{target_node}' could not be found.")
    return None


# In Python, we represent graphs using dictionaries (Hash Maps).
# The Key is the node, the Value is a list of their neighbors.
social_network = {
    "You": ["Alice", "Bob"],
    "Alice": ["Charlie"],
    "Bob": ["Charlie", "Dave"],
    "Charlie": ["Eve"],
    "Dave": [],
    "Eve": [],
}

# Run the search
shortest_path = breadth_first_search(social_network, "You", "Eve")

if shortest_path:
    print(
        f"The shortest connection is {len(shortest_path) - 1} steps: {' -> '.join(shortest_path)}"
    )
