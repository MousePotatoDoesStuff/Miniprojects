from typing import List


def leetcode_0_412(n: int) -> List[str]:  # fizzBuzz
    X=["" for i in range(n)]
    for (k,s) in [(3,"Fizz"),(5,"Buzz")]:
        for i in range(k-1,n,k):
            X[i]+=s
    return [e if e!="" else str(i+1) for (i,e) in enumerate(X)]


class Solution:
    pass


def main():
    return


if __name__ == "__main__":
    main()
