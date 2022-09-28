# 142. Linked List Cycle II

## Statement
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

### Example 1
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

### Example 2
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

### Example 3
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

### Constrains
- The number of the nodes in the list is in the range [0, 104].
- -105 <= Node.val <= 105
- pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?

## Solution without follow up

In this case, we have:

3 -> 2 -> 0 -> 4 -> 2 -> 0 -> 4 -> (2)

So, we will create a dict that will store the nodes of list and we will iterate in linked list.

In iteration we will verify if the node already is in dict. If not, we must add this node. If yes, we return this node because we have a repeated node, this only happen when we have an cycle.

So, we must to do:

1) Iteration

```
dict = {}

list = 3 -> 2 -> 0 -> 4 -> 2 -> 0 -> 4 -> (2)

list in dict ? false
```

2) Iteration

```
dict = {
  3 -> 2 -> 0 -> 4 -> 2 -> 0 -> 4 -> (2),
}

2 -> 0 -> 4 -> 2 -> 0 -> 4 -> (2)

list in dict ? false
```

3) Iteration

```
dict = {
  3 -> 2 -> 0 -> 4 -> 2 -> 0 -> 4 -> (2),
  2 -> 0 -> 4 -> 2 -> 0 -> 4 -> (2),
}

0 -> 4 -> 2 -> 0 -> 4 -> (2)

list in dict ? false
```

4) Iteration

```
dict = {
  3 -> 2 -> 0 -> 4 -> 2 -> 0 -> 4 -> (2),
  2 -> 0 -> 4 -> 2 -> 0 -> 4 -> (2),
  0 -> 4 -> 2 -> 0 -> 4 -> (2),
}

4 -> 2 -> 0 -> 4 -> (2)

list in dict ? false
```

5) Iteration

```
dict = {
  3 -> 2 -> 0 -> 4 -> 2 -> 0 -> 4 -> (2),
  2 -> 0 -> 4 -> 2 -> 0 -> 4 -> (2),
  0 -> 4 -> 2 -> 0 -> 4 -> (2),
  4 -> 2 -> 0 -> 4 -> (2),
}

2 -> 0 -> 4 -> (2)

list in dict ? true => return list 
```

This solution is O(N) in time and space.

## Solution with follow up

We will create a slow pointer and a faster pointer, the slower pointer will walk through the list with one by one steps, the faster pointer will walk through the list with two by two steps.

[]: slower
{}: faster

- [{3}] -> 2 -> 0 -> 4 -> 2 -> 0 -> 4 -> (2)
- 3 -> [2] -> {0} -> 4 -> 2 -> 0 -> 4 -> (2)
- 3 -> 2 -> [0] -> 4 -> {2} -> 0 -> 4 -> (2)
- 3 -> 2 -> 0 -> [4] -> 2 -> 0 -> {4} -> (2)
- 3 -> 2 -> {0} -> 4 -> [2] -> 0 -> 4 -> (2)
- 3 -> 2 -> 0 -> 4 -> {2} -> [0] -> 4 -> (2)
- 3 -> 2 -> 0 -> 4 -> 2 -> 0 -> [{4}] -> (2) => CYCLE = faster.next
- 3 -> [2] -> {0} -> 4 -> 2 -> 0 -> 4 -> (2)
- 3 -> 2 -> [0] -> 4 -> {2} -> 0 -> 4 -> (2)

This happens because:

- The distance to the entry of cycle is L1
- The length of cycle is L2
- The length of list without cycles is L1 + L2

So, after N steps we have:

slower_position = N = L1 + p*L2

faster_position = 2 * N = L1 + q*L2

=> subtraction <=

N = (q-p) * L2

L2 > 0; q > p > 0 => N exists.

In a more generic way, we can do:

slower_position = N = L1 + x + p*L2

faster_position = 2 * N = L1 + x + q*L2

=> subtraction <=

N = (q-p) * L2

L2 > 0; q > p > 0 => N exists.

So, the encouter point can happen in any point inside cycle.

Moreover, after several steps, we must to find and N that satisfies our encounter condition. Therefore, we must to find the entry of cycle to return in our function.

But, we know that:

L1: distance to entry point
L2: distance of entry point to meeting point
L3: length of cycle

But, we know that the faster pointer travels 2 times more faster than slower pointer, then, we have:

Distance Traveled of Faster = 2 * (L1 + L2)

or

Distance Traveled of Faster = L1 + L2 + n * C

So,

2 * (L1 + L2) = L1 + L2 + n * C
L1 = n * C - L2

So, moves the entry pointer and the slower point after the meet occours one step each time:

Initial:
entry_pos = 0
slower_pos = L1 + L2

After L1 steps:
entry_pos = L1
slower_pos = 2 * L1 + L2 = 2 * n * C - 2 * L2 + L2 = 2 * n * C - L2

But 2 * n * C means that the slower point returns to the meeting point:

slower_pos = L1 + L2 - L2 = L1

So, after L1 steps, slower_pos == entry_pos, therefore we find the entry point of cycle.
