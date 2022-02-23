#Program that reads in two numbers and outputs the integer answer and remainder
#Author Lais

num1 = input ('Enter first number: ')
num2 = input ('Enter the number yout want to divide by: ')
result = (num1//num2)
remainder = num1%num2
print (" {} divided by {} is {} with remainder {}".format (num1,num2,result,remainder) )
