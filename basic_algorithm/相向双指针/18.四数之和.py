#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    """
    固定一个元素后，转化为三数之和问题。
    注意tricks。

    时间复杂度：O(n^3)
    空间复杂度：O(1)
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for a in range(n-3):
            x = nums[a]
            if a>0 and x==nums[a-1]:
                continue
            if x+nums[a+1]+nums[a+2]+nums[a+3] > target:
                break
            if x+nums[-1]+nums[-2]+nums[-3] < target:
                continue
            # 内部是一个三数之和问题
            for b in range(a+1,n-2):
                y = nums[b]
                if b>a+1 and y==nums[b-1]:
                    continue
                if x+y+nums[b+1]+nums[b+2] > target:
                    break
                if x+y+nums[-1]+nums[-2] < target:
                    continue
                # 内部是一个两数之和问题
                c,d = b+1,n-1
                while c < d:
                    s = x+y+nums[c]+nums[d]
                    if s < target:
                        c += 1
                    elif s > target:
                        d -= 1
                    else:
                        ans.append([x,y,nums[c],nums[d]])
                        c += 1
                        while c<d and nums[c] == nums[c-1]:
                            c += 1
                        d -= 1
                        while c<d and nums[d] == nums[d+1]:
                            d -= 1
        return ans

# @lc code=end

