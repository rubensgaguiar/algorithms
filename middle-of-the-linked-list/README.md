# Middle of the linked list

## Statement

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

### Example 1
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

### Example 2
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

### Constrains
- The number of nodes in the list is in the range [1, 100].
- 1 <= Node.val <= 100

## Solution

Our solution must have the following behavior:

- [(1)] -> 2 -> 3 -> 4 -> 5; c[]=0, c()=0
- 1 -> [(2)] -> 3 -> 4 -> 5; c[]=1, c()=1
- 1 -> (2) -> [3] -> 4 -> 5; c[]=2, c()=1
- 1 -> 2 -> (3) -> [4] -> 5; c[]=3, c()=2
- 1 -> 2 -> (3) -> 4 -> [5]; c[]=4, c()=2

[]: actual node
(): middle node

So, we must iterate in the linked list with the "actual node", but we must too iterate in linked list with the "middle node" that will go to next node if 
- c[] = 0 => 0 / 2 = 0.0 => ceil => 0 => c() = 0
- c[] = 1 => 1 / 2 = 0.5 => ceil => 1 => c() = 1
- c[] = 2 => 2 / 2 = 1.0 => ceil => 1 => c() = 1
- c[] = 3 => 3 / 2 = 1.5 => ceil => 2 => c() = 2
- c[] = 4 => 4 / 2 = 2.0 => ceil => 2 => c() = 2

go to next node, if: ceil(c[]/2) > c()


