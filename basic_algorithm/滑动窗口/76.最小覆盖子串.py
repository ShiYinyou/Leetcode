#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        用一个计数器统计t中字符数目
        当窗口中包含一个t中字符，将计数器中该元素-1
        当计数器中所有元素个数均不大于0，说明找到了一个满足要求的解

        时间复杂度：O(m+n+d) d表示t中包含的字符种数
        空间复杂度：O(d)
        """
        # if len(s)<len(t):
        #     return ""
        # cnt = Counter(t)
        # left = 0
        # ans = inf
        # for right,ch in enumerate(s):
        #     if ch in cnt:
        #         cnt[ch] -= 1
        #         if cnt[ch]<=0 and len([v for v in cnt.values() if v>0])==0:
        #             while True:
        #                 x = s[left]
        #                 left += 1
        #                 if x in cnt:
        #                     cnt[x] += 1
        #                     if cnt[x] > 0:
        #                         break
        #             if right - left + 2 < ans:
        #                 ans = right - left + 2
        #                 l,r = left-1,right+1
        # return "" if ans==inf else s[l:r]

        """
        优化做法：两个cnt可以直接比较大小

        时间复杂度：O(m+n+d) d表示t中包含的字符种数
        空间复杂度：O(d)
        """
        r = len(s)
        if r<len(t):
            return ""
        cnt_s = Counter()
        cnt_t = Counter(t)
        left = 0
        l = -1
        for right,ch in enumerate(s):
            cnt_s[ch] += 1
            while cnt_s >= cnt_t:
                if r-l > right-left:
                    r = right
                    l = left
                cnt_s[s[left]] -= 1
                left += 1
        return "" if l < 0 else s[l:r+1]
            
# @lc code=end

