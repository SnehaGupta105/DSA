class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        mid= len(nums)//2
        equal = nums[mid]
        count=0
        for i in range (0, len(nums)):
            if nums[i]!= equal:
                n= abs(equal-nums[i])
                nums[i] += n
                count += n

        return count


        