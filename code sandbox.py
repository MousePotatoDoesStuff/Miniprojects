from typing import List


class Charset:
    def __init__(self, s):
        self.chars = dict()
        self.repeating = None

    def add_char(self, e):
        re = False
        x = 1 + self.chars.get(e, 0)
        self.chars[e] = x
        if x > 1:
            self.repeating = e
        return

    def remove_chars(self, s):
        for e in s:
            x = -1 + self.chars.get(e, 0)
            self.chars[e] = x
        self.repeating = None
        return


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        CS = Charset('')
        longest = 0
        for end in range(len(s)):
            e=s[end]
            CS.add_char(e)
            if CS.repeating == e:
                longest = max(longest,end-start)
                newstart = s[start:].index(e) + start + 1
                CS.remove_chars(s[start:newstart])
                start = newstart
        longest=max(longest,len(s)-start)
        return longest


def main():
    X = Solution()
    print(X.lengthOfLongestSubstring('abcdefgh'))
    print('wasdwasd'[2:].index('w') + 2)
    return


if __name__ == "__main__":
    main()
