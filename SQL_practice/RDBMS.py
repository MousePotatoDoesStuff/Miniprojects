class RBDMS:
    def __init__(self,columns:dict,data:list[dict]):
        self.columns=[E for E in columns]
        self.coldata=[columns[E] for E in self.columns]
        self.guide={e:i for i,e in enumerate(self.columns)}
        self.data=[]
        for entry in data:
            entrylist=[]
            for key in self.columns:
                value=entry.get(key,None)
                entrylist.append(value)
            self.data.append(entrylist)
        return
    def select(self,colnames:list[str],):
def main():
    return


if __name__ == "__main__":
    main()
