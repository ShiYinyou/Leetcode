#
# @lc app=leetcode.cn id=2300 lang=python3
#
# [2300] 咒语和药水的成功对数
#

# @lc code=start
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        遍历数组spells，对其中每一个元素，二分potions

        时间复杂度：O((m+n)lgm)
        空间复杂度：O(1)
        """
        m = len(potions)
        ans = [0]*len(spells)
        potions.sort()
        for i,spell in enumerate(spells):
            left,right = -1,m
            while left+1<right:
                mid = (left+right)//2
                if spell*potions[mid] < success:
                    left = mid
                else:
                    right = mid
            ans[i]=m-right
        return ans
# @lc code=end

