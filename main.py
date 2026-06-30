""" print("Namaste India"); """

# comments and variables in Python
'''
age=12
age1=24
name="Prashanth"
print(type(name))
print(name)
print(age)
v=3j
print(type(v))
print(v)'''

""" st='124343444444  sdgfffffffg 3434'
print(type(st))
 """
""" b=True
c=False

print(type(b))


st='A'
print(ord(st))
st1='a'
print(ord(st1)) """

""" name="Prashanth"
age=21
print(f"my name is {name} and my age is {age}") """

""" age=int(input("hello what is your age"))
print(f"my age is :{age}")
 """
""" 
print(24>34)
print(23==23)
print(23>34)
print((456 == 456) != (235 == 236)) """

""" print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)
print(True and bool(0)) """
""" print(bool(0))
print(bool(1))
a=12
b=13
print(a//b)

 """

"""  CONDITIONAL STATEMENTS  """

""" Q1. Accept two numbers and print the greatest between them. """

""" 
num1=int(input("enter a number1"))
num2=int(input("enter a number2"))
if(num1>num2):
    print("num1 is greater than num2")
else:
    print("nums2 is greater than num1") """

""" 
Q2. Accept the gender from the user as char and print the respective greeting message
Ex - Good Morning Sir (on the basis of gender) """
""" 
ch=str(input("enter a gender of Yours"))
if(ch=="M"):
    print("Good Morning sir")
elif(ch=='F'):
    print("Good Morning Madam")

 """

""" Q3. Accept an integer and check whether it is an even number or odd. """

""" a=int(input("enter a number"))

if(a%2==0):
    print("this number is even number")
else:
    print("this number is odd number")
 """

""" Q4. Accept name and age from the user. Check if the user is a valid voter or not.
Ex- “hello shery you are a valid voter” """

""" name=str(input("enter a name"))
age=int(input("enter a number"))
if(age>18):
    print(f" the name {name} is eligible to voting")

else:
    print(f"the name {name} is not eligible fot voting") """


""" Q5. Accept a year and check if it a leap year or not (google to find out what is a leap year) """

""" year =int(input("enter a year which you want"))
if((year%4==0)and(year%100!=0)):
    print(f"the year {year} is a leap year")
elif(year%400==0):
    print(f"the year is a leap year")
else:
    print(f"the year {year} is not a leap year") """

"""Q6. take the input of temperature in celsiusX
Below 0°C → "Freezing Cold b
0°C to 10°C → "Very Cold b
10°C to 20°C → "Cold b
20°C to 30°C → "Pleasant b
30°C to 40°C → "Hot b
Above 40°C → "Very Hot " """

""" temp=int(input("enter a temperature"))
if(temp<=0):
    print("freezing cold")
elif(temp>0 and temp<=10):
    print("Very cold")
elif(temp>10 and temp<=20):
    print("cold")
elif(temp>20 and temp<=30):
    print("Pleasant")
elif(temp>30 and temp<=40):
    print("hot")
else:
    print("very hot") """


""" LOOPS """

""" Accept an integer and Print hello world n times """
""" n=int(input("enter a number"))  """
""" for i in range(0,n):
    print("hello world")
     """
""" Reverse for loop. Print n to 1 """

""" for i in range(n,0,-1):
    print(i)
 """

""" - Take a number as input and print its table """

""" n=int(input("Enter which table you want to print"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")
 """
""" Sum up to n terms """

""" sum=0
n=int(input("Enter a number upto which you wnat to do"))
for i in range(0,n):
    sum+=i

print(sum) """

""" Factorial of a number """

""" fact=1
n=int(input("enter a number "))
for i in range(1,n):
    fact=fact*i

print(fact) """

""" Print the sum of all even & odd numbers in a range separately """

""" n=int(input("enter a number"))
even=0
odd=0
for i in range(0,n):
    if(i%2==0):
        even+=i
    else:
        odd+=i

print(f"the sum of even number is{even} and the sum of odd number is{odd}") """

""" Print all the factors of a number """

""" n=int(input("Enter a number"))
for i in range(1,n):
    if(n%i==0):
        print(i) """

"""  Accept a number and check if it a perfect number or not. """
""" 
n=int(input("Enter a number"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i 

if(sum==n):
    print(f"the given number {n} is the perfect number")
else:
    print(f"the given number {n} is not a perfect number") """

""" Check wether the number is prime or not """

""" n=int(input("Enter a number"))
sum=0
count=0
for i in range(1,n+1):
    if(n%i==0):
        count+=1
    
if(count==2):
    print(f" the given number {n} is a prime number")
else:
    print(f"the given number {n} is not a prime number")
 """

""" Reverse a string without using in build functions. """

""" rev=""
str1="prashanth"
for i in range(len(str1)-1,-1,-1):
    rev=rev+str1[i]

print(rev) """

""" Reverse a string without using in build functions """

""" str1="prashanth"
rev=""
temp="Prashanth"
for i in range(len(str1)-1,-1,-1):
    rev=rev+str1[i]


if(temp==str1):
    print("the given name is pallindrome")

else:
    print("the given name is not pallindrome")
     """
""" Separate each digit of a number and print it on the new line """

""" n=int(input("enter a random number"))
ans=0
while(n>0):
    ans=n%10
    print(ans) 
    n=n//10 """

""" Accept a number and print its reverse """

""" n=int(input("enter a random number"))
rev=0
ans=0
while(n>0):
    ans=n%10
    rev=rev*10+ans
    n=n//10

print(rev)

 """

