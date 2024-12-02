from collections import defaultdict
from typing import *
import inspect


class Link:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def makeGraph(pairs: List[List[int]]):
    nex = {e: [] for e, _ in pairs}
    count = defaultdict(int)
    a = 0
    while pairs:
        a, b = pairs.pop()
        nex[a].append(b)
        count[a] += 1
        count[b] -= 1
    start = a
    end = a
    used = 0
    for e, v in count.items():
        if v > 0:
            start = e
            used += 1
        elif v < 0:
            end = e
            used += 1
        if used == 2:
            break
    nex.setdefault(end, []).append(-1)
    nex[-1] = [start]
    for V in nex.values():
        V.sort(reverse=True)
    return nex, start, end


def traverseStep(nexdict: dict, ind: int, unused: dict):
    intersection = unused[ind]
    start = intersection.val
    nex = nexdict[start].pop()
    lastnode = intersection
    internext = intersection.next

    while nex != start:
        cur = nex
        node: Link = Link(cur)
        lastnode.next = node
        lastnode = node

        L = nexdict[node.val]
        nex = L.pop()
        if L:
            unused[cur] = node
            continue
        nexdict.pop(cur)
        if cur in unused:
            unused.pop(cur)

    lastnode.next = Link(start, internext)
    if not nexdict[start]:
        unused.pop(start)
        nexdict.pop(start)
    return lastnode.next


def breakChain(start: Link):
    while start.next.val != -1:
        start = start.next
    true_start = start.next.next
    start.next = None
    return true_start


def listLinks(start: Link) -> List[List[int]]:
    L = []
    while start.next:
        if start.val!=start.next.val:
            L.append([start.val, start.next.val])
        start = start.next
    return L


def traverse(nexdict: dict, start: int) -> List[List[int]]:
    startnode = Link(start)
    startnode.next = startnode
    unused = {start: startnode}
    while nexdict:
        cur = min(unused)
        traverseStep(nexdict, cur, unused)
    startnode = breakChain(startnode)
    L = listLinks(startnode)
    return L


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        nexdict, start, extraLink = makeGraph(pairs)
        RES = traverse(nexdict, start)
        return RES

    main = validArrangement


TESTS = [
    (
        [[5, 1], [4, 5], [11, 9], [9, 4]]
        ,
        []
    )
    ,
    (
        [[1, 2], [1, 3], [2, 1]]
        ,
        []
    )
]


def do_tests(tests, only_show_errors=True):
    """

    :param tests:
    :param only_show_errors:
    """
    SOL = Solution()
    count = 0
    print("Running...")
    for i, (arg, true_res) in enumerate(tests):
        true_res={tuple(e) for e in arg}
        res = SOL.main(arg)
        printout=str(res)
        is_good=False
        end=res[-1][-1]
        while res:
            E=tuple(res.pop())
            if E[1]!=end:
                break
            if E not in true_res:
                break
            end=E[0]
            true_res.remove(E)
        else:
            is_good=not true_res
        count += is_good
        if only_show_errors and is_good:
            continue
        print(f"Test {i + 1}")
        print(f"Got {printout}, not good")
    print(f"{count} out of {len(tests)} tests passed")


def main():
    """

    :return:
    """
    do_tests(TESTS)
    return


if __name__ == "__main__":
    main()
