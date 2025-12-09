'''Create a variable storing a 4-digit number.
Extract each digit using operators (// and %) and print them separately.
'''
num=1234
#extract last digit divide by 10 % it gives remainder
num1=num%10
print(num1)
#cut the last digit in num using //
num=num//10
#extract last digit divide by 10 % it gives remainder
num2=num%10
print(num2)
#extract last digit divide by 10 % it gives remainder
num=num//10
#extract last digit divide by 10 % it gives remainder
num3=num%10
print(num3)
#extract last digit divide by 10 % it gives remainder
num//=10
#extract last digit divide by 10 % it gives remainder
num4=num%10
print(num4)
