import os
import sys

f = open("input.txt", "r")
files = f.readlines()
files = list(filter(None, files))

d = {}

for i in files:
    i = i.strip()
    d[i] = i

results = []

r =  open("root.txt", "r")
walk_dir = r.readline()

for root, subdirs, files in os.walk(walk_dir):
    for filename in files:
        file_path = os.path.join(root, filename)
        results.append(file_path)

absent = []
there = []

for i in results:
    if d.get(i) is None:
        absent.append(i)
    else:
        there.append(i)

print(absent)
print(there)

f.close()
r.close()
