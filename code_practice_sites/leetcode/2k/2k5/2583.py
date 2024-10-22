import heapq
from typing import *
import inspect


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.cur = []

    def step(self):
        nex = []
        res = 0
        for e in self.cur:
            e: TreeNode
            res += e.val
            chi = [e.left, e.right]
            nex += [e for e in chi if e is not None]
        self.cur = nex
        return res

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1
        self.cur = [root]
        stack = []
        while self.cur:
            cursum = self.step()
            heapq.heappush(stack, cursum)
            if len(stack) > k:
                heapq.heappop(stack)
        return stack[0] if len(stack) == k else -1

    main = kthLargestLevelSum


TESTS = [
    (
        ([0, 1], 1),
        "test")
    ,
    (
        ([0, 1], 2),
        "also test"
    )
]


def do_tests(tests, only_show_errors=True):
    """

    :param tests:
    :param only_show_errors:
    """
    SOL = Solution()
    count = 0
    for i, (args, true_res) in enumerate(tests):
        res = SOL.main(*args)
        count += res == true_res
        if only_show_errors and res == true_res:
            continue
        print(f"Test {i + 1}")
        print("Got {} ({})".format(res, type(res)))
        print("Expected {} ({})".format(true_res, type(true_res)))
    print(f"{count} out of {len(tests)} tests passed")


def main():
    """

    :return:
    """
    do_tests(TESTS)
    return


if __name__ == "__main__":
    main()
