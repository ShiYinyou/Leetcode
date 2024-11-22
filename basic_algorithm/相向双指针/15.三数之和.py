#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        对数组排序后，通过对一个数进行遍历，可以将问题转化为两数之和
        需要注意对重复元素的处理
        两个trick：
        1. 固定i后，若此时与其他最小的两个数之和都大于0，那么之后一定没有解，可以直接退出循环
        2. 固定i后，若此时与其他最大的两个数之和都小于0，那么这个i一定没有解，直接进入下一轮循环
        
        时间复杂度：O(n^2) i循环O(n)，两数之和O(n)，排序开销O(nlgn)
        空间复杂度：O(1) 
        """
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            x = nums[i]
            if i>0 and x==nums[i-1]: # 去除掉第一个数重复的情况
                continue
            if x + nums[i+1] + nums[i+2] > 0:
                break # 最小的三数之和大于0，之后一定没有解
            if x + nums[n-2] + nums[n-1] < 0:
                continue # 与另外两个最大数之和小于0，对于这个i一定没有解
            j, k = i+1, n-1
            while j < k:
                y = x + nums[j] + nums[k]
                if y < 0:
                    j += 1
                elif y > 0:
                    k -= 1
                else:
                    ans.append([x,nums[j],nums[k]])
                    j += 1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while k>j and nums[k] == nums[k+1]:
                        k -= 1
        return ans
# @lc code=end

