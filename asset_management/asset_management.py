import json
import os
import hashlib
from datetime import datetime

import Miniprojects.private_input_management as PrivateInput

# Created with assistance from ChatGPT

private_inputs = dict()


class AssetFile:
    def __init__(self, size: int, modified: float, tags=None):
        if tags is None:
            tags = dict()
        tags: dict
        self.size = size
        self.modified = modified
        self.tags: dict = tags

    def read_physical_file(self, path):
        try:
            # Check if the file exists at the given path
            if not os.path.isfile(path):
                print(f"Error: File not found at {path}")
                return

            # Get the file's size in bytes
            self.size = os.path.getsize(path)

            # Get the file's last modified timestamp
            modified_timestamp = os.path.getmtime(path)
            self.modified = datetime.fromtimestamp(modified_timestamp)

        except OSError as e:
            print(f"Error: Failed to read physical file: {e}")
            # You can handle the exception as per your requirement

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

    def generate_from_directory_data(self, local_file_managers=None, reset=False):
        # Create a set of excluded directories
        if reset:
            self.files=dict()
        local_dict = dict()
        if local_file_managers is not None:
            for lfm in local_file_managers:
                lfm: AssetFileManager
                local_dict[lfm.rootfolder] = lfm

        stack = [self.rootfolder]

        while stack:
            current_folder = stack.pop()

            if current_folder in local_dict:
                continue

            for filename in os.listdir(current_folder):
                file_path = os.path.join(current_folder, filename)
                if os.path.isfile(file_path):
                    file=AssetFile(0,0)
                    file.read_physical_file(file_path)
                    self.files[file_path]=file
                elif os.path.isdir(file_path):
                    stack.append(file_path)

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
    def get_files_in_directory(self, dir_path):
        """
        Given a directory path, returns the files recorded by the AssetFileManager
        that are present in the specified directory.
        :param dir_path: The directory path to search for files.
        :return: A list of files recorded in the given directory.
        """
        files_in_directory = []
        for file_path in self.files.keys():
            if os.path.dirname(file_path) == dir_path:
                files_in_directory.append(file_path)
        return files_in_directory


def main():
    private_inputs['testdir'] = "C:\\Projects\\py_miniprojects\\Miniprojects"
    PrivateInput.get_private_inputs(private_inputs)
    testdir = private_inputs["testdir"]
    print(testdir)
    X = AssetFileManager(testdir)
    X.generate_from_directory_data()
    print("\n".join(X.get_files_in_directory(testdir)) )
    return


if __name__ == "__main__":
    main()
