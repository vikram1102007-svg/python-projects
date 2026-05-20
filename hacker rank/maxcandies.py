class Solution(object):
    def maxcan(self,candies):
        maxcan=candies[0]
        for i in candies:
            if maxcan<i:
                maxcan=i
        return maxcan

    def kidsWithCandies(self, candies, extraCandies):
        maximum=self.maxcan(candies)
        m=[]
        for i in candies:
            a=i+extraCandies
            if a>=maximum:
                m.append(True)
            else:
                m.append(False)
        return m
c1=Solution()
print(c1.kidsWithCandies([2,3,5,1,3],3))