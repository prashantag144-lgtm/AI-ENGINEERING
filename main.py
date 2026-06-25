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



