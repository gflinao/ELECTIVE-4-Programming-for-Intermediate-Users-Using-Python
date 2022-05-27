f = open("python.txt", "r")
print(f.readline())

for x in f:
    print(x)

import os
if os.path.exists("python.txt"):
    os.remove("python.txt")
else:
    print("The file does not exist.")