import json
import os.path
import time
from pathlib import Path


def NextName(base, index, used, infix="_"):
    name = base + infix + str(index)
    while name in used:
        index += 1
        name = base + infix + str(index)
    return name


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

    def get_base_filename(self, filename):
        """

        :param filename:
        """
        raise NotImplementedError

    def set_base_filename(self, filename):
        """

        :param filename:
        """
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
                 includeEnd: bool = False,
                 swapExtension: list[tuple] = None):
        self.startMark = startMark
        self.endMark = endMark
        self.repl = replacePairs if replacePairs else []
        self.tswap = typeSwaps if typeSwaps else []
        self.includeStart = includeStart
        self.includeEnd = includeEnd
        self.exswap = swapExtension if swapExtension else []

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

    def get_base_filename(self, filename: str):
        for base_ext, this_ext in self.exswap:
            if filename.endswith(this_ext):
                return filename[:-len(this_ext)] + base_ext
        return filename

    def set_base_filename(self, filename: str):
        for base_ext, this_ext in self.exswap:
            if filename.endswith(base_ext):
                return filename[:-len(base_ext)] + this_ext
        return filename


PyRenSyncMethod = WrapFileSyncMethod(
    '\nif True:',
    '\ndef',
    [
        ('\ninit ', '\nif True:  # ')
    ],
    includeStart=True,
    swapExtension=[('.rpy', '.py')]
)

RenPyInsert = WrapFileSyncMethod(
    "",
    "\n\n"
)

NullMethod = WrapFileSyncMethod(
    "",
    ""
)

METHODS = {
    'PyRenSync': PyRenSyncMethod,
    'RenPyIns': RenPyInsert,
    'Null': NullMethod,
}


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

    def get_base_filename(self):
        return self.syncMethod.get_base_filename(self.path)


class FileSyncLocation:
    def __init__(self, basedir: str, defaultSyncMethod: iFileSyncMethod, defaultFileBase: str = "", **kwargs):
        self.basedir = basedir
        self.files: dict = {}
        self.defSync: iFileSyncMethod = defaultSyncMethod
        self.defaultFileBase = defaultFileBase

    @classmethod
    def from_json(cls, raw: dict):
        methodname = raw.pop('method', '')
        raw['defaultSyncMethod'] = METHODS[methodname]
        return FileSyncLocation(**raw)

    def get_IDs(self):
        return set(self.files)

    def getExisting(self):
        existing = dict()
        for e, v in self.files.items():
            e: str
            v: FileSyncInstance
            existing[v.path] = e
        return existing

    def RegisterPath(self, rawpath, keyprefix, suffix, existing,
                     syncMethod=None):
        syncMethod: iFileSyncMethod
        syncMethod = syncMethod if syncMethod else self.defSync
        path = str(rawpath)
        if path in existing:
            return
        if not path.endswith(suffix):
            return
        basename = keyprefix + str(os.path.basename(path))
        name = NextName(basename, 0, existing, '')
        fins = FileSyncInstance(path, syncMethod)
        existing[path] = name
        self.files[name] = fins
        return

    def search(self, dir, suffix="", keyprefix="", syncMethod=None):
        syncMethod: iFileSyncMethod
        syncMethod = syncMethod if syncMethod else self.defSync
        existing = self.getExisting()
        directory = Path(dir)
        res = list(directory.rglob('*' + suffix))
        for path in res:
            self.RegisterPath(path, keyprefix, suffix, existing, syncMethod)
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
        res=os.path.getmtime(path)
        return res

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
        dirpath = os.path.dirname(os.path.abspath(path))
        if not os.path.exists(dirpath):
            os.makedirs(dirpath, exist_ok=True)
        fsi.write(new_data)
        return True

    def get_base_filepaths(self) -> dict:
        RES = {}
        for ID, FSI in self.files.items():
            FSI: FileSyncInstance
            globalpath = FSI.path
            localpath = os.path.relpath(globalpath, self.basedir)
            basepath = FSI.syncMethod.get_base_filename(localpath)
            RES[ID] = basepath
        return RES

    def set_base_filepaths(self, bases: dict):
        for ID, basepath in bases.items():
            globalpath = os.path.join(self.basedir, basepath)
            truepath = self.defSync.set_base_filename(globalpath)
            FSI = FileSyncInstance(truepath, self.defSync, self.defaultFileBase)
            self.files[ID] = FSI
        return


