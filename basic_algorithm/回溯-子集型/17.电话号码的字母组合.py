#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start

MAPPING = ["","","abc","def","ghi","jkl","mno","pqrs", "tuv","wxyz"]
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        多重循环的回溯问题
        回溯三问：
        1. 当前操作？  枚举path[i]要填入的字母
        2. 子问题？  构造字符串>=i的部分
        3. 下一个子问题？  构造字符串>=i+1的部分
        dfs(i) -> dfs(i+1)

        时间复杂度：O(n*4^n)
        空间复杂度：O(n)
        """
        n = len(digits)
        if n == 0:
            return []
        ans = []
        path = ['']*n
        
        def dfs(i):
            if i == n: # 边界条件
                ans.append("".join(path))
                return 
            # 非边界条件
            for c in MAPPING[int(digits[i])]:
                path[i] = c
                dfs(i+1)
        dfs(0)
        return ans
# @lc code=end

