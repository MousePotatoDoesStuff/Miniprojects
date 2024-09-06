from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)+"->"+str(self.next)
def initListNodes(L:List):
    cur=None
    while L:
        e=L.pop()
        cur=ListNode(e,cur)
    return cur

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Remove elements in linked list that are present in array.
        :param nums: The array.
        :param head: The linked list.
        :return: The edited linked list.
        """
        nums = set(nums)
        arch = ListNode(0, head)
        last = arch
        while head:
            if head.val in nums:
                head=head.next
                last.next = head
            else:
                last=head
                head=last.next
        return arch.next
    main = modifiedList


TESTS = [
    (([1,2,3],[1,2,3,4,5]), [4,5]),
    (([], []), "test")
]


def do_tests(tests):
    """

    :param tests:
    """
    SOL = Solution()
    for i, (args, true_res) in enumerate(tests):
        args=args[0],initListNodes(args[1])
        print(f"Test {i + 1}")
        res = SOL.main(*args)
        print("Got {} ({})".format(res, type(res)))
        print("Expected {} ({})".format(true_res, type(true_res)))


def main():
    """

    :return:
    """
    do_tests(TESTS)
    return


if __name__ == "__main__":
    main()
