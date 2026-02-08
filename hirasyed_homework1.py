# CS-860 Artificial Intelligence
# Assignment 1
# Name: Hira Syed
# Reg No: 577564




print("#1  Write a program to check whether a person is eligible for voting or not. (input age from user)")
# Input age from user
age = int(input("Enter your age: "))

# Check eligibility
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

print("-----------------------------------------------------------------------")
print("#2  Write a program to check whether a number entered by user is even or odd.")
# Input number from user
num = int(input("Enter a number: "))

# Check even or odd
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
print("-----------------------------------------------------------------------")

print("#3)	Write a program check whether a number is divisible by 13 or not")
#input number from user

num=int(input("Enter a number:"))
#check if it can be divided by 13
if num%13 == 0:
    print("the number is divisible by 13")
else:
    print("the number is not divisible 13")
print("-----------------------------------------------------------------------")
print("#4	Write a program to display “ I am hero” if a number entered by user is a multiple of five, otherwise print “ This is not a hero, try again”.")

#Input from user
num=int(input("Enter the number:"))

if num%5 == 0:
    print("I am hero")
else:
    print("this is not a hero, try again")

print("-----------------------------------------------------------------------")
print("#5	Write a program to display the last digit of a number. (hint: any number % 10 will return the last digit).")

num=int(input("Enter the number:"))

if num>=0:
    last_digit=num%10
    print("the last digit is:", last_digit)
else:
    last_digit=(-num)%10
    print("the last digit is:",last_digit)
print("-----------------------------------------------------------------------")
print("#6)	Write a program to check whether a year is a leap year or not.")

year=int(input("Enter the year:"))

if (year%400==0) or (year%4==0 and year%100!=0):
    print("this is leap year")
else:
    print("this is not leap year.")
print("-----------------------------------------------------------------------")
print("#7)	Accept any city from the user and display the monument of that city. For example city of Islamabad,  Monument the Pakistan Monument.")

city=input("Enter a city name:").lower()

if city == "islamabad":
    print("Monument: Pakistan Monument")
elif city == "lahore":
    print("Mounument: Minar e Pakistan")
elif city == "karachi":
    print("Monumet: Mizar e Quaid")
elif city == "multan":
    print("Monument: Tomb of Shah Rukn e Alam")
elif city == "peshawar":
    print("Monument: Bala Hisar Fort")
elif city == "quetta":
    print("Quaid e Azam Residency - Ziarat")
elif city=="rawalpindi":
    print("Mounument: Liaquat Bagh")
else:
    print("Mounument info not available")
print("-----------------------------------------------------------------------")

print("#8)	Accept the age of four people and display the youngest one.")
#method 1
a1=int(input("Enter age of first person:"))
a2=int(input("Enter age of second person:"))
a3=int(input("Enter age of third person:"))
a4=int(input("Enter age of fourth person:"))

if a1<a2 and a1<a3 and a1<a4:
    print("First person is youngest.")
elif a2<a1 and a2<a3 and a2<a4:
    print("Second person is youngest.")
elif a3<a1 and a3<a2 and a3<a4:
    print("Third person is youngest.")
else:
    print("Fourth person is youngest.")

#method 2
a1=int(input("Enter age of first person:"))
a2=int(input("Enter age of second person:"))
a3=int(input("Enter age of third person:"))
a4=int(input("Enter age of fourth person:"))

youngest = min(a1, a2, a3, a4)

if youngest == a1:
    print("First person os youngest.")
elif youngest == a2:
    print("second person is youngest")
elif youngest == a3:
    print("third person is youngest.")
else:
    print("fourth person is youngest")

print("-----------------------------------------------------------------------")
print("#9)	Write a program to check whether a character is a vowel or not.")

ch=input("Enter a single alphabet:")

if ch in ('a','e','i','o','u'):
    print("it is a vowel")
else:
    print("it is not a vowel")
print("-----------------------------------------------------------------------")
print("#10)	Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.")

