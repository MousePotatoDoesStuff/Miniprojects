from collections import deque


class MyStack:

    def __init__(self):
        self.A=deque()
        self.B=deque()
        self.al=0
        self.bl=0

    def push(self, x: int) -> None:
        self.B.append(x)
        if self.bl>min(self.al,3):
            self.A.append(self.B.popleft())
            self.al+=1
        else:
            self.bl+=1
        return


    def pop(self) -> int:
        for i in range(self.bl-1):
            self.B.append(self.B.popleft())
        res = self.B.popleft()
        self.bl-=1
        if self.bl==0:
            x=self.al//2
            for i in range(x):
                self.B.append(self.A.popleft())
            self.A,self.B=self.B,self.A
            self.al,self.bl=x,self.al-x
        return res


    def top(self) -> int:
        for i in range(self.bl-1):
            self.B.append(self.B.popleft())
        res=self.B.popleft()
        self.B.append(res)
        return res

    def empty(self) -> bool:
        return self.bl==0


def main():
    return


if __name__ == "__main__":
    main()
