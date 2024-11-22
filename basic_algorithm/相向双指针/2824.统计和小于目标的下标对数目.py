#
# @lc app=leetcode.cn id=2824 lang=python3
#
# [2824] 统计和小于目标的下标对数目
#

# @lc code=start
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        """
        由于只要求返回下标对的数量，因此是顺序无关的，进行排序
        排序后类似于一个有序数组的两数之和问题
        不断移动右指针直到满足和小于target，那么在left固定条件下，共有right-left个数对满足要求
        
        时间复杂度：O(nlgn) 主程序需要O(n)，排序开销O(nlgn)
        空间复杂度：O(1)
        """
        nums.sort()
        ans = left = 0
        right = len(nums)-1
        while left < right:
            x = nums[left] + nums[right]
            if x >= target:
                right -= 1
            else:
                ans += right-left
                left += 1
        return ans
# @lc code=end
