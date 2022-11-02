class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b = 0
        e = len(nums) - 1

        while e >= b:
            r = int((e + b) / 2)

            if target > nums[r]:
                b = r + 1
            elif target == nums[r]:
                return r
            else:
                e = r

            if b == e == r:
                return -1

        return -1
