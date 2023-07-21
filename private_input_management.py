import json
import os

private_inputs = dict()


def get_private_inputs(file_path="asset_inputs.private.txt", dest=None):
    if not os.path.exists(file_path):
        raise FileNotFoundError
    if dest is None:
        dest = private_inputs
    file = open(file_path, 'r')
    buf = json.load(file)
    file.close()
    dest.update(buf)
    return


def main():
    return


if __name__ == "__main__":
    main()
