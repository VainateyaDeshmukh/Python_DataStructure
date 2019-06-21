
# r opens file for eading only
# r+ opens file for reading and wiritng
# w opens file for writing only. over writes the existing file
# w+ same as r+
# a opens file for appending. starts with original data and adds new data at end
# a+ opens file for appending and allows you to read files

import os
os.chdir('D:\\college work\\Python')
#os.getcwd()

file1 = open('Demopy.txt')
a1 = file1.read()
file1.seek(0,0) #keeps cursor at the beginning
b = file1.read(17)
file1.close()

file1 = open('Demopy.txt', "a")
file1.write("\nNow the file has one more line!")

file1 = open('Demopy.txt', "w")
file1.write("Woops! I have deleted the content!")

file1 = open('Demopy.txt', "w")
file1.write("Python is a high level language.\nIt is open source.\nPortable language.\nUsed in many applications.")

file1 = open('Demopy.txt', "w")
file1.write("")

file1 = open('Demopy.txt')
a3 = file1.read().splitlines()

file2 = open("Demofile.txt", "w+")
file2.write("This is a new file.")
file2.seek(0,0)
#file2 = open("Demofile.txt")
a2 = file2.read()
file2.close()

file2 = open("Demofile.txt", "a")
file2.write("This is a new file.")