# 235. Lowest Common Ancestor of a Binary Search Tree

## Statement
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

### Example 1
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
```

### Example 2
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
```

### Example 3
```
Input: root = [2,1], p = 2, q = 1
Output: 2
```

### Constrains
- The number of nodes in the tree is in the range [2, 105].
- -109 <= Node.val <= 109
- All Node.val are unique.
- p != q
- p and q will exist in the BST.

## Solution
To solve this problem is necessary create a way to walk through tree using the two nodes of reference, that means, we must to go to left or right based on some comparison between the actual node and the reference nodes.

Let's take some example:

```
p = 2
q = 4


6
---------------
|             |
2             8
-----         -----
|   |         |   |
0   4         7   9
    -----
    |   |
    3   5
```

In this case, we analyze the first node:

```
6 > 2
6 > 4

go left
```

Now, the tree is:

```
p = 2
q = 4


2
-----
|   |
0   4
    -----
    |   |
    3   5
```

In this case, we analyze the first node:

```
2 == 2
2 < 4

return
```

Let's take another example:

```
p = 2
q = 8


6
---------------
|             |
2             8
-----         -----
|   |         |   |
0   4         7   9
    -----
    |   |
    3   5
```

In this case, we analyze the first node:

```
6 > 2
6 < 8

return
```

So, as we can see in the two examples above, this happens: while the actual node isn't between the two nodes, that means, while the actual node isn't more or equal than one of nodes and isn't less or equal than one of nodes, we must to go to left or right.

If the actual node is more or equal than one of nodes and less or equal then the other node, we must to return.
