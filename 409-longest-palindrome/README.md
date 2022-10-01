# 409. Logest Palindrome

## Statement
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


### Example 1
Input: s = "abccccdd"

Output: 7

Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

### Example 2.
Input: s = "a"

Output: 1

Explanation: The longest palindrome that can be built is "a", whose length is 1.

### Constrains
- 1 <= s.length <= 2000
- s consists of lowercase and/or uppercase English letters only.

## Solution
Consider this case:

abccccdd

If we create an hash table and iterate in this list adding each value as a key of our hash and adding the number of times that this letter appears in list as the value of hash table we will have:

{
    a: 1,
    b: 1,
    c: 4,
    d: 2
}

Then, we will iterate in this hashtable, then, if we find an odd number, we add 1 in palindrome counter just one time, after that we add the even part of each counter, by example, if "c: 5", we will do int(5/2) = 2 * 2 = 4, so we will add 4 in our counter that is the biggest pair less or equal to 5.

So, in our example:

counter = 0

"a: 1" => counter = 1
"b: 1" => counter = 1 + int(1 / 2) * 2 = 1
"c: 4" => counter = 1 + int(4 / 2) * 2 = 5
"d: 2" => counter = 5 + int(2 / 2) * 2 = 7 => our biggest palindrome.

This solution works because to mount an palindrome we must to have a setence that is mirrored in center, by example:

cccaccc => ccc | ccc
cccddcccc => cccd | dccc
cccdadcccc => cccd | dccc


