class Solution:
    def runningSum(self, nums):
        # Intuition: store each prefix in nums
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

