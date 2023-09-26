import bisect


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        letters = list(set(s))
        letters.sort()
        locations = {e: [] for e in letters}
        for i, e in enumerate(s):
            locations[e].append(i)
        res = []
        last = -1
        for e in letters:
            L = locations.pop(e)
            i = bisect.bisect(L, last)
            L.append(L[-1])
            loc= L[i]
            res.append((loc, e))
            last = max(last, loc)
        print(res)
        res.sort()
        return "".join([e[1] for e in res])


def main():
    SOL = Solution()
    res = SOL.removeDuplicateLetters("cbdabc")
    print(res)
    return


if __name__ == "__main__":
    main()
