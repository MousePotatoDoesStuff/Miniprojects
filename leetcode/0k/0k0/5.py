from collections import deque


class Solution:
    def convertConn(self,conn):
        n=0
        for e in conn:
            n*=10
            n+=e[0]*2+e[1]
        return n
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        conn=deque()
        for e in s:
            conn.append([True,True])
        best=(0,0)
        for diff in range(1,n):
            mode=diff&1
            last=conn.pop()
            nconn=deque()
            for i in range(n-diff-1,-1,-1):
                cur=conn.pop()
                ncur=cur[:]
                cur[mode]=last[mode] and s[i]==s[i+diff]
                if best[0]!=diff and cur[mode]:
                    best=(diff,i)
                nconn.appendleft(cur)
                last=ncur
            conn=nconn
        return s[best[1]:][:best[0]+1]


def main():
    SOL=Solution()
    res=SOL.longestPalindrome("AAAAB")
    print(res)
    res=SOL.longestPalindrome("AABAB")
    print(res)
    res=SOL.longestPalindrome("AAAAA")
    print(res)
    return


if __name__ == "__main__":
    main()
