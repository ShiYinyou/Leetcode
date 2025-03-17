#
# @lc app=leetcode.cn id=2698 lang=python3
#
# [2698] 求一个整数的惩罚数
#

# @lc code=start
class Solution:
    def punishmentNumber(self, n: int) -> int:
        """
        子集型回溯，部分过程参考131分割回文串
        """
        ans = []
        def dfs(j,start):
            if j == length:
                if sum([int(x) for x in path]) == i:
                    ans.append(num)
                return
            if j < length-1:
                dfs(j+1,start)
            path.append(s[start:j+1])
            dfs(j+1,j+1)
            path.pop()
        for i in range(n+1):
            path = []
            num = i*i
            s = str(num)
            length = len(s)
            dfs(0,0)
        return sum(set(ans))
# @lc code=end

