class Solution(object):
    def mergeAlternately(self, word1, word2):
        a = []

        for x, y in zip(word1, word2):
            a.append(x)
            a.append(y)

        a.append(word1[len(word2):])
        a.append(word2[len(word1):])

        return "".join(a)

n1 = Solution()
n2 = Solution()

print(n1.mergeAlternately("abc", "pqr"))
print(n2.mergeAlternately("ab", "pqrs"))