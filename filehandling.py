import os
# os.chdir('C:\\Users\\Shubham\\PycharmProjects')
# file1 = open('file1.txt')   #default mode is r
# # a= file1.read()
# # file1.seek(0,0) # to put the cursor at begining
# b =file1.read(12) #ten char
# file1.close()

#check file and read lines
# file1= open('file1.txt')
# a1=file1.readline() #read one line at a time
# a2=file1.readlines() #all lines
# file1.seek(0,0)
# a3=file1.read().splitlines() #without \n
# print(a1)
# print(a2)
# print()(a3)
# file1.close

# #write files
file2=open('file1.txt','w+')
file2.write('This is the first line')
file2.seek(0,0)
a=file2.read()
file2.close()
print(a)

# file3 = open('file3.txt','a')
# file3.write('\nThis text is appended')
# file3.close()


# fname='file4.txt'
#
# if os.path.isfile(fname):
#     f = open(fname,'r')
#     a=f.readlines()
#     print(a[2])
#     f.close()
# else:
#     print("File dose not exist")