class Solution(object):
    def rearrangeArray(self, nums):
        pos = []
        neg = []
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] < 0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        for i in range(n // 2):
            nums[2*i] = pos[i]
            nums[(2*i) + 1] = neg[i]
        return nums