import codecs
import os
import Miniprojects.private_input_management as PrivateInput


class FileBrowser:
    def __init__(self, root):
        self.root = root
        return

    def iterate_filepaths(self, pathfilter):
        X = os.walk(self.root)
        for root, dirs, files in X:
            for file in files:
                file_path = os.path.join(root, file)
                if pathfilter(file_path):
                    yield file_path

    def iterate_files(self, pathfilter, filefilter):
        for filepath in self.iterate_filepaths(pathfilter):
            with codecs.open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                if filefilter(content):
                    yield filepath


def create_endswith_checker(substring):
    def endswith_checker(string):
        return string.endswith(substring)

    return endswith_checker


def main():
    while True:
        root = input("Directory:")
        if len(root) == 0:
            D = {}
            PrivateInput.get_private_inputs(D)
            root = D["fb_testdir"]
        X = FileBrowser(root)
        text = 'TEXT'
        print("Directory:",root)
        while len(text) > 0:
            text = input("Text:")
            for e in X.iterate_files(create_endswith_checker('.rpy'), lambda X: text in X):
                print("->", e)
            print("Complete.")


if __name__ == "__main__":
    main()
