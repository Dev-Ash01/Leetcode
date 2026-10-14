class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        total = 0

        for i in accounts:
            for j in i:
                total += j

            if total > max_wealth :
                max_wealth = total 
            total = 0

        return max_wealth