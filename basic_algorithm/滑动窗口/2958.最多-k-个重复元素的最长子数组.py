#
# @lc app=leetcode.cn id=2958 lang=python3
#
# [2958] 最多 K 个重复元素的最长子数组
#

# @lc code=start
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        基于 3.无重复字符的最长子串 实现，将计数器的阈值设置为k即可

        时间复杂度：O(n)
        空间复杂度：O(d) d表示不同数字的个数
        """
        left = ans = 0
        cnt = Counter()
        for right,x in enumerate(nums):
            cnt[x] += 1
            while cnt[x] > k:
                cnt[nums[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans
# @lc code=end

