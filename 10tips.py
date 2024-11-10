# https://levelup.gitconnected.com/10-ways-to-write-better-python-codes-55fc862ab0ef
from collections import Counter, deque
from dataclasses import dataclass


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
    Use setdefault, not just get.
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

def wrapper_fn(func):
    def wrapper():
        print("Starting function...")
        func()
        print("Ending function...")
        return
    return wrapper

@wrapper_fn
def wrapped_fn():
    print("Hello World")
    return


def tip6():
    """
    Wrap functions.
    :return:
    """
    wrapped_fn()
    return

@dataclass
class Clone:
    name: str
    iteration: int
    def next(self):
        return Clone(self.name,self.iteration+1)


def tip7():
    """
    Use dataclasses.
    :return:
    """
    X=Clone('Joe',1)
    Y=X.next()
    print(X,Y)
    return


def tip8():
    """
    Use match case (PYTHON 3.10 AND UP!)
    :return:
    """
    return


def tip9():
    """
    all and any operators
    :return:
    """
    A=[0,1,2]
    print(all(e>0 for e in A))
    print(all(e<3 for e in A))
    print(any(e>1 for e in A))
    print(any(e<-2 for e in A))
    return


def tip10():
    """
    comprehensions
    :return:
    """
    L=[0,1,2,1,0]
    T=tuple(e for e in L)
    S={e for e in T}
    D={e:L.index(e) for e in S}
    print(D)
    return


def main():
    tip6()
    return


if __name__ == "__main__":
    main()
