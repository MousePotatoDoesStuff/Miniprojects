from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        cur=root,[head]
        L=[cur]
        while L:
            tree_el,steps=L.pop()
            if tree_el is None:
                continue
            nex_steps=[]
            for e in steps:
                if tree_el.val!=e.val:
                    continue
                nex=e.nex
                if nex is None:
                    return True
                nex_steps.append(nex)
            A=tree_el.left,nex_steps
            B=tree_el.right,nex_steps
            L+=[A,B]
        return False
    main = isSubPath()


TESTS = [
    (([0, 1], 1), "test"),
    (([0, 1], 2), "test")
]


def do_tests(tests):
    """

    :param tests:
    """
    SOL = Solution()
    for i, (args, true_res) in enumerate(tests):
        print(f"Test {i + 1}")
        res = SOL.main(*args)
        print("Got {} ({})".format(res, type(res)))
        print("Expected {} ({})".format(true_res, type(true_res)))


def main():
    """

    :return:
    """
    return


if __name__ == "__main__":
    main()
