class LinkNode:
    def __init__(self, value:int, keys:set, pre, nex):
        self.value:int = value
        self.keys:set=keys
        self.pre:LinkNode = pre
        self.nex:LinkNode = nex


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def insNode(self,pre,nex,val):
        new = LinkNode(val, set(), pre, nex)
        if pre:
            pre.nex=new
        else:
            self.first=new
        if nex:
            nex.pre=new
        else:
            self.last=new
        return new

    def addOne(self, key):
        if self.first and self.first.value == 1:
            self.first.keys.add(key)
            return self.first
        self.first = self.insNode(None,self.first,1)
        self.first.keys.add(key)
        return self.first

    def remove(self,node):
        pre = node.pre
        nex = node.nex
        if pre:
            pre.nex = nex
        else:
            self.first = nex
        if nex:
            nex.pre = pre
        else:
            self.last = pre

    def remNode(self, node:LinkNode, key):
        node.keys-={key}
        if not node.keys:
            self.remove(node)
            return node.pre, None, node.nex
        return node.pre, node, node.nex

    def ascNode(self, node, key):
        if node is None:
            return self.addOne(key), False
        pre, cur, nex = self.remNode(node,key)
        pre = cur if cur else pre
        newval = node.value + 1
        if not nex or nex.value != newval:
            nex=self.insNode(pre,nex,newval)
        nex.keys.add(key)
        return nex, cur is None

    def descNode(self, node, key):
        pre, cur, nex = self.remNode(node, key)
        nex = cur if cur else nex
        newval = node.value - 1
        if newval==0:
            return None, cur is None
        if not pre or pre.value != newval:
            pre=self.insNode(pre,nex,newval)
        pre.keys.add(key)
        return pre, cur is None

    def printAll(self):
        cur = self.first
        while cur:
            print(f"{cur.value}:{str(cur.keys)}->",end="")
            cur = cur.nex
        print()
        cur = self.last
        while cur:
            print(f"{cur.value}:{str(cur.keys)}<-",end="")
            cur = cur.pre
        print()
        return

    def getMax(self):
        return max(self.last.keys) if self.last else ""

    def getMin(self):
        return max(self.first.keys) if self.first else ""


class AllOne:

    def __init__(self):
        self.D = dict()
        self.RD = dict()
        self.commons=LinkedList()

    def inc(self, key: str) -> None:
        count=self.D.get(key,0)
        node=self.RD.get(count,None)
        newnode, isE=self.commons.ascNode(node,key)
        if isE:
            self.RD.pop(count)
        count+=1
        self.RD[count]=newnode
        self.D[key]=count
        print(self.D)
        print(self.RD.keys())
        self.commons.printAll()
        return

    def dec(self, key: str) -> None:
        count=self.D.get(key,0)
        node=self.RD[count]
        newnode, isE=self.commons.descNode(node,key)
        if isE:
            self.RD.pop(count)
        if count==1:
            return
        count-=1
        self.RD[count]=newnode
        self.D[key]=count
        print(self.D)
        print(self.RD.keys())
        self.commons.printAll()
        return


    def getMaxKey(self) -> str:
        return self.commons.getMax()


    def getMinKey(self) -> str:
        return self.commons.getMin()

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()