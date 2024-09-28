import os.path
from pathlib import Path


class iFileSyncMethod:
    """
    wasd
    """

    def read(self, content: str, old_base: str):
        """

        :param content:
        :param old_base:
        """
        raise NotImplementedError

    def write(self, base: str, old_content: str):
        """

        :param base:
        :param old_content:
        """
        raise NotImplementedError

    def convert_filename(self, filename:str) -> str:
        raise NotImplementedError


class WrapFileSyncMethod(iFileSyncMethod):
    """
    A file synchronisation method that extracts or updates
    the center of a file and replaces certain pre-determined pieces of syntax.
    """

    def __init__(self, startMark: str, endMark: str,
                 replacePairs: list[tuple] = None,
                 typeSwaps: list[tuple] = None,
                 includeStart: bool = False,
                 includeEnd: bool = False):
        self.startMark = startMark
        self.endMark = endMark
        self.repl = replacePairs if replacePairs else []
        self.tswap = typeSwaps if typeSwaps else []
        self.includeStart = includeStart
        self.includeEnd = includeEnd

    def get_base_range(self, content):
        """
        Retrieve the range of the content to be extracted or updated.
        :param content:
        :return:
        """
        ia = content.find(self.startMark)
        if not self.includeStart:
            ia += len(self.startMark)
        ib = content.rfind(self.endMark)
        if self.includeEnd:
            ib += len(self.endMark)
        ia = 0 if ia == -1 else ia
        ib = len(content) if ib == -1 else ib
        return ia, ib

    def read(self, content: str, old_base: str):
        ia, ib = self.get_base_range(content)
        res = content[ia:ib]
        for b_repl, c_repl in self.repl:
            temp = res.replace(c_repl, b_repl)
            res = temp
        return res

    def write(self, base: str, old_content: str):
        ia, ib = self.get_base_range(old_content)
        for b_repl, c_repl in self.repl:
            temp = base.replace(b_repl, c_repl)
            base = temp
        res = old_content[:ia] + base + old_content[ib:]
        return res


PyRenSyncMethod = WrapFileSyncMethod(
    '\nif True:',
    '\ndef',
    [
        ('\ninit ', '\nif True:  # ')
    ],
    includeStart=True
)

RenPySyncMethod = WrapFileSyncMethod(
    "",
    "\n\n"
)


class FileSyncInstance:
    def __init__(self, path, syncMethod: iFileSyncMethod,
                 oldBase: str = ""):
        self.path = path
        self.syncMethod = syncMethod
        self.oldBase = oldBase

    def exists(self):
        if not os.path.exists(self.path):
            return False
        if not os.path.isfile(self.path):
            return False
        return True

    def read(self):
        F = open(self.path, 'r')
        raw = F.read()
        F.close()
        res = self.syncMethod.read(raw, self.oldBase)
        self.oldBase = res
        return res

    def write(self, new_base=None):
        if new_base is None:
            new_base = self.oldBase
        self.oldBase = new_base
        old_content = ""
        if self.exists():
            F = open(self.path, 'r')
            old_content = F.read()
            F.close()
        raw = self.syncMethod.write(new_base, old_content)
        F = open(self.path, 'w')
        F.write(raw)
        F.close()
        return


class FileSyncLocation:
    def __init__(self, basedir: str, defaultSyncMethod):
        self.basedir = basedir
        self.files: dict = {}
        self.defSync = defaultSyncMethod

    def get_IDs(self):
        return set(self.files)

    def search(self, dir, suffix="", keyprefix="", syncMethod=None):
        syncMethod: iFileSyncMethod
        syncMethod = syncMethod if syncMethod else self.defSync
        existing = dict()
        for e, v in self.files.items():
            e: str
            v: FileSyncInstance
            existing[v.path] = e
        directory = Path(dir)
        res = list(directory.rglob('*'+suffix))
        for path in res:
            path = str(path)
            if path in existing:
                continue
            if not path.endswith(suffix):
                continue
            basename = keyprefix + str(os.path.basename(path))
            name = basename
            ind = 0
            while name in existing:
                ind += 1
                name = basename + str(ind)
            fins = FileSyncInstance(path, syncMethod)
            existing[path] = name
            self.files[name] = fins
        return

    def check_ID_last_change(self, ID):
        if ID not in self.files:
            return None
        fsi: FileSyncInstance = self.files[ID]
        path = fsi.path
        if not os.path.exists(path):
            return None
        if not os.path.isfile(path):
            return None
        return os.path.getmtime(path)

    def read_file(self, ID):
        if self.check_ID_last_change(ID) is None:
            return None
        fsi: FileSyncInstance = self.files[ID]
        return fsi.read()

    def write_file(self, ID, new_data):
        if ID not in self.files:
            return False
        fsi: FileSyncInstance = self.files[ID]
        path = fsi.path
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        fsi.write(new_data)
        return True


class FileSynchroniser:
    def __init__(self, locations: list[FileSyncLocation]):
        self.locations = locations

    def sync(self, preserveMissing=True):
        all_IDs = set()
        for loc in self.locations:
            IDs = loc.get_IDs()
            all_IDs |= IDs
        for ID in all_IDs:
            latest = None
            lind = -1
            for i, loc in enumerate(self.locations):
                time = loc.check_ID_last_change(ID)
                if time is None:
                    return
                if latest is None or latest < time:
                    latest = time
                    lind = i
            if lind == -1:
                continue
            filebase = self.locations[lind].read_file(ID)
            for i, loc in enumerate(self.locations):
                if i == lind:
                    continue
                loc.write_file(ID, filebase)
        return


def testInstances(reverse=False):
    P = FileSyncInstance("PyDir/test.py", PyRenSyncMethod)
    R = FileSyncInstance("RenDir/test.rpy", RenPySyncMethod)
    if reverse:
        R, P = P, R
    text = R.read()
    P.write(text)
    return


def testLocations():
    P = FileSyncLocation("C:/Projects/py_miniprojects/Miniprojects/file_sync/PyDir", PyRenSyncMethod)
    R = FileSyncLocation("C:/Projects/py_miniprojects/Miniprojects/file_sync/RenDir", RenPySyncMethod)
    R.search(R.basedir,".rpy","test_")
    print(R.files.keys())


def main():
    testLocations()
    return


if __name__ == "__main__":
    main()
