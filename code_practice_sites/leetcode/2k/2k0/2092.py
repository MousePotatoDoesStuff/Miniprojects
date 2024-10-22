from typing import List


def Flatten(groups, a):
    b = groups[a]
    while groups[b] != b:
        groups[a] = b
        b = groups[b]
    return b


def AddLink(groups, a, b):
    groups[a] = groups.get(a, a)
    groups[b] = groups.get(b, a)
    ga = Flatten(groups, a)
    gb = Flatten(groups, b)
    if ga > gb:
        (a, ga), (b, gb) = (b, gb), (a, ga)
    Flatten(groups, b)
    return


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        times = set()
        meetingTimes = dict()
        while meetings:
            (a, b, time) = meetings.pop()
            L = meetingTimes.get(time, [])
            if a > b:
                a, b = b, a
            L.append((a, b))
            meetingTimes[time] = L
            times.add(time)
        times = list(times)
        times.sort(reverse=True)
        curSecret = {0, firstPerson}
        while times:
            time = times.pop()
            L = meetingTimes.pop(time)
            L.sort(reverse=True)
            groups={}
            print(len(L),end="->")
            while L:
                a,b=L.pop()
                AddLink(groups,a,b)
            print(len(groups))
            for e,v in groups.items():
                groups[e]=groups[v]
            sets={e:set() for e,v in groups.items() if e==v}
            for e,v in groups.items():
                sets[v].add(e)

            nexSecret=set()
            nexGroups=set()
            for e in curSecret:
                nexSecret.add(e)
                if e not in groups:
                    continue
                nexGroups.add(groups[e])
            for group in nexGroups:
                nexSecret|=sets[group]
            curSecret=nexSecret
        L = list(curSecret)
        L.sort()
        return L


def main():
    return


if __name__ == "__main__":
    main()
