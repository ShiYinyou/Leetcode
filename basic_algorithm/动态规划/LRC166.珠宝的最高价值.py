#
# @lc app=leetcode.cn id=LCR166 lang=python3
#
# [LCR 166] 珠宝的最高价值
#

# @lc code=start
class Solution:
    def jewelleryValue(self, frame: List[List[int]]) -> int:
        ### 1. 递推：O(mn)空间复杂度
        # m,n = len(frame), len(frame[0])
        # dp = [[0]*(n+1) for _ in range(m+1)]
        # for i in range(m):
        #     for j in range(n):
        #         dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j]) + frame[i][j]
        # return dp[m][n]
    
        ### 2. 两个数组，滚动数组：O(n)空间复杂度
        # m,n = len(frame), len(frame[0])
        # dp = [[0]*(n+1) for _ in range(2)]
        # for i in range(m):
        #     for j in range(n):
        #         dp[(i+1)%2][j+1] = max(dp[i%2][j+1],dp[(i+1)%2][j]) + frame[i][j]
        # return dp[m%2][n]

        ### 3. 一个数组，每个数用过一次就不再用了：O(n)空间复杂度
        n = len(frame[0])
        dp = [0]*(n+1)
        for row in frame:
            for j in range(n):
                dp[j+1] = max(dp[j+1],dp[j]) + row[j]
        return dp[n]

# @lc code=end

