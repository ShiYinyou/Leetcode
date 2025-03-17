#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        组合型回溯
        左括号不超过n，右括号数目不多于左括号
        假设左括号为open，则右括号为i-open
        """
        ans = []
        path = [""]*2*n
        def dfs(i,open):
            if i == 2*n:
                ans.append("".join(path))
                return
            if open < n:
                path[i] = "("
                dfs(i+1, open+1)
            if i-open < open:
                path[i] = ")"
                dfs(i+1, open)
        dfs(0,0)
        return ans
# @lc code=end

