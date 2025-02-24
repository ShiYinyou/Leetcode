#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        将每两个字母之间看成有一个逗号，
        转化为选不选逗号的 **子集型回溯问题**

        时间复杂度：O(n*2^n)
        空间复杂度：O(n)
        """
        ans = []
        path = []
        n = len(s)
        ## 1. 从答案角度：
        # 枚举第一个逗号的位置，然后枚举第二个逗号的位置……
        # 枚举逗号的位置，相当于枚举回文子串结束的位置
        # def dfs(i):
        #     if i==n:
        #         # 没有每次都添加答案，因为每个字母都需要在答案中
        #         ans.append(path.copy())
        #         return
        #     for j in range(i,n):
        #         t = s[i:j+1]
        #         if t==t[::-1]:
        #             path.append(t)
        #             dfs(j+1)
        #             path.pop()
        # dfs(0)
        # return ans

        ## 2. 从输入角度
        def dfs(i,start): # 需要一个start记录这段回文串的开始位置
            if i==n:
                ans.append(path.copy())
                return 
            # 不选。i=n-1时一定要选
            if i < n-1:
                dfs(i+1,start)
            # 选
            t = s[start:i+1]
            if t==t[::-1]:
                path.append(t)
                dfs(i+1,i+1)
                path.pop()
        dfs(0,0)
        return ans

# @lc code=end

