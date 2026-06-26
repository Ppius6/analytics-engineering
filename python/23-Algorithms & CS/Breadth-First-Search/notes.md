
# Graph Navigators (Breadth-First Search)

We need to understand two concepts here:

- `Graphs (Nodes and Edges)`: A graph is made of data points called "Nodes" (i.e., people in a network) connected by lines called "Edges" (i.e., relationships between people). Graphs can be directed or undirected, weighted or unweighted, and can represent various real-world scenarios.

- `Queue (FIFO)`: BFS relies on a data structure called a queue, which follows the First-In-First-Out (FIFO) principle, working exactly like a line at a grocery store. The first person to enter the line is the first one to be served. In programming, a queue allows us to add elements to the back and remove elements from the front.

## The Logical Concept

Imagine we lose a dog, and want to ask our friends if they have seen it. 

- First, we need to ask our immediate friends (the first level of connections - 1 step away).

- If they have not seen the dog, we ask them to ask their friends (the second level of connections - 2 steps away).

- Then we ask their friends - 3 steps away.

We would never ask a friend-of-a friend before we finish asking our own direct frieds. The `layer-by-layer` expansion is exactly how BFS works. It explores all neighbors at the present depth prior to moving on to nodes at the next depth level.

## The Worked Example (Step-by-Step Trace)

Let us map out a mini social network. We want to find the shortest connection between me and a friend named "Eve". The graph is represented as follows:

- I am friends with `Alice` and `Bob`.
- `Alice` is friends with `Charlie`
- `Bob` is friends with `Dave` and `Charlie`.
- `Charlie` is friends with `Eve`, our target.
- `Dave` is friends with no one else.

The graph can be visualized as:

```
        Me
       /  \
    Alice  Bob
      |     | \
   Charlie  Dave
      |
     Eve
```

In our setup, we create an empty `Queue` and also keep a `Visited` list so we do not accidentally check the same person twice which would cause an infinite loop.

1. In Loop 1,
    - Add me to the queue
    - Queue: [Me] | Visited: []
    - Pop the front of the queue (Me). Am I Eve? No. 
    - Add my friends (Alice and Bob) to the queue.
    - Queue: [Alice, Bob] | Visited: [Me]

2. In Loop 2, 
    - Pop the front of the queue (Alice). Is Alice Eve? No.
    - Add Alice's friends to the back.
    - Queue: [Bob, Charlie] | Visited: [Me, Alice]

3. In Loop 3,
    - Pop the front of the queue (Bob). Is Bob Eve? No.
    - Add Bob's friends to the back (Charlie is already in the queue, so we just add Dave).
    - Queue: [Charlie, Dave] | Visited: [Me, Alice, Bob]

4. In Loop 4,
    - Pop the front of the queue (Charlie). Is Charlie Eve? No.
    - Add Charlie's friends to the back (Eve).
    - Queue: [Dave, Eve] | Visited: [Me, Alice, Bob, Charlie]

5. In Loop 5,
    - Pop the front of the queue (Dave). Is Dave Eve? No.
    - Dave has no friends to add.
    - Queue: [Eve] | Visited: [Me, Alice, Bob, Charlie, Dave]

6. In Loop 6,
    - Pop the front of the queue (Eve). Is Eve Eve? Yes! We found her! 
    - The search is complete.