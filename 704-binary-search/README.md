# 704. Binary Search

## **Statement**
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

### **Example 1**
Input: nums = [-1,0,3,5,9,12], target = 9

Output: 4

Explanation: 9 exists in nums and its index is 4

### **Example 2**
Input: nums = [-1,0,3,5,9,12], target = 2

Output: -1

Explanation: 2 does not exist in nums so return -1

### **Constrains**
- 1 <= nums.length <= 104
- -104 < nums[i], target < 104
- All the integers in nums are unique.
- nums is sorted in ascending order.

## **Solution**

Lets take this example of array [-1,0,3,5,9,12].

### **Case A**
Consider that we must to find a target equals to 9:

**Fist Step**

arr = [-1,0,3,5,9,12]

So, doing a binary search in this array, we have:

b => begin index

r => middle index

e => end index

b = 0

e = len(arr) - 1 = 5

r = int(b + e / 2) = [6/2] = 2

[-1{b},0,3{r},5,9,12{r}]

We verify if 9 is bigger than {r} element, that means:

9 > 3 ? Yes.

So, we must to find from the index {r} + 1 to end.

b = {r} + 1 = 3

**Second Step**

[-1,0,3{r},5{b},9,12{e}]

So, doing a binary search in this array, we have:

r => middle element

r = int(b + e) / 2 = int(3 + 5 / 2) = 4

[-1,0,3,5{b},9{r},12,{e}]

We verify if 9 is equal than {r} element, that means:

9 = 9 ? Yes. => Return {r}.

---
### **Case B**

Consider that we must to find a target equals to 2:

**Fist Step**

b => begin index

r => middle index

e => end index

b = 0

e = len(arr) - 1 = 5

r = int(b + e / 2) = [5/2] = 2

[-1{b},0,3{r},5,9,12{e}]

We verify if 2 is bigger than {r} element, that means:

2 > 3 ? No.

So, we must to find from the begin to index {r}.

e = {r} = 2

**Second Step**

[-1{b},0,3{r}{e},5,9,12]

So, doing a binary search in this array, we have:

r => middle element

r = int(b + e) / 2 = int(0 + 2 / 2) = 1

[-1{b},0{r},3{e},5,9,12]

We verify if 2 is bigger than {r} element, that means:

2 > 0 ? Yes.

So, we must to find from the index {r} + 1 to end.

begin = {r} + 1 = 2

**Thirdy Step**

[-1,0{r},3{b}{e},5,9,12]

So, doing a binary search in this array, we have:

r => middle element

r = int(b + e) / 2 = int(2 + 2 / 2) = 2

[-1,0,3{r}{b}{e},5,9,12]

We verify if 2 is bigger than {r} element, that means:

2 > 3 ? No.

So, we must to find from the begin to index {r}.

end = {r}

begin == end == r => return -1

