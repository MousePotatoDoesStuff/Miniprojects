def BracketMatcher(strParam):
    x=0
    for e in strParam:
        if e=='(':
            x+=1
        elif e==')':
            x-=1
        if x<0:
            return 0
    return int(x==0)


def main():
    return


if __name__ == "__main__":
    main()
