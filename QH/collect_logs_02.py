import os
import time
import winreg
import shutil
from distutils.dir_util import copy_tree


def copy_folder(src_path, dst_path):
    src_path = src_path.replace('\\', '/')
    dst_path = dst_path.replace('\\', '/')
    copy_tree(src_path, dst_path + src_path.replace('/', '_').replace(':', '').replace(' ', '_'))


def copy_file(src_path, dst_path):
    src_path = src_path.replace('\\', '/')
    dst_path = dst_path.replace('\\', '/')
    shutil.copy2(src_path, dst_path, follow_symlinks=True)


def get_av_path():
    path = winreg.HKEY_LOCAL_MACHINE
    reg_key = winreg.OpenKeyEx(path, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\scanner.exe")
    value_of_reg_key = winreg.QueryValueEx(reg_key, "path")
    if reg_key:
        winreg.CloseKey(reg_key)
    return value_of_reg_key[0]


def create_info_qhc_file(command):
    print(command)
    print("\nGathering system information pleas wait...")
    os.system(command)
    pass



if __name__ == '__main__':
    # copy_file("D:/Programms/html/1.py", 'D:/Programms/html2/')
    av_path_base = get_av_path()   # C:\Program Files\Quick Heal\Quick Heal Total Security\
    # av_path_base = "C:\Program Files\Quick Heal\Quick Heal Total Security\\"
    # filename = "D://Programms\\html2///comment5.txt"
    # os.makedirs(os.path.dirname(filename), exist_ok=True)
    # with open(filename, 'w') as f:
    #     f.write("yo")
    # for key in os.environ:
    #     print(key, '=>', os.environ[key])
    windir = os.environ["WINDIR"]            # C:\WINDOWS
    USERPROFILE = os.environ["USERPROFILE"]  # C:\Users\AFTAB SAMA
    SYSTEMDRIVE = os.environ["SYSTEMDRIVE"]  # C:
    # isFile = os.path.isfile("fpath")
    machine_info_exe = ('"' + av_path_base + 'MACHINFO.EXE" sysinfo@quickheal.com1 sysinfo@quickheal.com1 sysinfo@quickheal.com1').replace('\\', '/')
    create_info_qhc_file(machine_info_exe)
    print("Choose option from following:")
    print("1 => False issue")
    print("2 => Malware issue")
    print("q => exit")
    # print(USERPROFILE + "//home" + "file.txt")  #
    list_of_files_to_copy = list()
    list_of_files_to_copy.append(SYSTEMDRIVE + "/Info.qhc")
    while True:
        user_input = input("Enter Input: ")
        list_of_files_to_copy.append(av_path_base + "/Quarantine")
        list_of_files_to_copy.append(av_path_base + "/LOGS")
        list_of_files_to_copy.append(av_path_base + "/REPORT")
        list_of_files_to_copy.append(av_path_base + "/Arwbackup")       # Not found
        if user_input == '1':
            break
        elif user_input == '2':
            list_of_files_to_copy.append(windir + "/Tasks")
            list_of_files_to_copy.append(windir + "/System32/Tasks")
            list_of_files_to_copy.append(windir + "/Prefetch")
            list_of_files_to_copy.append(windir + "/System32/winevt")
            list_of_files_to_copy.append(windir + "/Connection_Log.csv")  # Not found
            list_of_files_to_copy.append(windir + "/regact.dat")
            break
        elif user_input == 'q':
            exit(0)
        else:
            print("Invalid input.Please try again...")
    # [print(i) for i in list_of_files_to_copy]
    folder_name = str(time.time_ns()) + "/"
    # folder_name = "1682765157686604700/"
    folder_path = USERPROFILE + '/' + folder_name
    folder_path = folder_path.replace('\\', '/')
    os.makedirs(os.path.dirname(folder_path + "/yo.txt"), exist_ok=True)
    print(folder_path)

    print("\nGive path to Upload Sample.\nExample: C:/Users/John/Downloads/cat.exe")
    while True:
        print("Enter 'q' to skip")
        mal_sample_path = input("Enter path: ").replace('\\', '/')
        if mal_sample_path == 'q':
            break
        if os.path.isfile(mal_sample_path) or os.path.isdir(mal_sample_path):
            list_of_files_to_copy.append(mal_sample_path)
        else:
            print("Invalid path\ntry again or Enter 'q' to skip")
    comment_s = ""
    print("\n\nStart entering your comment below and press 'q' to stop")
    while True:
        x = input("=>")
        if x == 'q':
            break
        comment_s += x + "\n"
    with open(folder_path + "comment_of_user.txt", 'w') as f:
        f.write(comment_s)
    for i in list_of_files_to_copy:
        try:
            if os.path.isfile(i):
                copy_file(i, folder_path)
            else:
                if "System32" in i:
                    copy_folder(i, folder_path + "/System32")
                else:
                    copy_folder(i, folder_path)
        except Exception as e:
            print(e)
    zip_dst = SYSTEMDRIVE + "/" + folder_name
    archived = shutil.make_archive(f"{zip_dst}/data", 'zip', f"{folder_path}")
    if os.path.exists(zip_dst):
        print(archived)
        shutil.rmtree(folder_path)
    else:
        print("ZIP file not created")
        print(folder_path)
    pass
    # make password protected zip
    # try:
    #     pyminizip.compress(inpt, None, oupt, password, com_lvl)
    # except Exception as e:
    #     print(e)
print('======================================\nDone')
