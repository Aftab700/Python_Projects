import os
import re

def create_all_txt(dir_path):
    if not os.path.exists(f'{dir_path}/all.txt'):
        with open(f'{dir_path}/all.txt', 'w') as f:
            pass
        pass
    lines_set = set()
    for filename in [f'{dir_path}/FileHash-MD5.txt', f'{dir_path}/FileHash-SHA1.txt', f'{dir_path}/FileHash-SHA256.txt']:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line != '':
                    lines_set.add(line)
    with open(f'{dir_path}/all.txt', 'w') as a:
        for line in lines_set:
            a.write(line + '\n')
    pass

def main():
    dir_list = []
    for dir_path in os.listdir("."):
        if os.path.isdir(dir_path):
            print(dir_path)
            dir_list.append(dir_path)
            try:
                create_all_txt(dir_path)
            except Exception as e:
                print(e)
                pass
    if not os.path.exists('all.txt'):
        with open('all.txt', 'w') as f:
            pass
        pass
    lines_set = set()
    for path_dir in dir_list:
        with open(f'{path_dir}/all.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line != '':
                    lines_set.add(line)
    with open(f'all.txt', 'w') as a:
        for line in lines_set:
            a.write(line + '\n')
        pass

if __name__ == '__main__':
    main()
    # it will create all.txt of combine hashes in all subdirectories
    # create all.txt of all subdirectories

print("Done...")
