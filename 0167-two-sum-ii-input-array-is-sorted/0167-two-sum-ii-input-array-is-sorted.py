class Solution:
    def twoSum(self, numbers, target):
        # Step 1 - Defining the 2 pointers
        left = 0
        right = len(numbers)-1

        # Step 3 - CHECKING WITH TARGET
        while left < right :
            #Step 2 - getting the value 
            current_value = numbers[left] + numbers[right]
            if current_value == target:
                return [left+1 , right+1]

            elif current_value < target:
                left += 1

            else :
                right -= 1
