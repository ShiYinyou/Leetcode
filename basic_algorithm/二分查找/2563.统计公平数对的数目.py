#
# @lc app=leetcode.cn id=2563 lang=python3
#
# [2563] 统计公平数对的数目
#

# @lc code=start
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
        对于固定的每一个数，通过二分找到可行上界和下界

        时间复杂度：O(nlgn)，局限在于排序
        空间复杂度：O(1)
        """
        nums.sort()
        ans = 0
        for j,x in enumerate(nums):
            if j==0:
                continue
            l = bisect_left(nums,lower-x,0,j)
            r = bisect_right(nums,upper-x,0,j)
            ans += r-l
        return ans
# @lc code=end

