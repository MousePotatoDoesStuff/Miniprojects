class Solution:
    def leetcode_0_204(self, n: int) -> int:
        if n < 3:
            return 0
        nexts = {}
        count = 1
        for i in range(3, n, 2):
            if i in nexts:
                for e in nexts.pop(i):
                    f = i + e
                    L = nexts.get(f, [])
                    L.append(e)
                    nexts[f] = L
            else:
                q = i ** 2
                count+=1
                if q < n:
                    nexts[q] = [i * 2]
        return count


def main():
    print(Solution().leetcode_0_204(628545))
    return


if __name__ == "__main__":
    main()
