from typing import *


class TreeNode:
    """
    treeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getChildrenSum(node: TreeNode):
    val = 0
    for e in [node.left, node.right]:
        if e:
            val += e.val
    return val


def setChild(node: TreeNode, child: TreeNode, isRight: bool):
    if isRight:
        node.right = child
    else:
        node.left = child


def getLevelSums(root: TreeNode):
    cur: list[TreeNode] = [root]
    levels = []
    while cur:
        cursum = 0
        nex = []
        for e in cur:
            cursum += e.val
            X = [e.left, e.right]
            nex += [e for e in X if e]
        cur = nex
        levels.append(cursum)
    return levels


def getCousinValues(root: TreeNode, levels: list[int]):
    arch = TreeNode(0, root)
    newarch = TreeNode(0)
    cur = root, 0, arch, newarch, False
    stack = [cur]
    while stack:
        E = stack.pop()
        print(E)
        cur, level, arch, newarch, side = E
        cousinval = levels[level] - getChildrenSum(arch)
        newnode = TreeNode(cousinval)
        setChild(newarch, newnode, side)
        isright = True
        for e in [cur.left, cur.right]:
            isright = not isright
            if not e:
                continue
            nex = e, level + 1, cur, newnode, isright
            stack.append(nex)
    return newarch.left


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levelsums = getLevelSums(root)
        res = getCousinValues(root, levelsums)
        return res

    main = replaceValueInTree


TESTS = [
    (
        ([5,4,9,1,10,None,7],),
        "test"
    )
]


def preprocess(args):
    tree=listToTree(args[0])
    return (tree,)

def postprocess(res):
    lis=treeToList(res)
    return lis


def do_tests(tests, only_show_errors=True):
    """

    :param tests:
    :param only_show_errors:
    """
    SOL = Solution()
    count = 0
    for i, (raw_args, true_res) in enumerate(tests):
        args=preprocess(raw_args)
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
