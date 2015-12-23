import sys
import os
from random import randint, choice

# set directory with files you want to randomise
dir = "G:\\"
# get list of files in the specified directory
files = os.listdir(dir)
print(files)
# get number of files in directory
long = len(files)
# make list of random integer numbers in range 0 to number of files in directory
random_file = list(range(0, long))
# loop through the list of files and append random number before the file name and rename file
for i in range(len(files)):

    if files[i] != 'System Volume Information':
        choose = choice(random_file)
        os.rename(os.path.join(dir, files[i]), os.path.join(dir, str(choose) + '.' + files[i]))
        random_file.remove(choose)


files = os.listdir(dir)
print(files)





