def anagram(s):
    n = len(s)
    D = dict()
    for e in s:
        D[e] = D.get(e, 0) + 1
    X = [('', D.copy())]
    for i in range(n):
        Y = []
        for (word, rem) in X:
            rem:dict
            els=list(rem.keys())
            els.sort()
            for el in els:
                new = rem.copy()
                new:dict
                new_el_v=rem[el]-1
                if new_el_v==0:
                    new.pop(el)
                else:
                    new[el]=new_el_v
                Y.append((word+el,new))
        X=Y
    return [e[0] for e in X]


def main():
    inp=input('->')
    res=anagram(inp)
    for e in res:
        print(e)
    return


if __name__ == "__main__":
    main()
