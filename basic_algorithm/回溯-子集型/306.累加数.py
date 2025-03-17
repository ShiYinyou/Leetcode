#
# @lc app=leetcode.cn id=306 lang=python3
#
# [306] 累加数
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        """
        子集型回溯
        """
        ans = []
        path = []
        n = len(num)
        def dfs(i,start):
            if i == n:
                if len(path)>=3:
                    ans.append(path.copy())
                return
            if i<n-1 and num[start] != "0":
                dfs(i+1,start)
            x = num[start:i+1]
            if len(path)>2 and int(path[-2])+int(path[-1]) != int(x):
                return
            path.append(x)
            dfs(i+1,i+1)
            path.pop()
        dfs(0,0)
        for nums in ans:
            flag = True
            for i in range(2,len(nums)):
                if () or (int(nums[i-2])+int(nums[i-1]) != int(nums[i])):
                    flag = False
                    break
            if flag:
                return True
        return False
# @lc code=end

