from typing import *
import inspect


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.count = 1

    def try_left(self, val):
        if self.left is None:
            self.left = TreeNode(val)
            return None
        return self.left

    def try_right(self, val):
        if self.right is None:
            self.right = TreeNode(val)
            return None
        return self.right

    def try_child(self, val):
        self.count += 1
        if val < self.val:
            return self.try_left(val)
        elif val > self.val:
            return self.try_right(val)


class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        cur: TreeNode = self.root
        while cur:
            cur = cur.try_child(val)

    def get_less_count(self, val):
        if not self.root:
            return 0
        cur = self.root
        res = 0
        while cur:
            cur: TreeNode
            if val < cur.val:
                cur = cur.left
                continue
            if val == cur.val:
                res += cur.left.count if cur.left else 0
                cur: None = None
                continue
            res += cur.count
            res -= cur.right.count if cur.right else 0
            cur = cur.right
        return res

    def list(self):
        X = [(self.root, True)]
        RES = []
        while X:
            cur, active = X.pop()
            if not cur:
                continue
            cur: TreeNode
            if active:
                X.append((cur.left, True))
                X.append((cur, False))
                X.append((cur.right, True))
                continue
            RES.append((cur.val, cur.count))
        return RES


class MyCalendar:

    def __init__(self):
        self.starts = Tree()
        self.ends = Tree()

    def book(self, start: int, end: int) -> bool:
        a = self.ends.get_less_count(start + 0.5)
        b = self.starts.get_less_count(end)
        if a != b:
            return False
        self.starts.add(start)
        self.ends.add(end)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


def main():
    """

    :return:
    """
    return


if __name__ == "__main__":
    main()
