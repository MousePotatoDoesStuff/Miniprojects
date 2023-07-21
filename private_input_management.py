import json
import os


def get_private_inputs(dest, file_path="asset_inputs.private.txt"):
    if not os.path.exists(file_path):
        raise FileNotFoundError
    file = open(file_path, 'r')
    buf = json.load(file)
    file.close()
    dest.update(buf)
    return


def main():
    return


if __name__ == "__main__":
    main()
