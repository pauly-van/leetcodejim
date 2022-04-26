"""
input: string of lowercase and uppercase characters
output: int 
contraints: between 1 and 2000 character
edge cases: upper and lowercase, spaces
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        # create a counter for longest palindrome characters
        palindrome_length = 0
        single_char = 0
        # create dictionary that collects number of letters
        characters = {}
        # remove spaces in string if there are any
        new_string = s.replace(" ", "")
        # iterate through string and add letters to dictionary
        for ch in new_string:
            if ch not in characters:
                characters[ch] = 1
            else:
                characters[ch]+=1
        # for every letter in dictionary if its a multiple of 2 add to counter for each division
        
        for k,v in characters.items():
            if v % 2 == 0:
                palindrome_length+=v
            elif v == 1:
                single_char+=1 
        
        if single_char>=1:
            palindrome_length+=1
        
        return palindrome_length
        

e1 = Solution.longestPalindrome(None, 'abccccdd')
e2 = Solution.longestPalindrome(None, 'a')
e3 = Solution.longestPalindrome(None, 'bb')
print(e1)
print(e2)
print(e3)