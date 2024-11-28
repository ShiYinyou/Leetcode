#
# @lc app=leetcode.cn id=2187 lang=python3
#
# [2187] 完成旅途的最少时间
#

# @lc code=start
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        """
        以示例1为例，假如3小时可以完成，那么大于3小时一定可以完成
        如果2小时无法完成，那么小于2小时一定无法完成
        答案具有单调性，可以使用二分进行求解
        问题转化为判断是否能在mid小时内完成
        两个边界条件：
        1. 当时间为0时，一定无法完成
        2. 当时间为totalTrips*min(times)时，一定可以完成

        时间复杂度：O(nlgU)，U是times中的最大值，在计算sum时需要遍历times中元素
        空间复杂度：O(1)
        """
        left,right = 0, totalTrips*min(time)
        while left + 1 < right:
            mid = (left+right)//2
            if sum(mid//time for time in time) < totalTrips:
                left = mid
            else:
                right = mid
        return right
# @lc code=end

