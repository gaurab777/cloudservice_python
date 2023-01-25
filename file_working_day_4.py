file = open('hello.txt','r')
#This will print every line one by one in the file
for x in file:
    print(x)

print(file.name)
print(file.mode)
print(file.closed)
print("----------------------------------------------")


#if you forget to specify the file mode, by default it will be in read mode
file1 = open('Hello.txt')
for each in file1:
    print(each)
file1.close()
print(file1.mode)
print(file.closed)
print("----------------------------------------------")


print("\n#read() mode character wise")
file2 = open("good.txt","r")
print(file2.read(40)) #Read mode character wise
print(file2.read(4))
print("----------------------------------------------")


#Creating a file using write() mode
file3 = open('g.txt','w')
file3.write("My name ")
file3.write("is Gaurab Bam ")
file3.write("This is write method.")
file3.close()
print("----------------------------------------------")

#Working with append
print("Working with append()")
file4 = open('g1.txt','a')
file4.write(" This will append text in the file.")
file4.close()


#FILE POSITION

fileopen = open('g.txt','r+')
str = fileopen.read(21)
print("Read string is: ",str)

#Check current position
position = fileopen.tell()
print("Current file position: ",position)

#Repositioning the pointer at the beginning
position = fileopen.seek(0,0)
str=fileopen.read(10);
print("Again read string is: ",str)
fileopen.close()#close the file

#Renaming file
import os #importing os is important
os.rename("g.txt","G.txt")

#Deleting the file
import os
os.remove("test.txt")

