from typing import *
import inspect


INF=1<<31
def merge(robot: list, factory: list):
    data = {}
    while robot:
        e = robot.pop()
        data[e] = -1
    while factory:
        e, v = factory.pop()
        v += data.get(e, 0)
        data[e] = v
    L = [E for E in data.items() if E[1] != 0]
    L.sort()
    return L


def setmin(D, k, v):
    if k not in D or D[k] > v:
        D[k] = v


def step(best: dict, delta: int, value: int):
    new_best = {0: INF}
    if value >= 0:
        for diff, res in best.items():
            if diff < 0:
                filled = min(-diff, value)
                res += delta * filled
            diff += value
            new_best[diff] = res
    else:
        for diff, res in best.items():
            setmin(new_best, min(diff, 0) - 1, res)
            if diff <= 0:
                continue
            new_res = res + delta * diff
            diff -= 1
            setmin(new_best, diff, new_res)
    new_best[0] = min([v for e, v in new_best.items() if e >= 0])
    return new_best


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        merged = merge(robot, factory)
        X = {0: 0}
        last = 0
        for position, value in merged:
            X = step(X, position - last, value)
            print("{}->{} ({}): {}".format(last, position, value, X))
            last = position
        RES = [v for k, v in X.items() if k >= 0]
        return min(RES)

    main = minimumTotalDistance


TESTS = [
    (
        ([670355988,403625544,886437985,224430896,126139936,-477101480,-868159607,-293937930],
         [[333473422,7],[912209329,7],[468372740,7],[-765827269,4],[155827122,4],[635462096,2],[-300275936,2],[-115627659,0]]),
        6
    )
    ,
    (
        ([0, 4, 6], [[2, 2], [6, 2]]),
        4
    )
]


def do_tests(tests, only_show_errors=True):
    """

    :param tests:
    :param only_show_errors:
    """
    SOL = Solution()
    count = 0
    for i, (args, true_res) in enumerate(tests):
        res = SOL.main(*args)
        count += res == true_res
        if only_show_errors and res == true_res:
            continue
        print(f"Test {i + 1}")
        print("Got {} ({})".format(res, type(res)))
        print("Expected {} ({})".format(true_res, type(true_res)))
    print(f"{count} out of {len(tests)} tests passed")


def main():
    """

    :return:
    """
    do_tests(TESTS)
    return


if __name__ == "__main__":
    main()
