from collections import Counter

# Complexities
# time: O(N)
# space: O(1)

class Solution:
    def hard_counter(self, s: str) -> dict:
        dict_counter = {}
        for char in s:
            if char in dict_counter:
                dict_counter[char] += 1
            else:
                dict_counter[char] = 1
        return dict_counter        

    def longestPalindrome(self, s: str) -> int:
        # dict_counter = self.hard_counter(s)
        # OR
        dict_counter = Counter(s)
    
        longest_palindrome = 0
        add_odd_element = True
        for item in dict_counter.values():
            if add_odd_element:
                if item % 2 == 1:
                    longest_palindrome += 1
                    add_odd_element = False
            
            longest_palindrome += int(item / 2) * 2
        
        return longest_palindrome
