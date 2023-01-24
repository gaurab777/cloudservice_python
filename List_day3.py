#LIST
A = [1,12.5,'a',"Python","Programming"]

print(A[1])
print(A[3])
print(A[1:4])

L = [9,18,"Hi",12,"Hello",15.55,"Programming",100,125.5]

print(L[5])
print(L[1:5])
print(L[2:8])
print(L[2:9:3])
print(L[-1])
print(L[-4])

print(L[0:9:2])
print(L[::2])
print(L[2])
print("-----------------------------------------------")


#Updating the list
Z=[30,17,29,2]

Z[1] = "Py"
print(Z)

Z.append(40) #Adding new item into the list
print(Z)

Z[2]="Program"
print(Z)
print("-----------------------------------------------")


#Deleting List Elements
B = ["Python",100,"Programming",2,"this"]
print(B)
del B[1]#Deleting using indexing
print(B)
B.remove("this")#removing the specific element from the list
print(B)
B.append("this")
print(B)


#Basic List Operations
C = [10,20,30,40,50,76]
print(len(C))
print(B+C)
print(C*3)
print(23 in C)
print(40 in C)
print(60 not in C)


#Built-in List Functions and Methods

#cmp(list1,list) Please note cmp() does not support in python3.

#len(list):Give the total length of the list.
#max(list): Returns item from the list with max value.
#min(list): Returns item from the list with min value

print(len(C))
print(max(C))
print(min(C))
print("------------------------------------------------")


#List Methods
D=[10,15,20,"Hello","Python",10]

D.append("Programming")
print(D)
print(D.count(10))

E=[100,500]
D.extend(E)
print(D)

print(D.index("Hello"))
D.insert(2,"Good")
print(D)
print(D.pop())
print(D.pop(3))
print(D)

D.remove("Hello")
print(D)
D.reverse()
print(D)
D.insert(5,"Chairs")
print(D)
print("-----------------------------------------------------------------")


E=[1,2,3,4]
print(E)

E.append(5)
print(E)

E.extend([6,7,8,9]) #Adding multiple items in the list.
print(E)
print("-----------------------------------------------------------------")


#TUPLES
F = (1,12.5,'a','Python','Programming')
print(F[1])
print(F[3])
print(F[1:4])
print("-----------------------------------------------------------------")

T = (9,18,"Hi",18,"Hello",15.55,"Programming",100,125.2)
print(T[5])
print(T[1:5])
print(T[2:8])
print(T[2:9:3])
print(T[-1])
print(T[])



