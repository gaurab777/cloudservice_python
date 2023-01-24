for x in 'Loops':
    print("*")
    print(x)
print("------------------------")

for a in range (3):
    print("Python")
print("------------------------")

for a in range(5,20,3):
    print(a)
print("------------------------")

for y in 'Gaurab':
    print(y)
print("------------------------")

for z in {20,22,12,13,14,15}:
    print(z)
print("------------------------")

#While Loop
c=21
count = 10
while (count<c):
    print("The count is: ",count)
    count = count + 1
print("------------------------")

table= 8
while table < 81:
    print(table)
    table += 8
print("------------------------")

#Multiplication table using while loop
num1= int(input("Enter the number you want the multiplication: "))
count=1
print("The multiplication of ",num1," is")
while count <=10:
    number = num1 * count
    print(num1,"X",count,"=",number)
    count += 1
print("------------------------")

#Multiplication table using for loop
c=1
num2= int(input("Enter the number you want the multiplication: "))
for t in range(num2,num2*11,num2):
    print(num2,"X",c,"=",t)
    c += 1
print("------------------------")


#Nested Loop
for i in range(1,6):
    for j in range (1,i+1):
        print(j, end="")
    print()
print("------------------------")

for i in range(1,5):
    for j in range (1,4):
        print("Hello")
print("------------------------")

#INFINITE LOOP
#cnt=10
#while(cnt>9):
#   cnt+=1
#   print(cnt)


#LOOP CONTROL STATEMENT

#Break Statement

for i in range(11,21):
    if(i==17):
        break
    print(i)
print("------------------------")

for i in range(11,21):
    if(i==17):
        break
    print(i)
print("Thank you")
print("------------------------")

#Continue Statement
for i in range(16,21):
    if(i==18):
        continue
    print(i)
print("Thank you!!")
print("------------------------")


#Pass Statement
for i in range(16,22):
    if(i==20):
        pass
    print(i)




