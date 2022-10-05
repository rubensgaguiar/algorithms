# Statement
Given the head of a singly linked list, reverse the list, and return the reversed list.

## Example 1
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

## Example 2
Input: head = [1,2]
Output: [2,1]

## Example 3
Input: head = []
Output: []

### Contrains
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

#### Follow up
A linked list can be reversed either iteratively or recursively. Could you implement both?

# Solutions

## Solution 1 - Iterative

zero iteration:

head = 1 -> 2 -> 3 -> 4 -> 5

Create an empty node, associate in this node:

node = 1 -> None

remove 1 of head, doing: head = head.next

first iteration:

head = 2 -> 3 -> 4 -> 5

Create an empty node, associate in this node:

node = 2 -> 1

remove 2 of head, doing: head = head.next

second iteration:

head = 3 -> 4 -> 5

Create an empty node, an do:

node = 3 > 2 > 1

....

last-1 iteration:

head = 5

Create an empty node, an do:

node = 5 > 4 > 3 > 2 > 1

remove 5 of head, doing: head = head.next

and stop because head is none



## Solution 2 - Recursive

we pass None and 1 -> 2 -> 3 -> 4 -> 5 to funtion, the function do:

2 -> 1
3 -> 4 -> 5

and then, we pass 2 -> 1 and 3 -> 4 -> 5 to function, the function do:

3 -> 2 -> 1
4 -> 5

and then, we pass 3 -> 2 -> 1 and 4 -> 5 to function, the function do:

4 -> 3 -> 2 -> 1
5

and then, we pass 4 -> 3 -> 2 -> 1 and 5 to function, the function do:

5 -> 4 -> 3 -> 2 -> 1
None

function ends

