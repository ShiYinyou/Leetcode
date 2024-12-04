#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        如果速度k可以吃完，那么>k一定可以吃完
        结果具有单调性，二分解决。问题转化为判断速度k能否吃完香蕉
        要判断是否能吃完，计算pile/k上取整之和
        两个边界条件：
        当速度为max(piles)时，一定可以吃完
        当速度为0时，一定不能吃完

        时间复杂度：O(nlgU),U=max(piles)
        空间复杂度：O(1)
        """
        n = len(piles)
        left,right = 0,max(piles)
        while left+1<right:
            mid = (left+right)//2
            if sum([(pile-1)//mid for pile in piles]) + n <= h:
                right = mid
            else:
                left = mid
        return right
# @lc code=end

