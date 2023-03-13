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
    mode = input('Mode:')
    if mode == '1':
        a = float(input('a:'))
        b = float(input('b:'))
        val = a / b
    else:
        val = float(input('v:'))
    R = closest_ratio(val, minlog=L)
    print(R)
    for e in L:
        print(e)
    return


if __name__ == "__main__":
    main()
