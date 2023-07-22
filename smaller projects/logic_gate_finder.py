tuple_to_bin = lambda T: int(''.join([str(int(e)) for e in T]), 2)
bin_to_tuple = lambda b, n: [
    lambda b: (0,),
    lambda b: (b,),
    lambda b: (list(bin_to_tuple(b // 2, n - 1)) + [b % 2])
][(n > 0) + (n > 1)](b)


def rearrange_indices(number, size, keylist):
    T = bin_to_tuple(number, size)
    V = tuple([keylist[T[i]] for i in range(size)])
    return tuple_to_bin(V)


def rearrange_gate(gate, size, indices):
    n = len(gate)
    M = [(bin_to_tuple(i, size), gate[i]) for i in range(len(gate))]
    print(M)
    N = [(tuple([T[indices[i]] for i in range(size)]), v) for T, v in M]
    print(N)
    N.sort()
    print(N)
    return [e[1] for e in N]


def process(gate, data, check=True):
    if check and len(gate) < (1 << len(data)):
        raise Exception("Too many inputs!")
    b = tuple_to_bin(data)
    return gate[b]


def generate_perms(data):
    M = [data]
    for i in range(len(data)):
        if M[0][i] in [0, 1]:
            continue
        Y = []
        for E in M:
            X = list(E)
            X[i] = 0
            Y.append(tuple(X))
            X[i] = 1
            Y.append(tuple(X))
        M = Y
    return M


def generate_perms_marked(data):
    variants={E:[] for E in set(data)}
    for i in range(len(data)):
        variants[data[i]].append(i)
    variants.pop(0)
    variants.pop(1)
    L=list(variants.keys())
    L.sort()
    M = [data]
    for var in L:
        indices=variants[var]
        N=[]
        for E in M:
            X=list(E)
            for value in [0,1]:
                for e in indices:
                    X[e]=value
                N.append(tuple(X))
        M=N
    return M



def generate_input(gate, data, mode=False):
    if len(gate) < (1 << len(data)):
        raise Exception("Too many inputs!")
    M = generate_perms_marked(data) if mode else generate_perms(data)
    R = [process(gate, E) for E in M]
    return R


def generate_all_inputs(gate,values): #[0,1,'a']
    X=[[]]
    for e in gate:
        Y=[]
        for f in values:
            for cur in X:
                Y.append(cur+[f])
        X=Y
    X=[tuple(E)for E in X]
    for e in X:
        print(e)
    return


def test_variant(gate, data, goal):
    X = generate_input(gate, data)
    print(X)
    print(goal)
    return


class LogicGateNaiveGroup:
    def __init__(self, size, safety_block=10):
        if size > safety_block:
            raise Exception("Too big!")
        self.size = size
        X = [[]]
        for i in range(1 << self.size):
            Y = []
            for E in X:
                Y.extend([E + [0], E + [1]])
            X = Y
        self.variants = [tuple(E) for E in X]
        return

    def test_all_variants(self):
        pass


def test_gate():
    gate = (0, 0, 1, 0)
    for i in range(4):
        print(process(gate, bin_to_tuple(i, 2)))
    print(generate_perms([-1, 1]))
    print(generate_input(gate, [-1, 1]))
    gate2 = (0, 0, 1, 0, 0, 0, 0, 0)
    gate3 = rearrange_gate(gate2, 3, [1, 2, 0])
    print(gate2)
    print(gate3)

def test_genperms():
    data=[0,1,'a',1,'b','a',0]
    print(generate_perms(data))
    print(generate_perms_marked(data))

def test_lgng():
    lgng = LogicGateNaiveGroup(3)
    gate = lgng.variants[3]
    print(gate,test_variant(gate, [0, 0, 0], [0,0]))


def main():
    test_genperms()
    return


if __name__ == "__main__":
    main()
