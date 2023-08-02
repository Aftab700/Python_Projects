import os
import shutil
import hashlib


def move_files_to_current_directory():
    for root, dirs, files in os.walk('.'):
        for file in files:
            src = os.path.join(root, file)
            dst = os.path.join('.', file)
            if src == dst:
                continue
            if os.path.exists(dst):
                base, ext = os.path.splitext(file)
                i = 1
                while os.path.exists(dst):
                    dst = os.path.join('.', f'{base}_{i}{ext}')
                    i += 1
            shutil.move(src, dst)
            if src != dst:
                print(src)


def delete_folders(directory):
    for folder in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, folder)):
            shutil.rmtree(os.path.join(directory, folder))
            print("deleted:", folder)


def rename_to_md5(path):
    for file in os.listdir(path):
        md5 = hashlib.md5(open(os.path.join(path, file), "rb").read()).hexdigest()
        new_name = os.path.join(path, md5)
        shutil.move(os.path.join(path, file), new_name)
        print(md5, ":", file)


if __name__ == '__main__':
    move_files_to_current_directory()
    delete_folders(".")
    rename_to_md5(".")
    print("\nDone...\n")
    

