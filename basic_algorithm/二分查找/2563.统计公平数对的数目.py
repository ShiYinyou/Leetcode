#
# @lc app=leetcode.cn id=2563 lang=python3
#
# [2563] 统计公平数对的数目
#

# @lc code=start
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
        后向遍历排序后的数组，二分查找能够匹配的上下界

        时间复杂度：O(nlgn)
        空间复杂度：O(1)
        """
        nums.sort()
        ans = 0
        for right,x in enumerate(nums):
            l = bisect_left(nums,lower-x,0,right)
            r = bisect_right(nums,upper-x,0,right)
            ans += r-l
        return ans
# @lc code=end

