def factorial(n):
    if n<0:
        print("please enter a positive number")
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        for i in range(2,n+1):
            fact*=i
        return fact
n=int(input("enter your number:"))
print("the factorial of",n,"is:",factorial(n))

if factorial(n)==1:
    print("the factorial of",n,"is:",factorial(n))
    