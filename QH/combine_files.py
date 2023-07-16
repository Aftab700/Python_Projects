import os
import re

def remove_duplicates(filename):
  lines_set = set()
  with open(filename, 'r') as f:
    for line in f:
      line = line.strip()
      if line and line not in lines_set:
        lines_set.add(line)
  with open(filename, 'w') as f:
    for line in lines_set:
      f.write(line + '\n')

def main():
  if not os.path.exists('all.txt'):
    with open('all.txt', 'w') as f:
      pass
  for filename in ['1.txt', '2.txt', '3.txt']:
    with open(filename, 'r') as f:
      for line in f:
        line = line.strip()
        with open('all.txt', 'a') as a:
          a.write(line + '\n')
  remove_duplicates('all.txt')

if __name__ == '__main__':
  main()

print("Done...")
