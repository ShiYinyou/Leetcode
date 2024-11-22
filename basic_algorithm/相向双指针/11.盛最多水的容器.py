#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    """
    对于任意一个中间状态[left,right]，如果固定短边、向内移动长边，容量一定减小
    而如果固定长边，向内移动短边，只有遇到的边更长才有可能使容积增大
    
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        ans = (right-left)*min(height[left],height[right])
        while left < right:
            if height[left] < height[right]:
                m = height[left]
                left += 1
                while height[left] < m:
                    left += 1
            else:
                m = height[right]
                right -= 1
                while height[right] < m:
                    right -= 1
            ans = max(ans,(right-left)*min(height[left],height[right]))
        return ans
# @lc code=end

