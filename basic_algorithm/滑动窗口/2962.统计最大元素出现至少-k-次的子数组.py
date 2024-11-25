#
# @lc app=leetcode.cn id=2962 lang=python3
#
# [2962] 统计最大元素出现至少 K 次的子数组
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        先选出数组中最大的数m，然后统计窗口中的数目
        当窗口中达到k个m时，缩小左窗口直至不足k个
        此时left左边均满足要求

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        ans = left = cnt = 0
        m = max(nums)
        for right,x in enumerate(nums):
            if x==m:
                cnt+=1
                while cnt == k:
                    left += 1
                    if nums[left-1]==m:
                        cnt -= 1
            ans += left
        return ans
# @lc code=end

