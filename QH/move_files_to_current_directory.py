import os
import shutil

def move_files_to_current_directory():
    for root, dirs, files in os.walk('.'):
        for file in files:
            src = os.path.join(root, file)
            dst = os.path.join('.', file)
            if os.path.exists(dst):
                base, ext = os.path.splitext(file)
                i = 1
                while os.path.exists(dst):
                    dst = os.path.join('.', f'{base}_{i}{ext}')
                    i += 1
            shutil.move(src, dst)
            print(src)


if __name__ == '__main__':
    move_files_to_current_directory()
    print("\nDone...\n")
