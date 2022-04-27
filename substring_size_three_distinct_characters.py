"""
A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

input: string
output: the set of substring in the string of 3 characters
constraint: length of string has to be between 1 and 100
"""

# take the string and slice it into 3 characters for the whole string
# place the substring into a list
# add each character into a set to determine if the substring is unique
#return the substring index plus 1 of the unique substring

import dis


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        spliced_into_threes = []
        for three_ch in range(len(s)-2):
           spliced_into_threes.append(s[three_ch:three_ch+3])
        
        for index, substring in enumerate(spliced_into_threes):
            distinct_string = set()
            for uniq_ch in substring:
                distinct_string.add(uniq_ch)
            if len(distinct_string) == 3:
                return index+1
        
        

e1 = Solution()
e2 = Solution()
print(e1.countGoodSubstrings('xyzzaz'), e2.countGoodSubstrings('aababcabc'))
