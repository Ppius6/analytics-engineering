
# Depth First Search (DFS)

To understand Depth First Search (DFS), we need to understand the `Stack` data structure. 

## The Logical Concept

A stack works exactly like a stack of plates. You can only add or remove the top plate. The last plate you put on the stack is the first one you take off. This is known as Last In First Out (LIFO).

In DFS, instead of adding your friends to the back of the line, you add them to the front of the stack. This means the computer will immediately abandon what it was doing to explore the newest friend you just added, diving deeper and deeper into the network.

## The Worked Example

We want to find Eve, starting from me.

- I am friends with Alice and Bob.
- Alice is friends with Charlie
- Bob is friends with Charlie and Dave
- Charlie is friends with Eve

1. Loop 1: Exploring step 1
    Stack [Me]
    Pop the top of the stack, which is Me. 
    Add the neighbors to the top of the stack
    Stack: [Alice, Bob]

2. Loop 2: Exploring step 2
    Here, the major difference is, in BFS, we checked Alice next because she was at the front. In DFS, we pull from the top (the end) of the stack.
    Pop the top of the stack, which is Bob.
    Look at Bob's friends, which are Charlie and Dave. 
    Add them to the top of the stack.
    Stack: [Alice, Charlie, Dave]

2. Loop 3: Exploring step 3
    Pop the top of the stack, which is Dave.
    Look at Dave's friends, but he has none. 
    Stack: [Alice, Charlie]

3. Loop 4: Exploring step 4
    Pop the top of the stack, which is Charlie.
    Look at Charlie's friends, which is Eve.
    Add Eve to the top of the stack.
    Stack: [Alice, Eve]

4. Loop 5: Exploring step 5
    Pop the top of the stack, which is Eve.
    We found Eve! The search is complete.

Notice that DFS completely ignored Alice. It ran straight down Bob's path, hit a dead end at Dave, backed up, and found Eve through Bob $\rightarrow$ Charlie $\rightarrow$ Eve. Since DFS dives blindly, it `does not guarantee the shortest path`. However, it uses much less memory than BFS and is incredible for exhaustively exploring massive mazes or game trees (like calculating the best move in chess).

