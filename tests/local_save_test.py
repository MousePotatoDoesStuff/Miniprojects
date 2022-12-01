from Miniprojects.event_handling import *

SAVEPATH = 'C:/DDLC/python lab/tests/save'
SVMC = SAVEPATH + '/MC'


def forcedelete(filepath):
    try:
        os.remove(filepath)
    except FileNotFoundError:
        pass
    return


def delete_test():
    X = LocalSaves(SVMC)
    X.delete_all_files()
    X.set('main', 'name', 'Dense Boi')
    X.save_more()
    X.delete_all_files()
    Y = LocalSaves(SVMC)
    Y.load()
    res1 = str(X.data)
    res2 = str(Y.data)
    for e in X.data:
        if e in Y.data:
            return 'Failed, did not delete {}'.format(e)
    return 'Passed'


def test_1():
    X = LocalSaves(SVMC)
    name = 'Dense Boi'
    X.set('main', 'name', name)
    res = X.get('main', 'name')
    if res == name:
        return 'Passed'
    return 'Failed, returned {} instead of {}'.format(res, name)


def test_2():
    X = LocalSaves(SVMC)
    X.delete_all_files()
    X.set('main', 'name', 'Dense Boi')
    X.save_more()
    Y = LocalSaves(SVMC)
    Y.load()
    res1 = str(X.data)
    res2 = str(Y.data)
    if X.data == Y.data:
        return 'Passed'
    return 'Failed, returned \n{}\n instead of \n{}'.format(res1, res2)


def test_3():
    X = LocalSaves(SVMC)
    X.delete_all_files()
    X.set('main', 'name', 'Dense Boi')
    X.set('1', 'crush', 'Cinnamon Bun')
    X.save_more()
    Y = LocalSaves(SVMC)
    Y.load()
    res1 = str(X.data)
    res2 = str(Y.data)
    for e in X.data:
        if e not in Y.data:
            return 'Failed, did not reload {}'.format(e)
    return 'Passed'


def main():
    all_tests = [
        ('Delete test', delete_test),
        ('Set/get test', test_1),
        ('Save/load test', test_2),
        ('Multifile save/load test', test_3)
    ]
    tests = all_tests[0:]
    for (name, fn) in tests:
        print(name)
        res = fn()
        print('-'*80)
        print('{}: {}'.format(name, res))
    return


if __name__ == "__main__":
    main()
