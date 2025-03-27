#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N 皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        排列型回溯
        按照行序，对列号进行排列
        """
        ans = []
        path = []
        def dfs(i,s):
            if i == n:
                ans.append(["."*x+"Q"+"."*(n-1-x) for x in path])
                return
            for x in s:
                ## all操作符
                # all(iterable)
                # iterable为空 或 iterable元素全为True 时为True
                if all([abs(x-c)!=abs(i-l) for l,c in enumerate(path)]):
                    path.append(x)
                    dfs(i+1, s-{x})
                    path.pop()
        dfs(0,set(range(n)))
        return len(ans)
# @lc code=end

