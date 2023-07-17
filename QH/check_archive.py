import os
import re

def is_compressed_file(filename, target_folder):
  with open(filename, 'rb') as f:
    header = f.read(4)
  if header.startswith(b'PK') :
    os.rename(filename, os.path.join(target_folder, os.path.basename(filename+".zip")))
  elif header.startswith(b'ustar'):
    os.rename(filename, os.path.join(target_folder, os.path.basename(filename+".tar")))
  elif header.startswith(b'Rar!\x1A\x07\x00'):
    os.rename(filename, os.path.join(target_folder, os.path.basename(filename+".rar")))


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

print("Done...")
