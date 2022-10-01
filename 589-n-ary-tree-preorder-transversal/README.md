# 589. N-ary Tree Preorder Traversal

## Statement
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

### Example 1
Input: root = [1,null,3,2,4,null,5,6]

Output: [1,3,5,6,2,4]

### Example 2.
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]

### Constrains
- The number of nodes in the tree is in the range [0, 104].
- 0 <= Node.val <= 104
- The height of the n-ary tree is less than or equal to 1000.

### Follow up
Recursive solution is trivial, could you do it iteratively?


## Solution
Once we have an input like this:

[1,null,3,2,4,null,5,6]

We can build this nodes:

{
    val: 1,
    children: [-> 3, -> 2, -> 4]
}

{
    val: 3,
    children: [-> 5, -> 6]
}


{
    val: 2,
    children: None
}

{
    val: 4,
    children: None
}

{
    val: 5,
    children: None
}

{
    val: 6,
    children: None
}

And our tree will be:

```
1
-----------------
|           |   |
3           2   4
-----
|   |
5   6

```




We must to create a list with elements in pre order, so, to do this we must to most left element starting in the root of tree. So, we can do this:

### START

Add the root of tree.

```
1. Recursion -> Lvl 1

(1)
-----------------
|           |   |
3           2   4
-----
|   |
5   6

```

Then, get the first child and add the root.

```
2. Recursion -> Lvl 2

(3)
-----
|   |
5   6

```

Then, get the first child and add the root.

```
3. Recursion -> Lvl 3

(5)

```

Add the root value. No child, return.

```
4. Recursion -> Lvl 2

{3}
-----
|   |
5   6

```

Get the next child.

```
5. Recursion -> Lvl 3

(6)

```

Add the root value. No child, return.

```
6. Recursion -> Lvl 2

{3}
-----
|   |
5   6

```

No child, return.

```
7. Recursion -> Lvl 1

{1}
-----------------
|           |   |
3           2   4
-----
|   |
5   6

```

Get the next child.

```
8. Recursion -> Lvl 2

(2)

```

Add the root value. No child, return.

```
9. Recursion -> Lvl 1

{1}
-----------------
|           |   |
3           2   4
-----
|   |
5   6

```

Get the next child:

```
10. Recursion -> Lvl 2

(4)

```

Add the root value. No child, return.

```
11. Recursion -> Lvl 1

{1}
-----------------
|           |   |
3           2   4
-----
|   |
5   6

```

No child, return.

### END

So, we built this list that is the preorder list:

[1, 3, 5, 6, 2, 4]

Then, we must to create a recursive function that receive root element and a list, add the value of root in the list, iterate in their children calling the recursive function with child as root and the built list. After iteration or if the root has no child, the function must return.


## Solution with follow up

If we want to do this iteratively we must to do:

order = []
children_list = [{1}]

**START**

Get pointer
- pointer = children_list.pop(0) = {1}
- children_list = []

*Iteration in children_list*

```
1. Iteration

{1}
-----------------
|           |   |
3           2   4
-----
|   |
5   6

```

Add to children_list:
children_list = pointer.children + children_list
- children_list = [{3}, {2}, {4}]


Add pointer val list order:
order = order.append(1)
- order = [1]

Get pointer
- pointer = children_list.pop(0) = {3}
- children_list = [{2}, {4}]


```
2. Iteration

1
-----------------
|           |   |
{3}           2   4
-----
|   |
5   6

```

Add to children_list:
children_list = pointer.children + children_list
- children_list = [{5}, {6}, {2}, {4}]


Add pointer val list order:
order = order.append(3)
- order = [1, 3]

Get pointer
- pointer = children_list.pop(0) = {5}
- children_list = [{6}, {2}, {4}]


```
3. Iteration

1
-----------------
|           |   |
3           2   4
-------
|     |
{5}   6

```

Add to children_list:
children_list = pointer.children + children_list
- children_list = [{6}, {2}, {4}]


Add pointer val list order:
order = order.append(5)
- order = [1, 3, 5]

Get pointer
- pointer = children_list.pop(0) = {6}
- children_list = [{2}, {4}]


```
4. Iteration

1
-----------------
|           |   |
3           2   4
------
|    |
5   {6}

```

Add to children_list:
children_list = pointer.children + children_list
- children_list = [{2}, {4}]


Add pointer val list order:
order = order.append(6)
- order = [1, 3, 5, 6]

Get pointer
- pointer = children_list.pop(0) = {2}
- children_list = [{4}]


```
5. Iteration

1
------------------
|            |   |
3           {2}  4
-----
|   |
5   6

```

Add to children_list:
children_list = pointer.children + children_list
- children_list = [{4}]


Add pointer val list order:
order = order.append(6)
- order = [1, 3, 5, 6, 2]

Get pointer
- pointer = children_list.pop(0) = {4}
- children_list = []

```
5. Iteration

1
------------------
|           |    |
3           2   {4}
-----
|   |
5   6

```

Add to children_list:
children_list = pointer.children + children_list
- children_list = []


Add pointer val list order:
order = order.append(6)
- order = [1, 3, 5, 6, 2, 4]

**END**