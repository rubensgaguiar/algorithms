# 102. Binaryy Tree Level Order Transversal

## Statement
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


### Example 1
Input: root = [3,9,20,null,null,15,7]

Output: [[3],[9,20],[15,7]]

### Example 2.
Input: root = [1]

Output: [[1]]

### Example 3.
Input: root = []

Output: []

### Constrains
- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000

## Solution

Consider this tree of example:


```
3
-----
|   |
9   20
    -----
    |   |
    15  7
```

First, if we want to create an transversal order starting from root, we must to iterate in tree by levels and save the elements of tree in a list following a level order adding the elements first of left side and second from the right side.

So, we will create and index that store the level of root node in tree. This index starts in zero. Moreover, we will create a list that should store the values of elements in each level according with the level index. This list begins empty, and at level with index "n", the list must store all elements of this level.

Consider this notation:
- {}: root node
- []: child to be next root node


```
START

Recursion Lvl 0

index = 0
order = []


{3}
---------
 |      |
[9]    20
        -----
        |   |
        15  7

order = [[3]]

>>>> Recursion Lvl 1
    index = 1
    order = [[3]]


    {9}

    order = [[3], [9]]

Recursion Lvl 0

index = 0
order = [[3], [9]]


{3}
---------
 |      |
 9     [20]
        -----
        |   |
        15  7

order = [[3], [9]]

>>>> Recursion Lvl 1
    index = 1
    order = [[3], [9]]


    {20}
    -----
    |     |
    [15]  7

    order = [[3], [9, 20]]

>>>>>>>> Recursion Lvl 2
        index = 2
        order = [[3], [9, 20]]

        {15}

        order = [[3], [9, 20], [15]]

>>>> Recursion Lvl 1
    index = 1
    order = [[3], [9, 20], [15]]


    {20}
    -----
    |    |
    15  [7]

    order = [[3], [9, 20], [15]]


>>>>>>>> Recursion Lvl 2
        index = 2
        order = [[3], [9, 20], [15]]

        {7}

        order = [[3], [9, 20], [15, 7]]

>>>> Recursion Lvl 1
    index = 1
    order = [[3], [9, 20], [15, 7]]


    {20}
    -----
    |   |
    15  7

    order = [[3], [9, 20], [15, 7]]

Recursion Lvl 0

index = 0
order = []


{3}
---------
 |      |
[9]    20
        -----
        |   |
        15  7

order = [[3], [9, 20], [15, 7]]

END

```

So, as we can see, in recursion of level 0, first, the root val is added to the list, after that, an iteration occours in children of root, and another recursion that change the order list. After the iteration in all children, the function returns if there is not children.
