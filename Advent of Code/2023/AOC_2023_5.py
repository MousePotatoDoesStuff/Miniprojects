from pathlib import Path


def process_map(IN):
    L = IN.split("\n")
    RES = []
    for s in L[1:]:
        E = [int(e) for e in s.split()]
        E2 = (E[1], E[1] + E[2], E[0] - E[1])
        RES.append(E2)
    RES.sort()
    return RES


def process_all(IN):
    M = IN.split("\n\n")
    START = [int(e) for e in M[0].split()[1:]]
    MAPS = [process_map(e) for e in M[1:]]
    return START, MAPS


def solve1(IN):
    cur, maps = process_all(IN)
    cur.sort()
    for EL in maps:
        new = []
        last = cur[-1]
        EL.append((last + 1, last + 2, 0))
        pointer = 0
        f = EL[0]
        for e in cur:
            while f[1] <= e:
                pointer += 1
                f = EL[pointer]
            e2 = e
            if f[0] <= e:
                e2 += f[2]
            new.append(e2)
        cur = new
        cur.sort()
    return cur[0]


TESTVAL = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''


def solve2(IN):
    cur, maps = process_all(IN)
    cur2 = []
    temp = None
    for e in cur:
        if temp is None:
            temp = e
        else:
            cur2.append((temp, e))
            temp = None
    cur=cur2
    cur2=None
    cur.sort()
    print(cur)
    for EL in maps:
        new=[]
        E=cur.pop()
        F = EL.pop()
        while cur and EL:
            while F[0]>=E[1]:
                F = EL.pop()
            if F[1]<=E[0]:
                new.append((E[0],E[1]))
                E=nw
        new.append(cur)
        new.sort()
    return cur[0]


in_loc = "AOC_2023_{}.txt"
data = {'version': 2}


def main():
    num = Path(__file__).name.split('_')[-1][:-3]
    F = open(in_loc.format(num), 'r')
    IN = F.read()
    F.close()
    OUT1 = solve1(IN)
    print(OUT1)
    OUT2 = solve2(IN)
    print(OUT2)
    return


if __name__ == "__main__":
    main()
