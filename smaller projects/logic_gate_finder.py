tuple_to_bin = lambda T:int(''.join([str(int(e))for e in T]),2)
bin_to_tuple = lambda b,n:[
    lambda b:(0,),
    lambda b:(b,),
    lambda b:(list(bin_to_tuple(b//2,n-1))+[b%2])
][(n>0)+(n>1)](b)

def process(gate,data,check=True):
    if check and len(gate)<(1<<len(data)):
        raise Exception("Too many inputs!")
    b=tuple_to_bin(data)
    return gate[b]

def generate_input(gate,data):
    if len(gate)<(1<<len(data)):
        raise Exception("Too many inputs!")
    M=[data]
    for i in range(len(data)):
        if M[0][i] in [0,1]:
            continue
        Y=[]
        for E in M:
            X=list(E)
            X[i]=0
            Y.append(tuple(X))
            X[i]=1
            Y.append(tuple(X))
        M=Y
    R=[process(gate,E) for E in X]
    return R


class LogicGateNaiveGroup:
    def __init__(self,size,safety_block=10):
        if size>safety_block:
            raise Exception("Too big!")
        self.size=size
        X=[[]]
        for i in range(self.size):
            Y=[]
            for E in X:
                Y.extend([E+[0],E+[1]])
        self.variants=[tuple(E) for E in X]
        return


def main():
    gate=(0,0,0,1)
    res=process(gate,[0,1])
    for i in range(4):
        print(process(gate,bin_to_tuple(i,2)))
    return


if __name__ == "__main__":
    main()
