from pathlib import Path


def solve(IN):
    return IN


in_loc = "AOC_2023_{}.txt"


def main():
    num=Path(__file__).name.split('_')[-1][:-3]
    F=open(in_loc.format(num),'r')
    IN=F.read()
    F.close()
    OUT = solve(IN)
    print(OUT)
    return


if __name__ == "__main__":
    main()
