import codecs
import os

class FileBrowser:
    def __init__(self,root):
        self.root=root
        return
    def iterate_filepaths(self,pathfilter):
        for root, dirs, files in os.walk(self.root):
            for file in files:
                file_path = os.path.join(root, file)
                if pathfilter(file_path):
                    yield file_path
    def iterate_files(self,pathfilter,filefilter):
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
    root=input("->")
    X=FileBrowser(root)
    text=input("->")
    for e in X.iterate_files(create_endswith_checker('.rpy'),lambda X:text in X):
        print(e)
    return


if __name__ == "__main__":
    main()