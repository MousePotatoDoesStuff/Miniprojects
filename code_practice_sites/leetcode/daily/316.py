import bisect


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        L=[]
        seen=set()
        last_dict={e:i for i,e in enumerate(s)}
        for i,e in enumerate(s):
            if e in seen:
                continue
            while L and e<L[-1] and i<last_dict[L[-1]]:
                seen.discard(L.pop())
            seen.add(e)
            L.append(e)
        return "".join(L)


def main():
    SOL = Solution()
    res = SOL.removeDuplicateLetters("cbdabc")
    print(res)
    return


if __name__ == "__main__":
    main()
