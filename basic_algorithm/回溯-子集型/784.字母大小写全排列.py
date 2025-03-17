#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        子集型回溯，每个字母选择变/不变大写

        时间复杂度：O(n*2^n)
        空间复杂度：O(n)
        """
        ans = []
        path = []
        n = len(s)
        def dfs(i):
            if i==n:
                ans.append("".join(path))
                return
            c = s[i]
            if '0'<=c<='9':
                path.append(c)
                dfs(i+1)
            else:
                path.append(c.lower())
                dfs(i+1)
                path.pop()
                path.append(c.upper())
                dfs(i+1)
            path.pop()
        dfs(0)
        return ans
            
            
# @lc code=end