class FileSyncMain:
    def __init__(self, locations: list[FileSyncLocation]):
        self.locations = locations
        self.last_synced = 0.0

    @classmethod
    def from_json(cls, raw: dict):
        last_sync = raw.get('last_sync', 0.0)
        locs = []
        raw_locations = raw.get('locations', [])
        for rawloc in raw_locations:
            loc=FileSyncLocation.from_json(rawloc)
            locs.append(loc)
        new = FileSyncMain(locs)
        new.last_synced = last_sync
        return new

    def print_sync_diff(self,time):
        if time is None:
            print('N/A')
            return
        print(int(time-self.last_synced))

    def save_data(self, old_json: dict):
        old_json['last_sync'] = self.last_synced

    def collect_IDs(self) -> set[int]:
        all_IDs = set()
        for loc in self.locations:
            IDs = loc.get_IDs()
            all_IDs |= IDs
        return all_IDs

    def delete_one(self, ID):
        for i, loc in enumerate(self.locations):
            file = loc.files.pop(ID, None)
            if not file:
                continue
            file: FileSyncInstance
            if file.exists():
                os.remove(file.path)
        return

    def sync_one(self, ID, preserveMissing=True, check_last_sync=True):
        latest = None
        lind = -1
        fileMissing = False
        times = []
        for i, loc in enumerate(self.locations):
            time = loc.check_ID_last_change(ID)
            times.append(time)
            if time is None:
                fileMissing = True
                continue
            if latest:
                print(time - latest, loc.files[ID].path)
            if latest is None or latest < time:
                latest = time
                lind = i
        print(latest, lind, fileMissing, times)
        if fileMissing and not preserveMissing:
            self.delete_one(ID)
            return
        if lind == -1:
            return
        print(f"Reading from {lind}")
        filebase = self.locations[lind].read_file(ID)
        for i, loc in enumerate(self.locations):
            if i == lind:
                continue
            last_changed=times[i]
            self.print_sync_diff(times[0])
            if last_changed and last_changed > self.last_synced:
                continue
            print(f"Writing to {i}")
            loc.write_file(ID, filebase)

    def sync(self, preserveMissing=True, check_last_sync=True, curtime="now"):
        print(f"Last sync:{int(self.last_synced)}")
        all_IDs: set[int] = self.collect_IDs()
        for ID in all_IDs:
            self.sync_one(ID, preserveMissing, check_last_sync)
        if curtime == "now":
            curtime = float(time.time())
        curtime: float
        self.last_synced = curtime
        return


def testInstances(reverse=False):
    P = FileSyncInstance("PyDir/test.py", PyRenSyncMethod)
    R = FileSyncInstance("RenDir/test.rpy", RenPyInsert)
    if reverse:
        R, P = P, R
    text = R.read()
    P.write(text)
    return


def testLocations():
    P = FileSyncLocation("C:/Projects/py_miniprojects/Miniprojects/file_sync/PyDir", PyRenSyncMethod)
    R = FileSyncLocation("C:/Projects/py_miniprojects/Miniprojects/file_sync/RenDir", RenPyInsert)
    R.search(R.basedir, ".rpy", "test_")
    paths = R.get_base_filepaths()
    for e, V in paths.items():
        print(f"{e}\t\t{str(V)}")
    P.set_base_filepaths(paths)
    SYN = FileSyncMain([P, R])
    SYN.sync()

def testFinal():
    filepath="test.filesync.json"
    F=open(filepath,'r')
    raw=F.read()
    F.close()
    data=json.loads(raw)
    SYN=FileSyncMain.from_json(data)
    data=json.loads(raw)
    P,R=SYN.locations
    R.search(R.basedir, ".rpy", "test_")
    paths = R.get_base_filepaths()
    P.set_base_filepaths(paths)
    SYN.sync()
    SYN.save_data(data)
    raw2=json.dumps(data,indent=2)
    F=open(filepath,'w')
    F.write(raw2)
    F.close()


def main():
    testFinal()
    return


if __name__ == "__main__":
    main()
