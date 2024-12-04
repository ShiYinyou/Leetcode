#
# @lc app=leetcode.cn id=275 lang=python3
#
# [275] H 指数 II
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        如果有h满足要求，那么<h都满足；如果h不满足，那么>h都不满足
        结果具有单调性，两个边界条件：
        当h=0时，一定是满足要求的
        当h=n+1时，一定是不满足要求的
        因此取(0,n+1)的开区间，在区间内二分答案
        题目转化为判断h是否满足要求

        时间复杂度：O(lgn)
        空间复杂度：O(1)
        """
        n = len(citations)
        left,right = 0,n+1
        while left+1<right:
            mid = (left+right)//2
            if citations[n-mid] >= mid: 
                # citations[n-mid]：最大的第mid篇论文的引用次数
                left = mid
            else:
                right = mid
        return left
# @lc code=end

