#Write a Python program to create a basic calculator that performs the following
m = int(input('enter:'))
n = int(input('enter:')) 
operator = str(input('enter operators like + - % * / : '))
if operator =="+" :
    print(m+n) 
elif operator == "-" :
    print(m-n) 
elif operator == "*" :
    print(m*n) 
elif operator == "/" :
    print(m/n) 
elif operator == "%" :
    print(m%n)  
else :
    print("invalid operator")  

#Write a Python program to print the first N terms of the Fibonacci series using a while loop. 
num = int(input("enter: ")) 
a, b = 0, 1
count = 0
while count < num:
    print(a, end=" ")
    a, b = b, a + b
    count += 1 

#Write a program to check whether a number is an Armstrong number using a while loop. Example: 153 → 1³ + 5³ + 3³ = 153 
a = int(input('enter: ') ) 
num = a 
res= 0 
lenght = len(str(num))
while a >0 :
    dight = a % 10 
    res = res + dight ** lenght
    a// 10 
if res == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

#Write a program to find the greatest digit in a given number using a while loop 
a = int(input('enter: ')) 
max_num = 0
while a > 0 :
    dight = a % 10 
    if dight > max_num :
        max_num== dight 
    a//10 
print(max_num) 

# Find the greatest among three numbers

a = float(input("Enter first number : "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    grt = a
elif b >= a and b >= c:
    grt = b
else:
    grt = c

print("The greatest number is:", grt) 

#Write a function sum_numbers(*args) that accepts any number of arguments and returns their sum.

def sum(*args):
    total = 0
    for num in args:
        total += num
    return total
print( sum(1, 2, 3))   

#rite a function display_info(**kwargs) that prints all key-value pairs passed as arguments.
def display(**kwargs):
    for key,value in kwargs.items():
        print(key,value) 
display(name = "pooja" ,age = 24, graduation = 'btech')
                  
# Program to calculate sum at even and odd indices
num = list(map(int, input("Enter element by space: ").split()))
even= 0
odd= 0
for i in range(len(num)):
    if i % 2 == 0:
        even += num[i]
    else:
        odd+= num[i]
print(even)
print(odd) 

#Modify the list such that all even numbers are halved, odd numbers remain unchanged. Example: Input: [4, 7, 8, 3] → Output: [2, 7, 4, 3] 
a = list(map(int,input('enter number by space').split()))
for i in range(len(a)):
    if a[i] % 2 == 0 :
        a[i]//=2 
print(a) 

#perfect number or not 
num = int(input("Enter a number: "))
total = 0
for i in range(1, num):
    if num % i == 0:
        total += i
print("Perfect Number" if total == num else "Not a Perfect Number") 

# uppercase and lowercase separate
ses = input("Enter a sentence: ")
uppercase_letters = ""
lowercase_letters = ""
for char in ses:
    if char.isupper():
        uppercase_letters += char
    elif char.islower():
        lowercase_letters += char
print( uppercase_letters)
print( lowercase_letters)




    

    


