from typing import *
import inspect


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "X"
        left=self.serialize(root.left)
        right=self.serialize(root.right)
        if left+right=='XX':
            return "{}".format(root.val)
        res="{}:{}|{}".format(root.val,left,right)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        datalist=[]
        cur=""
        for e in data:
            if e in ":|":
                datalist.append(cur)
                if e==":":
                    datalist.append(e)
                cur=""
            else:
                cur+=e
        datalist.append(cur)
        stack=[]
        isReady=False
        while datalist:
            cur=datalist.pop()
            if cur==':':
                isReady=True
                continue
            cn=None if cur=='X' else TreeNode(int(cur))
            if isReady:
                left=stack.pop()
                right=stack.pop()
                cn.left=left
                cn.right=right
                isReady=False
            stack.append(cn)
        return stack[0]


def do_tests(tests, only_show_errors=True):
    """

    :param tests:
    :param only_show_errors:
    """
    SOL = Codec()
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
    CDC = Codec()
    A = '1000:X|-1000'
    B = CDC.deserialize(A)
    A = CDC.serialize(B)
    B = CDC.deserialize(A)
    A = CDC.serialize(B)
    print(A)
    return


if __name__ == "__main__":
    main()