a=int(input("Enter first side of triangle:"))
b=int(input("Eneter second side of triangle:"))
c=int(input("Enter third side of triangle"))

if a==b==c:
    print("this is an equilateral triangle")
elif a==b or b==c or a==c:
    print("it is an isoceles triangle.")
else:
    print("it is a scalene triangle")

print("-----------------------------------------------------------------------")

print("11)	Write a Python program to guess a number between 1 and 9. ")

print("Lets play a guessing game (1-9)")
print("think of any number to start a game..")

base=int(input("enter any number to start"))
secret_number = (base*7+3)%9
if secret_number==0:
    secret_number==9

while True:
    guess=int(input("guess a number between 1&9:"))

    if guess==secret_number:
        print("WELL GUESSED!!")
        break
    else:
        print("Try Again")


print("-----------------------------------------------------------------------")
print("12)	Write a Python program to construct the following pattern, using a nested for loop.")
n=5
for i in range(1, n+1):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n-1, 0, -1):
    for j in range(i):
        print("*",end=" ")
    print()


print("-----------------------------------------------------------------------")

print("13)	Write a Python program that accepts a word from the user and reverses it.")

word = input("Enter a word:")
reversed_word=""
for char in word:
    reversed_word=char+reversed_word
print("Reversed Word:", reversed_word)

print("-----------------------------------------------------------------------")

print("14)	Write a Python program to count the number of even and odd numbers in a series of numbersSample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) ")

numbers = (1,2,3,4,5,6,7,8,9)
even_count=0
odd_count=0

for num in numbers:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1

print("Even number count:", even_count)
print("Odd number count:", odd_count)

print("-----------------------------------------------------------------------")
print("15)	Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.")

for i in range(7): 
    if i==3 or i==6:
        continue
    print(i,end=" ")


print("-----------------------------------------------------------------------")
print("16)	Write a Python program to get the Fibonacci series between 0 and 50.")

a, b = 0, 1
while b<50:
    print(b, end=" ")
    a, b= b, a+b

print("-----------------------------------------------------------------------")
print("17)	Write a Python program that iterates the integers from 1 to 50. For multiples of three print Fizz, for multiples of five print Buzz. For numbers that are multiples of three and five, print FizzBuzz.")

for i in range(1,51):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)


print("-----------------------------------------------------------------------")
print("18)	Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j")

m=int(input("Enter number of rows:"))
n=int(input("Enter no. of columns:"))

array=[]

for i in range(m):
    row=[]
    for j in range(n):
        row.append(i*j)
    array.append(row)
print(array)


print("-----------------------------------------------------------------------")
print("19)	Write a Python program to check the validity of passwords input by users")

password=input("Enter Your Password:")
has_lower=False
has_upper=False
has_digit=False
has_special=False

for ch in password:
    if ch.islower():
        has_lower=True
    elif ch.isupper():
        has_upper=True
    elif ch.isdigit():
        has_digit=True
    elif ch in "$#@":
        has_special=True

if len(password) < 6 or len(password) > 16:
    print("Invalid passwrd: length must be between 6 and 16 characters.")
elif not has_lower:
    print("Invalid Password: must contain at least one lower letter [a-z]")
elif not has_upper:
    print("Invalid Passwrod: must conetain at leats one upper case letter [A-Z]")
elif not has_digit:
    print("Invalid Password: must contain atleats one digit[0-9]")
elif not has_special:
    print("Invalid Password: must contain atleast one special character [$#@]")

else:
    print("Valid Password")


print("-----------------------------------------------------------------------")
print("20)	Write a Python program to print the alphabet pattern 'E'.")

for row in range(7):
    for col in range(5):
        if col==0 or row==0 or row==3 or row==6:
            print("*", end="")
        else:
            print("",end="")
    print()

print("-----------------------------------------------------------------------")
print("21)	Write a Python function to find the maximum of three numbers.")

