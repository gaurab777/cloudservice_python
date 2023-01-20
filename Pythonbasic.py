print("Hello World!")
print("Iam a python intern at cloud tech service.")

Age=18
Percentage=80.90
Name="James"

print(Age)
print(Percentage)
print(Name)

a=b=c=12
print(a)
print(b)
print(c)

x,y,z = 100,200,'Python'

print(x)
print(y)
print(z)

str='Hello World'
list=[1,'apple','mango','banana','orange']
tuple=(2,'pineapple','watermelon','papaya','guava')

print(tuple)

Dict={1:"Python",2:"Java",3:"MySQL",4:"C#"}

#Set is unorder data type
set={'James',2,3,'Python'}

#to check data type
print(type(a))

print(float(10))

age = "10"
print(type(age))

int(age)

print(type(age))


name = input("Enter your name:")
print("Your're ",name)

num = input("Enter your roll number:")
print(num)

#Everything input will be converted to string
#typecasting

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

print(number1+number2)

per=float(input("Enter your percentage: "))
print(per)
print(type(per))


#Taking multiple inputs
x,y = input("Enter no. of boys and girls: ").split()
print("Number of boys: ",x)
print("Number of girls: ", y)

#Output Formatting
#Modulo Method
print("Rank:%d, Percentage:%f"%(1,9.987))
print("Total students:%5d, Boys:%d" %(240,120))
print("Growth is %.3f" %(10.75))
print("The number of boys is %d, which id %.3f percentage of total students" %(40,45.5))

#format method
print("I am learning {0} from the {1}".format('Python','Expert'))

def main():
    print("hello world!")
    name = input("What is your name? ")
    print("Nice to meet you,", name)

if __name__ == "__main__":
    main()


for i in range(5):
    print(i)

list(range(0, 10, 3))

print("I am learning {0} from the {1}".format('Python',1))















