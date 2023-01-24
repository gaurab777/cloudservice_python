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
print(T[-5])
print(T[0:9:3])
print(T[::3])
print(T[2::2])
print(T[2::3])
print(T[3::3])
print(T[5:-2])
print(T[-2:-5:-1])
print(T[-2:-7:-2])


tup1 = (10,4.6)
tup2 = ('Hi','Python')

#tup[0] = 100 following action is not allowed in tuples

tup3 = tup1 + tup2
print(tup3)

tup =("Math", "Science", "English", "Nepali")

#Removing individual tuple elements is not possible.
#but can delete entire tuple

del tup
print("After deleting tup:")#tup)

print("-------------------------------------------------------")
G = (10.5,11.5)
H = (12.5,13,14,16,20)
print(len(H))
print(G+H)
print(G*3)
print(3 in H)
print(12 not in H)
print("-------------------------------------------------------")

print(max(H))
print(min(H))
print("-------------------------------------------------------")


#Tuple Methods
#-count()
#-index()
I=(20,15,10,'Hello','Python',10,1,10)

print(I.count(10))
print(I.index(10))
print("-------------------------------------------------------")


#DICTIONARY
J={'Name':'James','Age':35,'Degree':'Master'}
print(J)
print(J['Name'])
print(J['Age'])
print(J['Degree'])
print("-------------------------------------------------------")

#Updating Dictionary
J['Age'] = 30 #Updating existing entry
J['College'] = "Islington" #Adding new entry
print(J)
print("-------------------------------------------------------")
print("-------------------------------------------------------")


#Delete Dictionary Elements
del J['Name'] # remove entry with key 'Name'
print(J)
del J['Age']
print(J)
J.clear() #remove all entries in dictionary
print(J)
del J #delete entire dictionary
#print(J)
print("-------------------------------------------------------")

K = {1:20,2:30,3:40}
print(K)
print(len(K))
M=str(K)
print(M)
print(type(M))
print("-------------------------------------------------------")
print("-------------------------------------------------------")


#Dictionary Methods
#dict.clear()-->removes all the elements of dictionary
#dict.copy()
d1={'Roll_no':45,'class':6, 'Percentage':85.5}
d2=d1.copy()
print(d2)

#Using fromkeys() methods
seq=('name','age','sex')
dict = dict.fromkeys(seq)
print(dict)
dict=dict.fromkeys(seq, 10)
print(dict)

print(d1.get('class')) #Use of get method
print(d1['class'])
print(d1.items())

print(d1.keys())
print(d1.values())
print(d1.setdefault('class',None))
print(d1)
print("-------------------------------------------------------")

d3={'Name':'Dennis','Age':50}
d4={'Roll':'Scientist','City':'Mumbai'}
d4.update(d3)
print(d3)
print(d4)




