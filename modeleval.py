class ClassifierModel:
    def __init__(self, examples, matrix=False):
        if matrix:
            n = len(examples)
            self.matrix = examples
        else:
            n = 1
            for e in examples:
                for f in e:
                    n = max(n, f + 1)
            self.matrix = [[0 for i in range(n)] for j in range(n)]
            for el in examples:
                self.matrix[el[0]][el[1]] += 1
        self.n = n
        self.colsum = [0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                self.colsum[j] += self.matrix[i][j]
        self.rowsum = [sum(E) for E in self.matrix]
        self.allsum = sum(self.rowsum)
        return

    def make_submatrices(self, k):
        TP = self.matrix[k][k]
        FP = self.rowsum[k] - TP
        FN = self.colsum[k] - TP
        TN = self.allsum - FP - FN - TP
        return [[TP, FP], [FN, TN]]

    def micro(self):
        TM = [[0, 0], [0, 0]]
        for i in range(self.n):
            EM = self.make_submatrices(i)
            for j in range(2):
                for k in range(2):
                    TM[j][k] += EM[j][k]
        pm = TM[0][0] / (TM[0][0] + TM[0][1])
        rm = TM[0][0] / (TM[0][0] + TM[1][0])
        fm = 2 / (1 / pm + 1 / rm)
        return fm

def E1():
    M1 = [
        [30, 18, 3],
        [11, 25, 2],
        [4, 2, 5]
    ]
    M2 = [
        [35, 8, 3],
        [10, 25, 5],
        [0, 12, 2]
    ]
    M=[M1,M2][1]
    X = ClassifierModel(M,True)
    for i in range(3):
        print(X.make_submatrices(i))
    m1=X.micro()
    print(m1)
    L=[0]*len(M[0])
    for E in M:
        for i in range(len(E)):
            L[i]+=E[i]
    s=sum(L)
    print(L)
    X = ClassifierModel([[L[i]*L[j]/s for j in range(3)]for i in range(3)],True)
    for i in range(3):
        print(X.make_submatrices(i))
    m2=X.micro()
    print(m1-m2)
    return

def E2():
    e1=(2, 2, 2, 2, 2, 2, 1, 3, 1, 2, 2, 1, 3, 2, 2)
    e2=(1, 2, 2, 2, 3, 1, 1, 1, 2, 2, 3, 3, 3, 2, 2)
    L=[(e1[i],e2[i])for i in range(15)]
    X=ClassifierModel(L)
    print(X.matrix)
    for i in range(3):
        print(X.make_submatrices(i))
    print(X.micro())



def main():
    E1()
    return


if __name__ == "__main__":
    main()
