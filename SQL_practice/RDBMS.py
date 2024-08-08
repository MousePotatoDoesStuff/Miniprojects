class RDBMS:
    """
    A simple enough yet (hopefully) computationally efficient
    (R)elational (D)ata(B)ase (M)anagement (S)ystem
    """

    def __init__(self, columns: dict, data: list[dict]):
        self.columns = [E for E in columns]  # Column names
        self.coldata = [columns[E] for E in self.columns]  # TODO columbn data
        self.guide = {e: i for i, e in enumerate(self.columns)}  # Name-to-index pipeline
        self.data: list = []
        for entry in data:
            entrylist = []
            for key in self.columns:
                value = entry.get(key, None)
                entrylist.append(value)
            self.data.append(entrylist)
        self.emptycount = 0
        return

    def get_indices(self, colnames: list[str]):
        indices = []
        for name in colnames:
            index = self.guide.get(name, None)
            indices.append(index)
        return

    def wrap_condition(self, dict_condition):
        def list_condition(L):
            D={key:L[i] for i,key in enumerate(self.columns)}
            val=dict_condition(D)
            return val
        return list_condition

    def insert_list(self, entry: list):
        n = len(self.columns)
        entry = entry[:n]
        m = len(entry)
        entry += [None] * (n - m)
        self.data.append(entry)

    def insert_dict(self, entry: dict):
        entry_list = []
        for key in self.columns:
            value = entry.get(key, None)
            entry_list.append(value)
        self.data.append(entry_list)

    def delete_naive(self, crit: callable):
        cur = 0
        for i, E in enumerate(self.data):
            if crit(E):
                continue
            self.data[cur] = E
            cur += 1
        n = len(self.data)
        for i in range(cur, n):
            self.data.pop()
        return

    def delete(self, crit: callable):
        for i, E in enumerate(self.data):
            if E is None:
                continue
            if not crit(E):
                continue
            self.data[i] = None
            self.emptycount += 1
        while self.data and self.data[-1] is None:
            self.data.pop()
            self.emptycount += 1
        if self.emptycount * 2 >= len(self.data):
            self.delete_naive(lambda E: E is None)

    def select_rows(self, colnames: list[str], ):
        col_indices = self.get_indices(colnames)
        # TODO


def main():
    return


if __name__ == "__main__":
    main()
