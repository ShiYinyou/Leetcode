#
# @lc app=leetcode.cn id=301 lang=python3
#
# [301] 删除无效的括号
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        组合型回溯
        设左括号为left，右括号为right
        若left=right时，不能选右括号
        如果最后left!=right，则一定不对
        """
        ans = []
        max_length = 0
        path = []
        n = len(s)
        def dfs(i,left,right):
            if i == n:
                if left == right:
                    x = "".join(path)
                    l = len(x)
                    nonlocal max_length
                    if l > max_length:
                        ans.clear()
                        ans.append(x)
                        max_length = l
                    elif l == max_length:
                        if x not in ans:
                            ans.append(x)
                return
            c = s[i]
            if c not in "()":
                path.append(c)
                dfs(i+1,left,right)
                path.pop()
                return
            if not (c==")" and left == right):
                path.append(c)
                if c=="(":
                    dfs(i+1,left+1,right)
                else:
                    dfs(i+1,left,right+1)
                path.pop()
            dfs(i+1,left,right)
        dfs(0,0,0)
        return ans
# @lc code=end

