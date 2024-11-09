# https://levelup.gitconnected.com/10-ways-to-write-better-python-codes-55fc862ab0ef
from collections import Counter, deque


def generatorExample(test: list[int]):
    """

    :param test:
    :return:
    """
    for e in test:
        s = str(e) * e
        yield s
    return


def tip1():
    """
    Save memory using generators.
    # for line in open(filepath, r)
    """
    X = [i for i in range(1, 11)]
    for e in generatorExample(X):
        print(e)


def tip2():
    """
    Use setdefault, not just getdefault.
    """
    X = {1: 1}
    Y = [X.setdefault(i, 0) for i in range(3)]
    print(X, Y)


def tip3():
    """
    Use dictionaries instead of if-elif
    """

    def if_zero():
        print('Nothing is here')

    def if_one():
        print('One thing is here')

    def if_more():
        print('Multiple things are here')

    D = {0: if_zero, 1: if_one}
    n = int(input("Thing amount:"))
    D.get(n, if_more)()


def tip4():
    """
    Use this.
    :return:
    """
    X = Counter("banana")
    for e, v in X.items():
        print(e, ":", v)
    return


def memo_collatz(n: int, store: dict[int, int]):
    """

    :param n:
    :param store:
    :return:
    """
    store[1] = 0
    cur = n
    k = 0
    while cur != 1:
        if cur in store:
            k += store[cur]
            break
        cur = [cur // 2, cur * 3 + 1][cur % 2]
        k += 1
    store[n] = k
    cur = n
    while cur not in store:
        store[cur] = k
        cur = [cur // 2, cur * 3 + 1][cur % 2]
        k -= 1
    return store[n]



def tip5():
    """
    Use memos as a space-for-time tradeoff.
    :return:
    """
    return

def main():
    tip4()
    return


if __name__ == "__main__":
    main()
