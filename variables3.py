#Swap two variables without using third variable.
a,b=10,20
a,b=b,a
print(a)
print(b)
print("--------------------------------------------------------------------------")
'''Create a variable storing your name and age. Print:

My name is Sam and I am 21 years old.'''
name="Sam"
age=19
print(f"My name is {name} and I am {age} years old")
print("--------------------------------------------------------------------------")
#Convert boolean True into integer. What is the output?
var=int(True)
print(var)
print("--------------------------------------------------------------------------")
'''Create three variables: int, float, string. Convert all into string and concatenate.'''
var_integer=10
var_float=10.0
var_string="10"
conversion=str(var_integer)+str(var_float)+var_string
print(conversion)
print("--------------------------------------------------------------------------")
'''Find datatype of:

x = 5 > 3=> My answe is bool'''
x=5>3
print(type(x))
print("--------------------------------------------------------------------------")
#Create a string "50" and multiply it by 3. Observe result.
print("50"*3)
print("--------------------------------------------------------------------------")
#Divide two integers and check datatype of result.
a=16.9
b=2.0
c=(a/b)
print(c)
print(type(c))
print("--------------------------------------------------------------------------")
#Create a variable with value None. Print its type.
my_var=None
print(type(my_var))
print("--------------------------------------------------------------------------")
#Write a small program that converts Celsius to Fahrenheit.
cel=100
f=(cel*9/5)+32
print(f)
