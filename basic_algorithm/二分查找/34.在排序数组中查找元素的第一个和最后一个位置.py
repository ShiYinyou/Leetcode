# @before-stub-for-debug-begin
from python3problem34 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        题目需要求>=和<=
        
        时间复杂度：O(lgn)
        空间复杂度：O(1)
        """
        def lower_bound(nums:List[int], target:int) -> int:
            left,right = -1,len(nums)
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid
                else:
                    right = mid
            return right
        start = lower_bound(nums,target)
        # 当start为数组长度，或表示的值不是target时，说明没有找到
        if start == len(nums) or nums[start]!=target:
            return [-1,-1]
        end = lower_bound(nums,target+1)-1
        return [start,end]
# @lc code=end

