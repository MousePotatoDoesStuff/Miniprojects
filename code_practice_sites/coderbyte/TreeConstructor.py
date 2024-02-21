class TreeNode:
    def __init__(self,value):
        self.value=value
        self.parent=None
        self.children=[]
    def add_child(self,key):
        if len(self.children)==2:
            return False
        self.children.append(key)
        return True
    def add_parent(self,key):
        if self.parent is not None:
            return False
        self.parent=key
        return True


def TreeConstructor(strArr):
    nodes=dict()
    rootless=set()
    for E in strArr:
        L=E[1:][:-1].split(',')
        a,b=[int(e)for e in L]
        if a not in nodes:
            rootless.add(a)
            nodes[a] = TreeNode(a)
        if b not in nodes:
            rootless.add(b)
            nodes[b]=TreeNode(b)
        A=nodes[a]
        B=nodes[b]
        if A.add_parent(b):
            rootless.remove(a)
        else:
            return False
        if not B.add_child(a):
            return False
    n=len(nodes)
    if len(rootless)>1:
        return False
    X=[min(rootless)]
    used=set()
    while len(X)>0:
        Y=[]
        for e in X:
            n-=1
            if e in used:
                return False
            Y.extend(nodes[e].children)
            used.add(e)
        X=Y
    return True


# keep this function call here


def main():
    print(TreeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]))
    print(TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"]))


if __name__ == "__main__":
    main()
