#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        数组可以看成两段。
        需要根据当前值和目标值与最后一素比较大小来判断修改哪个边界

        时间复杂度：
        空间复杂度：
        """
        left, right = -1, len(nums)-1
        lst = nums[-1]
        while left+1 < right:
            mid = (left+right)//2
            if nums[mid] > lst:
                left = mid
            else:
                right = mid
        mn = right

        if target>nums[-1]:
            i = bisect_left(nums,target,0,mn)
            return i if i<mn and nums[i]==target else -1
        else:
            i = bisect_left(nums,target,mn)
            return i if i<len(nums) and nums[i]==target else -1
# @lc code=end

