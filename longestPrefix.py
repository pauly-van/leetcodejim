"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

#input: list of strings
#output: the prefix of the longest character of strings in the list
#edge case: when skipping a word we need to compare with our total string and continue that index
#constraints: 
# 1 <= strs.length <= 200.  
# 0 <= strs[i].length <= 200.  
# strs[i] consists of only lower-case English letters.

#example1 ["dog", "flow", "flight", "fist", "fish", "find", "finish"]
#example2 Input: {"geeksforgeeks", "gekks", "geek", "geezer"}

#what are the limitations.  Control the integers that loops

# add all prefix we find into a dict 



example1 = ["dog", "flow", "flight", "fist", "fish", "find", "finish"]


def longestCommonPrefix(strs):
    prefix=""
    if len(strs)==0: return prefix
    
    for i in range(len(min(strs))):
        c=strs[0][i]
        if all(a[i]==c for a in strs):
            prefix+=c
        else:
            break
    return prefix


print(longestCommonPrefix(example1))