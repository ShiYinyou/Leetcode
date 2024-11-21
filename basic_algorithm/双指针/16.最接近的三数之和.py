#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        以 15.三数之和 为基础进行调整
        三个小优化：
        1. 若nums[i]==nums[i-1]，不需要再次计算，可以直接枚举下一个i
        2. 固定i后，最小的三数之和都大于target，之后不可能再出现更接近的，直接break
        3. 固定i后，最大的三数之和都小于target，之后对于这个i不可能出现更接近的，枚举下一个i
        
        时间复杂度：O(n^2)
        空间复杂度：O(1)
        """
        nums.sort()
        n = len(nums)
        min_diff = inf
        for i in range(n-2):
            x = nums[i]
            if i>0 and x==nums[i-1]:
                continue
            t = x + nums[i+1] + nums[i+2]
            if t > target:
                if t - target < min_diff:
                    ans = t
                break
            t = x + nums[-1] + nums[-2]
            if t < target:
                if target - t < min_diff:
                    ans = t
                    min_diff = target - t
                continue
            j, k = i+1, n-1
            while j < k:
                t = x + nums[j] + nums[k]
                if t > target:
                    if t - target < min_diff:
                        ans = t
                        min_diff = t - target
                    k -= 1
                elif t < target:
                    if target - t < min_diff:
                        ans = t
                        min_diff = target - t
                    j += 1
                else:
                    return target
        return ans
# @lc code=end

