#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        子集型回溯
        """
        if len(s)<4 or len(s)>12:
            return []
        ans = []
        path = []
        n = len(s)
        def dfs(i,start,cnt):
            if i == n:
                if cnt == 4:
                    ans.append(".".join(path))
                return
            if cnt == 3:
                x = s[start:]
                if int(x)>255 or (s[start]=="0" and start!=n-1):
                    return
                path.append(x)
                dfs(n,n,cnt+1)
                path.pop()
                return
            if i-start>2:
                return
            if i<n-1 and s[start]!="0":
                dfs(i+1,start,cnt)
            x = s[start:i+1]
            if int(x)>255:
                return
            path.append(x)
            dfs(i+1,i+1,cnt+1)
            path.pop()
        dfs(0,0,0)
        return ans
# @lc code=end

