'''Store:

name

age

marks

passed (True/False)

Print a formatted result like:

Student Sam is 20 years old.
Marks: 85.5
Passed: True'''
name="Sam"
age=19
marks=90
passed=True
print(f"Student {name} is {age} years old.")
print(f"Marks: {marks}")
print(f"Passed: {passed}")
print('------------------------------------------------------------------------------------')
'''Create a variable x = 5
Do:

x = x + 5
x = x * 2'''
x=5
x=x+5
x=x*2
print(x)
print("------------------------------------------------------------------------------------------")
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print("--------------------------------------------------------------------------------------------")
'''Create two float numbers and print their sum rounded to 2 decimal places.'''
num1=18.76
num2=19.876
sum=round(num1+num2,2)
print(sum)
print("-------------------------------------------------------------------------------------------------")
'''Take an integer and check:

Is it positive?

Is it negative?

Is it zero?'''
num=12
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")
