def group(s):
    L = []
    last = "@"
    for e in s:
        if e == last:
            continue
        last = e
        L.append(e)
    return L


def set_dp(m):
    dp = [[1 << 31] * m for _ in range(m)]
    for i in range(m):
        dp[i][i]=1
    return dp


class Solution:
    def set_last_seen(self):
        last = {}
        filtered = self.filtered
        m = len(filtered)
        for i in range(m - 1, -1, -1):
            char = filtered[i]
            self.nex[i] = last.get(char, -1)
            last[char] = i
        return last

    def fill_ins(self, length, start):
        end = start + length - 1
        resL = self.dp[start + 1]
        res=resL[end] + 1
        next_pos = self.nex[start]
        while next_pos != -1 and next_pos <= end:
            altres = self.dp[start][next_pos - 1]
            if next_pos + 1 <= end:
                altres += self.dp[next_pos + 1][end]
            if altres <= res:
                res = altres
            next_pos=self.nex[next_pos]
        self.dp[start][end] = res

    def fill_table(self):
        m = len(self.filtered)
        for length in range(2, m + 1):
            for start in range(m - length + 1):
                self.fill_ins(length,start)

    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0
        self.filtered = group(s)
        m = len(self.filtered)
        self.nex = [-1] * m
        self.dp = set_dp(m)
        self.last = self.set_last_seen()
        self.fill_table()
        return self.dp[0][~0]
