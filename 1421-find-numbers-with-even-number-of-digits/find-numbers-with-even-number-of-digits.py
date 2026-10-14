class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for i in nums:
            if (10 <= i < 100) or (1000 <= i < 10000) or (i == 100000):
                count += 1
        return count