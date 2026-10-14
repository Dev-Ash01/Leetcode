class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        previous_sum = 0

        for i in range(0,len(nums)):
            previous_sum += nums[i]
            nums[i] = previous_sum

        return nums


