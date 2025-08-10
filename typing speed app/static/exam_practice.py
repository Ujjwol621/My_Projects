"""a = int(input("enter the number you want to get multipication table of : "))
for i in range(1,11):
    print(f"{a}*{i}={a*i}")"""

"""sentence = input("Enter a string you want to reverse : ")
print(f"Reverse of string {sentence} is {sentence[::-1]}")"""

'''name='ujjwol'
print('Name : {}'.format(name))'''
'''
while True:
    # Get user input
    first_num = int(input("Enter the first number : "))
    second_num = int(input("Enter the second number : "))
    operation = input("Choose '+', '-', '*', '/' which operation do you want to take in : ")

    # Perform the chosen operation
    if operation == '+':
        print(f"{first_num} + {second_num} = {first_num + second_num}")
    elif operation == '-':
        print(f"{first_num} - {second_num} = {first_num - second_num}")
    elif operation == '*':
        print(f"{first_num} * {second_num} = {first_num * second_num}")
    elif operation == '/':
        if second_num != 0:
            print(f"{first_num} / {second_num} = {first_num / second_num}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Please choose the correct operation given!!!")

    # Ask the user if they want to continue
    ch = input("Do you want to continue? (y/n): ")
    if ch.lower() != 'y':
        break
'''

'''first_num = int(input("Enter the first number : "))
second_num = int(input("Enter the second number : "))
operation = input("Choose '+', '-', '*', '/' which operation do you want to take in : ")
match operation:
    case '+':
        print(f"{first_num} + {second_num} = {first_num + second_num}")
    case '-':
        print(f"{first_num} - {second_num} = {first_num - second_num}")
    case '*':
        print(f"{first_num} * {second_num} = {first_num * second_num}")
    case '/':
        print(f"{first_num} / {second_num} = {first_num / second_num}")'''

'''year = int(input("Enter the year : "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")'''

'''user_input = input("Enter a number: ")
try:
    number = int(user_input)
    valid_input = True
except ValueError:
    print("Please enter a valid integer number!!")
    valid_input = False

if valid_input:
    if isinstance(number, int):
        if number == 0:
            print("zero")
        elif number % 2 == 0:
            print("Even")
        else:
            print("Odd")'''

'''condition = True
while condition:
    print("i love you")
    ch = input("do you love me? y for yes and n for no : ")
    if ch == 'n' or ch=='N':
        print("NO i hate you")
        condition=False'''

'''my_list = [3,4,5,2,0]
user_input = int(input("Enter number "))
if user_input in my_list:
    print(f"{user_input} xa hai")
else:
    print("xaina")'''

'''a,b=0,1
user_in = int(input("Enter the no of series : "))
print("Fibonacci series : ")
c=a+b
print(a,b,c,end=' ')
for num in range(user_in):
    a=b
    b=c
    c=a+b
    print(c,end=' ')'''

'''rows=5
for i in range(rows):
    for j in range(i+1):
        print("*",end=' ')
    print()

for i in range(rows-1,0,-1):
    for j in range(i):
        print("*",end=' ')
    print()'''

'''my_list = []
for i in range(5):
    user_in = int(input("Enter the no to add to list : "))
    my_list.append(user_in)
print(my_list)'''

'''my_list=[1,2,2,3,4,2]
new_list=[]
for i in my_list:
    if i!=2:
        new_list.append(i)
print(new_list)

new_list.pop(0)
print(new_list)'''

'''for i in range(1,11,2):
    print(i)'''

'''my_dict = {'a':1, 'b':2, 'c':3}
for key in my_dict:
    print(f"{key}:{my_dict[key]}")'''

'''my_dict={'name':'ujjwol','age':21}
def func(my_dict):
    return list(my_dict.values())
a=func(my_dict)
print(a)'''

'''def factorial(n):
    if n==0:
        return 1
    else:
        return(n*factorial(n-1))
n = int(input("Enter a number to get the factorial of : "))
result=factorial(n)
print(result)'''

'''list = []
n=int(input("Enter no of elements you want to add in list : "))
for i in range(n):
    user_in=int(input(f"Enter {i+1} element : "))
    list.append(user_in)
print(list)
print(sum(list))
print(max(list))
print(min(list))
print(int(sum(list)/len(list)))'''
'''
def checkpalindrome(str):
    a=str[::-1]
    if a==str:
        print(f"{str} is a palindrome")
    else:
        print(f"{str} is not a palindrome")
s=input("Enter a string : ")
checkpalindrome(s)'''

import my_module