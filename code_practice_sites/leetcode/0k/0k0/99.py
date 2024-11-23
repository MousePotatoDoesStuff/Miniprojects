from typing import *
import inspect


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.last = TreeNode(-float('inf'))

    def checkElement(self, root):
        print(root.val,self.last.val)
        if root.val > self.last.val:
            return
        if not self.first:
            self.first = self.last
        self.second = root
        return

    def traverse(self, root: TreeNode):
        if root is None:
            return None
        self.traverse(root.left)
        self.checkElement(root)
        self.last=root
        self.traverse(root.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.traverse(root)
        self.first: TreeNode
        self.second: TreeNode
        self.first.val, self.second.val = self.second.val, self.first.val

    main = recoverTree


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
