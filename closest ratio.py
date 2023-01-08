def closest_ratio(f, max_rem=0.01, minlog=None, limit=10000):
    for k in range(1, limit):
        a = f * k
        b = int(a)
        c = (a - b) / f
        if minlog is not None:
            if len(minlog) == 0 or minlog[-1][-1] >= c:
                minlog.append((k, b, c))
        if c <= max_rem:
            return k, b, c
    return None


def main():
    L = []
    R = closest_ratio(1171 / 655, minlog=L)
    print(R)
    for e in L:
        print(e)
    return


if __name__ == "__main__":
    main()
