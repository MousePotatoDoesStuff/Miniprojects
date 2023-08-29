class Solution:
    def bestClosingTime_complicated(self, customers: str) -> int: # 560/570/603 ms
        customers+='N'
        n=len(customers)
        c=0
        best=(0,0)
        open=True
        for i in range(n):
            if customers[i]=='N':
                if open:
                    open=False
                    if c<best[0]:
                        best=(c,i)
                c+=1
            else:
                c-=1
                open=True
            print(c,best)
        return best[1]

    def bestClosingTime_simple(self, customers: str) -> int:
        n=len(customers)
        c=0
        best=(0,0)
        for i in range(n):
            if customers[i]=='N':
                c+=1
            else:
                c-=1
                if c<best[0]:
                    best=(c,i+1)
        return best[1]




def main():
    return


if __name__ == "__main__":
    main()
