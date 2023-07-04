import os
import hashlib


# Created with assistance from ChatGPT

class AssetFile:
    def __init__(self, size: int, modified: float):
        self.size = size
        self.modified = modified

    def size_diff(self, other):
        if not isinstance(other, AssetFile):
            raise TypeError("Other object must be an AssetFile")
        return abs(self.size - other.size)

    def modified_diff(self, other):
        if not isinstance(other, AssetFile):
            raise TypeError("Other object must be an AssetFile")
        return abs(self.modified - other.modified)

    def __eq__(self, other):
        if not isinstance(other, AssetFile):
            return False
        return self.size == other.size and self.modified == other.modified

    def __repr__(self):
        return f"AssetFile(size={self.size}, modified={self.modified})"


class AssetFileManager:
    def __init__(self, rootfolder):
        self.rootfolder = rootfolder
        self.files = {}

    def add_file(self, file_path, size, modified):
        self.files[file_path] = AssetFile(size, modified)

    def import_submanager_data(self, submanager):
        if not isinstance(submanager, AssetFileManager):
            return -1

        if not submanager.rootfolder.startswith(self.rootfolder):
            return -2

        relative_path = os.path.relpath(submanager.rootfolder, self.rootfolder)

        for file_path, asset_file in submanager.files.items():
            new_file_path = os.path.join(self.rootfolder, relative_path, file_path)
            self.files[new_file_path] = asset_file

        return 0

    def generate_from_directory_data(self, local_file_managers=None):
        # Create a set of excluded directories
        local_dict = dict()
        if local_file_managers is not None:
            for lfm in local_file_managers:
                lfm: AssetFileManager
                local_dict[lfm.rootfolder] = lfm

    def compare_to(self, other_file_manager):
        results = []
        for file_path, asset_file in self.files.items():
            if file_path not in other_file_manager.files:
                results.append((file_path, asset_file, None))
            else:
                other_asset_file = other_file_manager.files[file_path]
                if asset_file != other_asset_file:
                    results.append((file_path, asset_file, other_asset_file))
        return results


def main():
    X = AssetFileManager("C:\\Projects\\py_miniprojects\\Miniprojects")
    X.generate_from_directory_data()
    for e in X.files:
        print(X)
    return


if __name__ == "__main__":
    main()
