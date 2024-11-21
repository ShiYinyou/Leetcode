#
# @lc app=leetcode.cn id=611 lang=python3
#
# [611] 有效三角形的个数
#

# @lc code=start
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        通过固定最大边后，可以将问题转化为 2824.统计和小于目标的下标对数目
        双指针过程中，寻找对于每一个右指针k，左指针j至少需要满足的位置，
        差值就是对于这个k，可选的j的可能种数
        两个小优化：
        1. 当固定最大边后，若剩余两条最大边之和不大于最大边，一定无法组成三角形，直接考虑前一个最大边
        2. 当固定最大边后，若剩余两条最小边之和大于最大边，任意组合均能组成三角形
        
        时间复杂度：O(n^2)
        空间复杂度：O(1)
        """
        ans = 0
        nums.sort()
        n = len(nums)
        for i in range(n-1,1,-1):
            x = nums[i]
            if x >= nums[i-2]+nums[i-1]:
                continue
            if x < nums[0]+nums[1]:
                ans += i*(i-1)//2
                continue
            j,k = 0, i-1
            while j < k:
                s = nums[j] + nums[k]
                if s <= x:
                    j += 1
                else:
                    ans += k-j
                    k -= 1
        
        return ans
# @lc code=end

