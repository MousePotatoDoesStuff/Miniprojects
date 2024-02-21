class Solution:
    def longestFor(self,paths):
        L=list(paths.keys())
        if len(L)==1:
            return 1,1
        L.sort()
        a=L[-1]
        if paths[a]>1:
            return a,a*2-1
        b=L[-2]
        return a,a+b-1
    def longestPath(self, parent: List[int], s: str) -> int:
        n=len(s)
        children=[0 for e in s]
        for i in range(1,n):
            j=parent[i]
            if s[j]==s[i]:
                parent[i]=-1
            else:
                children[j]+=1
        cur=[i for i in range(n) if children[i]==0]
        paths=[{1:1} for e in s]
        best=0
        while len(cur)!=0:
            nex=[]
            for e in cur:
                longest_part,longest_full=self.longestFor(paths[e])
                best=max(best,longest_full)
                f=parent[e]
                if f==-1:
                    continue
                longest_part+=1
                children[f]-=1
                if children[f]==0:
                    nex.append(f)
                paths[f][longest_part]=paths[f].get(longest_part,0)+1
            cur=nex
        return best



def main():
    return


if __name__ == "__main__":
    main()
