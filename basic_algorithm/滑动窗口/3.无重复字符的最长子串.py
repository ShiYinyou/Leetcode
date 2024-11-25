#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        每当窗口中某种字符数量变成2，则缩小左窗口

        时间复杂度：O(n)
        空间复杂度：O(d) d表示字符的种数
        """
        left = ans = 0
        cnt = Counter()
        for right,ch in enumerate(s):
            cnt[ch] += 1
            while cnt[ch] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans
# @lc code=end

