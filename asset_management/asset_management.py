import os
import hashlib

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
    def __init__(self):
        self.files = {}

    def add_file(self, file_path, size, modified):
        self.files[file_path] = AssetFile(size, modified)

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
    return


if __name__ == "__main__":
    main()
