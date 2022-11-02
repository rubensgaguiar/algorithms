# 98. Validate Binary Search Tree

## Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

### Example 1
```
Input: root = [2,1,3]
Output: true
```

### Example 2.
```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

### Constrains
- The number of nodes in the tree is in the range [1, 104].
- -231 <= Node.val <= 231 - 1


## Solution

**First Case**

Lets consider this tree:

```
Tree: 

2
-----
|   |
1   3
```

We must to validate if the children of root element satisfies the valid BST condition. If yes, we must to take each children and pass then as root to another isValidBST verification. So, doing that, we have:

1. Verify if children satisfies the conditions:

```
root > left  => 2 > 1 => OK
root < right => 2 < 3 => OK
```

2. Children as root:

```
Tree: 

1
```

Don't have any children => return True.

3. Children as root:

```
Tree: 

3
```

Don't have any children => return True.

4. At end

When all children returns True and all conditions are satisfied, the tree is valid!


**First Case**

Lets consider this tree:

```
Tree: 

5
-----
|   |
1   4
    -----
    |   |
    3   6
```

1. Verify if children satisfies the conditions:

```
root > left  => 5 > 1 => OK
root < right => 5 < 4 => FALSE
```

One of conditions is False, so this Tree isn't valid, in this case return False.
