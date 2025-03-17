#
# @lc app=leetcode.cn id=2397 lang=python3
#
# [2397] 被列覆盖的最多行数
#

# @lc code=start
class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        """
        子集型回溯，需要以答案角度进行选择
        """
        ans = 0
        path = []
        n = len(matrix[0])
        def dfs(i,numSelect):
            if n-i < numSelect:
                return
            if i == n or numSelect == 0:
                t = 0
                for row in matrix:
                    if sum([row[col] for col in range(n) if col not in path]) == 0:
                        t+=1
                nonlocal ans
                ans = max(ans,t)
                return
            for j in range(i,n):
                path.append(j)
                dfs(j+1, numSelect-1)
                path.pop()
        dfs(0,numSelect)
        return ans
# @lc code=end

