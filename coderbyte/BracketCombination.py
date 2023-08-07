def BracketCombinationsNaive(num):
  X=[(num,0)]
  last=0
  while len(X)>0:
    Y=[]
    for (a,b) in X:
      if a>0:
        E=(a-1,b+1)
        Y.append(E)
      if b>0:
        E=(a,b-1)
        Y.append(E)
    last=len(X)
    X=Y
  return last

def BracketCombinations(num):
    X=dict()
    L=[(num,0)]
    while True:
        M=[]
        for E in L:
            pass




if __name__ == "__main__":
    for i in range(10):
        print(BracketCombinationsNaive(i))
