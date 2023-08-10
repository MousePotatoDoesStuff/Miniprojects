from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}
        for e in s:
            if e in pairs.keys():
                stack.append(e)
            else:
                if len(stack) == 0 or pairs[stack.pop()] != e:
                    return False
        return len(stack) == 0


def main():
    X = Solution()
    print(X.isValid('()'))
    return


if __name__ == "__main__":
    main()
