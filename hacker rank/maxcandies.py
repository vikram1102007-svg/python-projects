class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maximum=max(candies)
        m=[]
        for i in candies:
            a=i+extraCandies
            if a>=maximum:
                m.append(True)
            else:
                m.append(False)
        return m