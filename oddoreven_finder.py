n=int(input("enter your number:"))
sum=0
odd_sum=0
even_sum=0
if n<0:
    print("please enter a positive number")
else:
    if n%2==0:
        print("even")
    else:
        print("odd")
for i in range(1,n+1):
    if i%2==0:
        even_sum+=i      
    else:
        odd_sum+=i
print("the sum of even numbers is:",even_sum)          
print("the sum of odd numbers is:",odd_sum)

for i in range(1,n+1):
    sum+=i
print("the sum of all numbers is:",sum)

