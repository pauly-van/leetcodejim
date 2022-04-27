"""
Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

input: string and substring
output: index of first occurance or -1 if no occurance

"""

class Solution:
    def strStr(self, haystack: str, needle: str):
      if needle in haystack:
          return haystack.index(needle[0])
      if needle not in haystack:
          return -1
    

e1 = Solution()
e2 = Solution()
print(e1.strStr('hello', 'll'))
print(e2.strStr('aaaaa', 'bba'))