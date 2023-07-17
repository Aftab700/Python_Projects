import os
import re
import zipfile

def is_compressed_file(filename, target_folder):
  with open(filename, 'rb') as f:
    header = f.read(4)
  if header.startswith(b'PK') :
    print(filename)
    is_apk = False
    with zipfile.ZipFile(filename, 'r') as zf:
      if 'AndroidManifest.xml' in zf.namelist() and 'classes.dex' in zf.namelist():
        is_apk = True
    if is_apk:
      if not os.path.exists("apk"):
        os.mkdir(target_folder)
      os.rename(filename, os.path.join("./apk", os.path.basename(filename)))
    else:
      os.rename(filename, os.path.join(target_folder, os.path.basename(filename+"_zip")))
  elif header.startswith(b'ustar'):
    print(filename)
    os.rename(filename, os.path.join(target_folder, os.path.basename(filename+"_tar")))
  elif header.startswith(b'Rar!\x1A\x07\x00'):
    print(filename)
    os.rename(filename, os.path.join(target_folder, os.path.basename(filename+"_rar")))


def main():
  # move the compressed files from 'sample' to 'archive' 
  target_folder = 'archive'
  if not os.path.exists(target_folder):
    os.mkdir(target_folder)
  for filename in os.listdir('./sample'):
    if filename.endswith('.py') or filename == target_folder:
      continue
    is_compressed_file("./sample/"+filename, target_folder)

if __name__ == '__main__':
  main()

print("\nDone...\n")
