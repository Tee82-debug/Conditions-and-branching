# Write a Python program to determine the largest among three numbers entered by the user.

num1 = int(input( 'Enter a number '))
num2 = int(input( 'Enter a number '))
num3 = int(input( 'Enter a number '))

max_num = num1 
if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3 

print ("The max number is", max_num)

# Second approach

num[]

for i in range(3):
    num = int(input("Enter a number: "))
    numbers.append(num)
max_num = max(numbers)