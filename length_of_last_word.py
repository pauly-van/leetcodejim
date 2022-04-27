"""
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
input: string
output is the lenght of the last word in that string
"""

class Solution:
    def lengthOfLastWord(self, s:str) -> int:
        split_s = s.split()
        return len(split_s[len(split_s)-1])


e1 = Solution()
print(e1.lengthOfLastWord('Hello World'))
print(e1.lengthOfLastWord('   fly me   to   the moon  '))
print(e1.lengthOfLastWord('luffy is still joyboy'))