SQR5 = 5.0 ** 0.5


def CalculateSequence(C, R, p, rl=3):
    n = min(len(C), len(R))
    res = 0
    for i in range(n):
        res += C[i] * (R[i] ** p)
    return round(res, rl)


def test1():
    a = (1 + SQR5) / 2
    b = (1 - SQR5) / 2
    C = [1.0 / SQR5, -1.0 / SQR5]
    R = [a, b]
    print([CalculateSequence(C, R, i) for i in range(10)])
    return


def test2():
    a = (1 + SQR5) / 2
    b = (1 - SQR5) / 2
    C = [a ** 2 / SQR5, -b ** 2 / SQR5, -1]
    R = [a, b, 1]
    # print([int(CalculateSequence(C, R, i)) for i in range(10)])
    for i in range(0,100,10):
        print(i,2**i-1,int(CalculateSequence(C, R, i)))
    return


def main():
    test1()
    test2()
    return


if __name__ == "__main__":
    main()