""" Accept a number and check if it is a pallindromic number (If number and its reverse are equal? """

""" n=int(input("enter a random number"))
temp=n
ans=0
rev=0
while(n>0):
    ans=n%10
    rev=rev*10+ans
    n=n//10

if(temp==rev):
    print(f"the given number {rev} is pallindrome number")
else:
    print(f"The given number {rev} is not a pallindrome number")
 """

    
""" Create a random number guessing game with python. """

""" print("THE NUMBER GUESSING GAME")
n=int(input("Enter a random number"))
attempt=10
count=0
while(attempt>0):
    guess=int(input("enter a number"))
    if(guess==n):
        count+=1
        print("YOU ARE WINNER")
    else:
        print("TRY ONCE AGAIN")


if(count==1):
    print("YOU ARE wINNER")
else:
    print("YOU ARE LOOSER")

 """


""" FUNCTIONS """

""" def greet():
    print("hello world")

greet() """

""" 
def sum(a,b):
    sum1=a+b
    return sum1

a=int(input("enter a number"))
b=int(input("enter a number"))
print(sum(a,b))


 """
""" def greet(name):
    print(f"good morning {name}")

name=input("Enter your name to greet")
greet(name)
 """


""" LIST """

""" Print positive and negative elements of an List? """

""" num=[1,2,4,4,2,5,3,2,5]
nums1=[]
nums2=[]
for i in num:
    if(num[i]%2==0):
        nums1.append(num[i])
    else:
        nums2.append(num[i])


print(nums1,nums2) """


""" Mean of List elements? """

""" nums=[1,2,4,4,2,5,3,2,5]
sum=0
n=len(nums)

for i in nums:
    sum+=nums[i]

print(sum//n)
 """

""" Find the greatest element and print its index too? """

""" nums=[1,2,4,4,2,5,3,2,5]
maxi=-1
for i in nums:
    maxi=max(maxi,nums[i])

print(f"The maximum element is {maxi} and the index is {nums.index(maxi)}") """



""" Check if List is sorted or not. """

""" nums=[2,4,5,6,7,8]
for i in range(0,len(nums)-1):
    if(nums[i]>nums[i+1]):
        print("This list is unsorted")
        break
    else:
        continue
        

 """

""" TUPLES """

""" Tuples are hetergoenus in nature , means all the datatypes or some other functions and all can be include in the tuple 
    Tuples are immutable in nature and can have duplcates in this """

""" a=(1,2,3,4,2,4,print("hello"),'a','b','b','c','v')

print(a.count(2))
print(a.index(4))
 """

""" SETS """

""" s={1,2,4,3,2,5}

s.add(10)
s.remove(2)
s.discard(5)
s.pop() #removes arandom elements

for i in s:
    print(i) """


""" a={1,2,3,4,3}
b={1,2,4,5,6}

s=a.union(b)
b=a.intersection(b)
print(s,b) """


""" DICTIONARY """

""" d={1:"hello",2:3,4:"world",5:"prashanth","hello":"hello"}
print(d)
print(type(d)) """

""" d={1:2,3:4,4:5,6:6}
d[2]=33
d.update({50:500}) #the one way of updating/creating the value the value
print(d) """

""" print(d[1])
for i in d:
    print(i) """

""" LOOPS IN DICTIONARY """

""" a=[10,20,30,40,50,60]
d={1:2,3:4,4:5,6:6}
for i in d:
    print(i)

for i in d:
    print(d[i]) """




""" d={1:200,3:400,4:500,6:600} 
d.clear()
 """

""" a=[1,2,4,5,4,3]
b=a
b[0]=100
print(a)

This is the deep copy
 """
""" Shallow copy """

""" a=[1,2,4,5,4,3]
b=a.copy()
b[2]=200
print(b)
print(a) """


""" Write a python dictionary to merge dictionary """

""" a={1:100,2:200,3:300,4:400,5:500}
b={13:1300,4:400,3:300,4:400,2:200,6:6000}


for i in b:
    a[i]=b[i]

 """

""" Write a Python program to sum all the values in a dictionary? """

""" d={1:100,2:200,3:300,4:400,5:500}
sum=0
for i in d:
    sum+=d[i]

print(sum) """

""" Count the frequency of each element """

""" d={1:100,2:200,3:300,4:400,5:500,5:300,6:300}
temp={}
for i in d.values():
    if(i not in temp):
        temp[i]=d[i]
    else:
        print(f"The given number {d[i]} is a duplicate number") """


""" Write a Python program to combine two dictionary by adding
values for common keys. """

""" d={1:100,2:200,3:300,4:400}
d1={1:300,4:400,6:600,3:100,2:200}

for i in d:
    d[i]=d1[i]
    d[i]=d[i]+d1[i]

print(d)
 """

""" EXCEPTIONAL HANDLING """

""" a=int(input("enter a number"))

try:
    print(10//a)
except ZeroDivisionError:
    print("there is a zero division error")


print("this line is executed sucesfully")

 """

""" a=int(input("enter a number"))
try:
    print(10//a)
except Exception as err:
    print(f"there is an excetion called {err}")

 """

""" FILE HANDLING """

""" f=open(r'file.txt')
print(f.read()) """

""" p=open('main.py')
print(p.read())
 """

""" p=open('superman.txt','a')
p.write("hello this is prashanth ,and i am writing inside this file") 
p.write("and i am appending something other stuffs inside this file") 

 """