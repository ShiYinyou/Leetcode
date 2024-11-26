#
# @lc app=leetcode.cn id=2529 lang=python3
#
# [2529] 正整数和负整数的最大计数
#

# @lc code=start
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        """
        问题转化为<0和>0

        时间复杂度：O(lgn)
        空间复杂度：O(1)
        """
        def lower_bound(nums,target):
            left,right = -1,len(nums)
            while left+1<right:
                mid = (left+right)//2
                if nums[mid] < target:
                    left = mid
                else:
                    right = mid
            return right
        n = len(nums)
        neg = lower_bound(nums,0) # 不需要-1，因为在统计个数时还会把1加回来
        if neg > n//2:
            return neg
        pos = n - lower_bound(nums,1)
        return max(neg,pos)
# @lc code=end

