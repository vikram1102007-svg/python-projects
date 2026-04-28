n=int(input("enter your number:"))
sum=0
if n<0:
    print("please enter a positive number")
else:
    if n%2==0:
        print("even")
    else:
        print("odd")
for i in range(1,n+1):
    if i%2==0:
        sum=sum+i
print("the sum of even numbers is:",sum)        