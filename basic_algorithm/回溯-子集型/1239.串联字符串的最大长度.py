#
# @lc app=leetcode.cn id=1239 lang=python3
#
# [1239] 串联字符串的最大长度
#

# @lc code=start
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """
        子集型回溯。每个词选/不选
        """
        ans = 0
        path = []
        n = len(arr)
        def dfs(i):
            if i == n:
                nonlocal ans
                ans = max(ans,sum([len(x) for x in path]))
                return
            # 如果不重复，可以选
            s = "".join(path)
            cnt = Counter([c for c in s])
            flag = True
            for ch in arr[i]:
                cnt[ch] += 1
                if cnt[ch] == 2:
                    flag = False
                    break
            if flag:
                path.append(arr[i])
                dfs(i+1)
                path.pop()
            # 不选
            dfs(i+1)
        dfs(0)
        return ans
# @lc code=end

# ["aa","bb"]