print("Welcome to the calculator")
a=input("Enter your Operator:")
how=int(input("Enter with how many numbers you want to perform operation:"))
sum=0
subtract=0
multiply=0
divide=0

if a == '+':
 for i in range(0,how):
        n=int(input("Enter number:"))
        sum+=n
 print(sum)
 
elif  a == '-':
 for i in range(0,how):
        n0=int(input("Enter number:"))
        subtract-=n0   
 print(subtract)
 
elif  a == '*':
 for i in range(0,how):
        n1=int(input("Enter number:"))
        multiply*=n1  
 print(multiply)    
        
else:
 for i in range(0,how):
        n2=int(input("Enter number:"))
        divide/=n2
 print(divide)