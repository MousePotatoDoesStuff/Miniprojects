class Element:
    def __init__(self, value, prev=None, nex=None):
        self.value = value
        self.prev: Element = prev
        self.next: Element = nex


class Queue:
    def __init__(self, data=None):
        self.first = None
        self.last = None
        if data is not None:
            self.first = self.last = Element(None)
            cur = None
            for e in data:
                self.last.next = cur = Element(e)
            self.last = cur
            self.first = self.first.next
        return

    def append(self, v):
        el = Element(v)
        if self.first is None:
            self.first = el
        else:
            self.last.next = el
        self.last = el
        return el

    def popleft(self, default=None):
        if self.first is None:
            return default
        el = self.first
        self.first = el.next
        return el.value

    def remove(self, el: Element):
        if el.prev is None:
            if self.first is el:
                self.first = el.next
        else:
            el.prev.next = el.next
        if el.next is None:
            if self.last is el:
                self.last = el.prev
        else:
            el.next.prev = el.prev
        return el.value


class Solution:
    def firstUniqChar(self, s: str) -> int:
        used = set()
        Q = Queue()
        D = dict()
        for (i, e) in enumerate(s):
            if e in D:
                v = D.pop(e)
                Q.remove(v)
                used.add(e)
            elif e not in used:
                v = Q.append(i)
                D[e] = v
        return Q.popleft()


def main():
    return


if __name__ == "__main__":
    main()
