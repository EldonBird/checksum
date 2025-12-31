import os;
import hashlib

def bfs_checksum(directory):
    file_list = []

    for root, dirs, files in os.walk(directory):
        for name in files:
            relative_path = os.path.relpath(os.path.join(root, name), directory)
            file_list.append(relative_path.replace('\\', '/'))

    file_list.sort()

    combined_names = "|".join(file_list)
    return hashlib.sha256(combined_names.encode('utf-8')).hexdigest()


if __name__ == "__main__":
    my_checksum = bfs_checksum(".")
    print(f"Directory Fingerprint: {my_checksum}")
