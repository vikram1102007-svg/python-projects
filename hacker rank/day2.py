class Solution(object):
    def gcd(self,x,y):
        while y!=0:
            x,y=y,x%y
        return x
    def gcdOfStrings(self, str1, str2):
        a=len(str1)
        b=len(str2)
        c=self.gcd(a,b)
        if str1+str2==str2+str1:
            return str1[:c]
        else:
            return ""
m=str(input("Enter first string: "))
n=str(input("Enter second string: "))
o=Solution()
print("your repetative string is: "+o.gcdOfStrings(m,n))
print("Thank you!")
print("Have a nice day!")