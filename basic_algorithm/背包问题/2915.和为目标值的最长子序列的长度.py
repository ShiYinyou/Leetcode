#
# @lc app=leetcode.cn id=2915 lang=python3
#
# [2915] 和为目标值的最长子序列的长度
#

# @lc code=start
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        f = [[-inf]*(target+1) for _ in range(2)]
        f[0][0]=0
        for i,x in enumerate(nums):
            for c in range(target+1):
                if c < x:
                    f[(i+1)%2][c] = f[i%2][c]
                else:
                    f[(i+1)%2][c] = max(f[i%2][c], f[i%2][c-x]+1)
        return f[n%2][target] if f[n%2][target]>0 else -1
# @lc code=end

# [1,1,5,4,5]\n3