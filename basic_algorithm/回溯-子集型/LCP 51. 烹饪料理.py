#
# @lc app=leetcode.cn id=LCP_51 lang=python3
#
# [LCP 51] 烹饪料理
# https://leetcode.cn/problems/UEcfPD/
#

# @lc code=start
class Solution:
    def perfectMenu(self, materials: List[int], cookbooks: List[List[int]], attribute: List[List[int]], limit: int) -> int:
        """
        子集型回溯。由于限定了每种料理只能做一次，对于每种料理只有做/不做两种选择
        """
        ans = -1
        path = []
        n = len(cookbooks)
        def dfs(i,ys,materials):
            if i == n:
                if ys >= limit:
                    nonlocal ans
                    ans = max(ans, sum([ attribute[cb][0] for cb in path ]))
                return
            # 如果食材足够，可以做
            temp = [mt - cost for mt,cost in zip(materials, cookbooks[i])]
            if min(temp) >= 0:
                path.append(i)
                dfs(i+1, ys+attribute[i][1], temp)
                path.pop()
            # 不做
            dfs(i+1, ys, materials)
        dfs(0,0,materials)
        return ans
# @lc code=end

