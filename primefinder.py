def makelist(n, maxprimes=0):
    L = list()
    for i in range(2, n + 1):
        for e in L:
            if i % e == 0:
                break
        else:
            L.append(i)
            if len(L) == maxprimes:
                break
    return L


def main():
    L = makelist(int(2023.0 ** 0.5 + 1))
    print(L)
    for e in L:
        if 2023 % e == 0:
            print(e, 2023 // e)
    L=makelist(1000,42)
    print(L)
    return


if __name__ == "__main__":
    main()
