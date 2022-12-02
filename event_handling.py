if True:
    import os
    import pickle


    class EventDataRegistry:
        def __init__(self):
            self.events = dict()

        def easy_set(self, lbl, followup, ephemeral=False, name=None):
            name = lbl if name is None else name
            X = {'name': name,
                 'followup': followup,
                 'ephemeral': ephemeral
                 }
            self.events['label'] = X
            return

        def get(self, lbl):
            return self.events.get(lbl, None)


    class LocalSaves:
        def __init__(self, dirpath, extension='.dat'):
            self.dirpath = dirpath
            self.data = dict()
            self.updated = set()
            self.extension = extension

        def get(self, filename, key, default=None, def2=None, doubleDefault=False):
            if not doubleDefault:
                def2 = default
            if filename not in self.data:
                return default
            base = self.data[filename]
            ret = base.get(key, def2)
            return ret

        def load(self):
            files = os.listdir(self.dirpath)
            for f in files:
                if not os.path.isfile(self.dirpath + '/' + f):
                    continue
                if not f.endswith(self.extension):
                    continue
                F = open(self.dirpath + '/' + f, 'rb')
                X = pickle.load(F)
                name = X['__name__']
                self.data[name] = X
                F.close()
            return

        def delete_all_files(self):
            files = os.listdir(self.dirpath)
            for f in files:
                if not os.path.isfile(self.dirpath + '/' + f):
                    continue
                if not f.endswith(self.extension):
                    continue
                os.remove(self.dirpath + '/' + f)
            return

        def save(self, filename):
            if filename not in self.data:
                return False
            current = self.data[filename]
            filepath = self.dirpath + '/' + filename + self.extension
            print(filepath)
            F = open(filepath, 'w')
            F.close()
            F = open(filepath, 'wb+')
            pickle.dump(current, F)
            F.close()
            return True

        def save_more(self, save_all=False):
            cur = set(self.data.keys()) if save_all else self.updated
            for filename in cur:
                self.save(filename)
            self.updated = set()
            return

        def set(self, filename, key, value, overwrite=True, autosave=False):
            if not overwrite:
                if key in self.data:
                    return False
            if filename not in self.data.keys():
                current = {'__name__': filename}
                self.data[filename] = current
            else:
                current = self.data[filename]
            current[key] = value
            self.updated.add(filename)
            if autosave:
                if self.save(filename):
                    self.updated.remove(filename)
            return True


    EDR_MC = EventDataRegistry()

class test:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        return
    def load(self,local:LocalSaves,filename):
        self.a=local.get(filename,'a')
        self.b=local.get(filename,'b')
        self.c=local.get(filename,'c')
        return


def main():
    return


if __name__ == "__main__":
    main()
