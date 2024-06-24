def preventChains(groups, a):
    X = [a]
    a = groups[a]
    if X[-1] == a:
        return a
    X.append(a)
    a = groups[a]
    while X[-1] != a:
        X.append(a)
        a = groups[a]
    while X:
        groups[X.pop()] = a
    return a


def pairs_to_groups(L):
    groups = dict()
    while L:
        (a, b) = L.pop()
        if a > b:
            a, b = b, a
        groups[a] = groups.get(a, a)
        groups[b] = groups.get(b, a)
        ga = preventChains(groups, a)
        gb = preventChains(groups, b)
        if ga > gb:
            (ga, a), (gb, b) = (gb, b), (ga, a)
        groups[gb] = ga
        groups[b] = ga
        print(groups)
    return groups


def groupsToSets(D: dict):
    res = {e: set() for e in D.values() if D[e] == e}
    for k in D:
        v = preventChains(k)
        res[v].add(k)
    return res


def main():
    L = [(1, 2), (3, 4), (4, 5), (0, 3)]
    D = pairs_to_groups(L)
    R = groupsToSets(D)
    print(R)
    return


if __name__ == "__main__":
    main()
