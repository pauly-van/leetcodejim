# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
"""
An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

 ([]{}[](()))

(())
first (
3 )
4 )

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

"""

#input: string
#output: boolean value
#edge cases: 
 # - check for first index 
  # var says theres open paran
#constraits: 

#

#break input string into a list
# compare first index of string into next index of string 
# return true if theres an open and close 
 # need to figure out how to determine if the ch is open and close

def paren(str):
    