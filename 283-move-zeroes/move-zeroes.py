class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for i in range(0, len(nums)):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)



'''
        start = 0
        end = len(nums)-1

        while start < end:
            if nums[end] != 0 :

                if nums[start] == 0:
                    nums[start] = nums[end]
                    nums[end] = 0
                    start += 1
                    end -= end

                else :
                    start += 1

            else : 
                end -= end
                '''