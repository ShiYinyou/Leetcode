#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        在153的基础上，唯一的改动在于元素可重复，对于答案的影响为：
        1.若mid对应数字不是lst，没有影响
        2.若mid对应数字是lst，需要额外判断在哪一段

        时间复杂度：O(lgn)
        空间复杂度：O(1)
        """
        ### 优化写法：相等时直接缩小右端点，一定不会导致丢失最小值：
        # 1.若right是最小，删去right后mid仍是最小值
        # 2.若right不是最小值，相当于排除一个错误答案
        left, right = -1, len(nums)-1
        while left+1<right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1 # 相等时缩小右端点
        return nums[right]

        ### 自己的写法：相等时不断前移mid，若mid能移到-1，说明在第一段
        # def check(idx):
        #     while idx >= 0 and nums[idx]==lst:
        #         idx -= 1
        #     return idx==-1
        # left, right = -1, len(nums)-1
        # lst = nums[-1]
        # while left+1 < right:
        #     mid = (left+right)//2
        #     if nums[mid] > lst or (nums[mid]==lst and check(mid)):
        #         left = mid
        #     else:
        #         right = mid
        # return nums[right]
# @lc code=end

