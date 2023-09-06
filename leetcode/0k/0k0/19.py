# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: object = 0, nex=None):
        self.val = val
        self.next = nex


from typing import Optional


class Solution:
    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0

    def add_link(self, current):
        if self.first is None:
            self.first = current
        else:
            self.last.next = current
        self.last = current
        self.count -= 1
        if self.count < 0:
            self.first = self.first.next
            self.count = 0
        return

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.first = None
        self.last = None
        self.count = n + 1
        cur = head
        while cur is not None:
            self.add_link(ListNode(cur))
            cur=cur.next
        if self.first is None:
            return None
        if self.count>0:
            if self.count==1:
                return head.next
            return None
        cur=self.first.val
        res=cur.next
        cur.next=res.next
        return head


def generateList(L):
    head = ListNode(-1, None)
    tail = head
    for e in L:
        tail.next = ListNode(e, None)
        tail = tail.next
    return head.next


def test(L, n):
    head = generateList(L)
    sol = Solution()
    return sol.removeNthFromEnd(head, n)


def main():
    X = [
        ([1, 2, 3, 4, 5], 2),
        ([1],1),
        ([1, 2, 3, 4, 5], 5)
    ]
    for (L, n) in X:
        print(L, n, test(L, n).val)
    return


if __name__ == "__main__":
    main()
