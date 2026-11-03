class Solution(object):
    def minMoves(self, nums):
        count = 0
        n = max(nums)

        for i in range(0, len(nums)):
            if nums[i] < n:
                diff = n - nums[i]
                nums[i] += diff
                count += diff

        return count