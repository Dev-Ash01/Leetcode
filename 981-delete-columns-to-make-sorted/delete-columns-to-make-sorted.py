class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        n = len(strs[0])
        for i in range(n):
            res = []
            for j in strs:
                res.append(j[i])
            if res != sorted(res):
                cnt += 1
        return cnt