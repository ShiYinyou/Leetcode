#
# @lc app=leetcode.cn id=2212 lang=python3
#
# [2212] 射箭比赛中的最大得分
#

# @lc code=start
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        """
        子集型回溯。决定每个区域Bob是否得分
        如果得分，即选择，则射入ak+1根箭
        如果不得分（箭数不够则不得分），即不选择，则为0
        
        对于取得的最大得分，如果箭没用完，随意分配即可
        """
        ans = []
        maxScore = 0
        path = [0]*12
        def dfs(i, numArrows):
            if i == 12:
                score = sum([k for k in range(12) if path[k]!=0])
                nonlocal maxScore
                if score > maxScore:
                    maxScore = score
                    nonlocal ans
                    ans = path.copy()
                return 
            # 箭数足够得分，可以选择得分
            if numArrows > aliceArrows[i]:
                path[i] = aliceArrows[i] + 1
                dfs(i+1, numArrows-path[i])
                path[i] = 0
            # 不得分
            dfs(i+1, numArrows)
        dfs(0,numArrows)
        sum_ans = sum(ans)
        if sum_ans < numArrows:
            ans[0] += numArrows-sum_ans
        return ans
# @lc code=end

