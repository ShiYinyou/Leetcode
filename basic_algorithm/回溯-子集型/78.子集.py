#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        子集型回溯

        时间复杂度：O(n*2^n)，每次递归有选/不选，copy答案的时间为O(n)
        空间复杂度：O(n)
        """
        ans = []
        path = []
        n = len(nums)

        ## 1. 从输入的角度
        # def dfs(i):
        #     if i == n:
        #         ans.append(path.copy())
        #         # path是一个全局变量，后续会变化，通过copy固定
        #         return 
        #     dfs(i+1) # 如果不选，直接递归到i+1
        #     # 如果选，则将第i个加入path，再递归i+1，记得递归后要恢复现场
        #     path.append(nums[i])
        #     dfs(i+1)
        #     path.pop()
        # dfs(0)
        # return ans

        ## 2. 从答案的角度
        def dfs(i):
            ans.append(path.copy()) # 需要写在外面，递归到的每个节点都是答案
            # path是一个全局变量，后续会变化，通过copy固定
            if i == n: # 可省略，i=n时j无可取值
                return 
            
            for j in range(i,n):
                path.append(nums[j])
                dfs(j+1)
                path.pop()
        dfs(0)
        return ans
# @lc code=end