def maximum_of_three(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
    
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number"))
num3 = float(input("Enter third number"))

print("the maximum number is:", maximum_of_three(num1,num2,num3))

print("-----------------------------------------------------------------------")
print("22)	Write a Python function to sum all the numbers in a list")

def sum_list(numbers):
    total = 0
    for n in numbers:
        total+=n
    return total

nums = [8,2,3,0,7]

print("Sum of all numbers:", sum_list(nums))

print("-----------------------------------------------------------------------")
print("23)	Write a Python function to multiply all the numbers in a list.")

def multiply_list(numbers):
    result = 1
    for n in numbers:
        result*=n
    return result

nums=[8,2,3,-1,7]
print("Product of all numbers:", multiply_list(nums))


print("-----------------------------------------------------------------------")
print("24)	Write a Python program to reverse a string.")

def reverse_string(s):
    reversed_str=""
    for char in s:
        reversed_str=char+reversed_str
    return reversed_str

text1="dfhsdjr327432"

print("Reversed String is:",reverse_string(text1))

print("-----------------------------------------------------------------------")
print("25) Define a function to check if a string is a palindrome")

def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
    
text2 = input("Enter a phrase or a word:")
if is_palindrome(text2):
    print("It is a plaindrome")
else:
    print("It is not a palindrome")

print("-----------------------------------------------------------------------")
print("26)	Write a Python function that prints out the first n rows of Pascal's triangle.")

def pascal_triangle(n):
    for i in range(n):
        num = 1
        for j in range(i+1):
            print(num, end="")
            num=num*(i-j)//(j+1)

        print()

rows=int(input("Enter the number of rows:"))
pascal_triangle(rows)

print("-----------------------------------------------------------------------")
print("27)	Write a Python function to check whether a string is a pangram or not.")

def is_pangram(sentence):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    for letter in alphabet:
        if letter not in sentence:
            return False
        
    return True
text = input("Enter a sentence")

if is_pangram(text):
    print("The sentence is a pangram.")
else:
    print("This sentence is not a pangram")

print("-----------------------------------------------------------------------")
print("28)	Write a Python program that invokes a function after a specified period of time")

def manual_sqrt(number):
    guess=number/2
    for i in range(10):
        guess=0.5*(guess+number/guess)
    return guess

def delay(milliseconds):
    count=0
    for i in range(milliseconds*1000):
        count+=1

def delayed_square_root(number, delay_ms):
    print(f"Square root after {delay_ms} milliseconds:")
    delay(delay_ms)
    print(manual_sqrt(number))

delayed_square_root(16,1)
delayed_square_root(100,1)

print("-----------------------------------------------------------------------")
print("29)	Write a program to find out the prime factors of a number.")

def prime_factors(n):
    i=2
    factors=[]
    while i<=n:
        if n%i == 0:
            factors.append(i)
            n=n//i
        else:
            i+=1
    return factors

num=int(input("Enter a number:"))
print("Prime factors of ", num, "are", *prime_factors(num))


print("-----------------------------------------------------------------------")
print("30)	Write a function that converts a decimal number to a binary number.")

def decimal_to_binary(n):
    binary = ""
    if n ==0:
        return "0"
    while n>0:
        remainder=n%2
        binary=str(remainder)+binary
        n=n//2
    return binary

num=int(input("Enter a decimal number:"))
print("Binary number:", decimal_to_binary(num))


print("-----------------------------------------------------------------------")
print("Write a function cubesum() that accepts an integer and returns the sum of the cubes of individual digits of that number")

def cubesum(n):
    total=0
    while n>0:
        digit=n%10
        total+=digit**3
        n=n//10
    return total

def isArmstrong(num):
    return num==cubesum(num)

def PrintArmstrong(start,end):
    print("Armstrong numbers between", start, "and", end, "are:")
    for i in range(start, end+1):
        if isArmstrong(i):
            print(i)

num=int(input("Enter a number:"))
if isArmstrong(num):
    print(num, "is an Armstrong number.")

else:
    print(num, "is not an Armstrong number.")

PrintArmstrong(1,500)


print("---------------------------THE END--------------------------------------------")
