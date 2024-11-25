#
# @lc app=leetcode.cn id=2730 lang=python3
#
# [2730] 找到最长的半重复子字符串
#

# @lc code=start
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        """
        记录窗口中包含多少组相等相邻字符，cnt为2时收缩左窗口

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        cnt = left = 0
        ans = 1
        for right,ch in enumerate(s):
            if right>0 and s[right]==s[right-1]:
                cnt += 1
                while cnt == 2:
                    left += 1
                    if s[left]==s[left-1]:
                        cnt -= 1
            ans = max(ans,right-left+1)
        return ans
# @lc code=end

