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

    def traverse(self, a, b, RES:list, cur=TreeNode(0.5)):
        if cur is None:
            return
        cur:TreeNode
        if cur.val==0.5:
            cur=self.root
        d=(cur.val>=b)-(cur.val<a)
        if d>=0:
            self.traverse(a,cur.val,RES,cur.left)
        if d==0:
            RES.append(cur.val)
        if d<=0:
            self.traverse(cur.val+1,b,RES,cur.right)
        return

    def extend(self, L, cur=TreeNode(0.5)):
        if not L:
            return
        if cur is None:
            return
        cur:TreeNode
        if cur.val==0.5:
            cur=self.root


class MyCalendar:

    def __init__(self):
        self.starts = Tree()
        self.ends = Tree()
        self.doublestarts = Tree()
        self.doubleends = Tree()

    def book(self, start: int, end: int) -> bool:
        a = self.doubleends.get_less_count(start + 0.5)
        b = self.doublestarts.get_less_count(end)
        if a != b:
            return False
        a = self.ends.get_less_count(start + 0.5)
        b = self.starts.get_less_count(end)
        if a != b:
            pass
            # get first start
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
