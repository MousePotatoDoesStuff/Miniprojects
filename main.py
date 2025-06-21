# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import traceback
def print_hi(name):
    try:
        raise ValueError(name)
    except ValueError as err:
        tb_str = traceback.format_exc()
        print(tb_str)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
