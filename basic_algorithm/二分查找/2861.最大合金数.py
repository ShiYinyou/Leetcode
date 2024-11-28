#
# @lc app=leetcode.cn id=2861 lang=python3
#
# [2861] 最大合金数
#

# @lc code=start
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        """
        答案具有单调性，转化为判断每台机器是否能在预算内生产
        两个边界条件：
        1. 0份合金一定能完成
        2. 每种材料最多持有量中的最小值+1 一定无法完成

        时间复杂度：O(knlgU)，U表示每种材料最多持有量中的最小值
        空间复杂度：O(1)
        """
        def check(target,i):
            ans = 0
            for j,x in enumerate(composition[i]):
                need = x*target
                if need > stock[j]:
                    ans += (need-stock[j])*cost[j]
            return ans
        left = 0
        right = min([s+budget//c for s,c in zip(stock,cost)])+1
        while left + 1 < right:
            mid = (left+right)//2
            if min([check(mid,i) for i in range(k)]) > budget:
                right = mid
            else:
                left = mid
        return left
# @lc code=end

