# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        begin = 1
        end = n
        middle = int((begin + end) / 2)

        while begin != end:
            if isBadVersion(middle):
                end = middle
            else:
                begin = middle + 1

            middle = int((begin + end) / 2)

        return begin
