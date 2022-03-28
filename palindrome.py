#! /usr/bin/python3

#input: int
#output: boolean value
#edge cases: negative numbers
#constrictions: no strings no floats

"""
Ex 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Ex 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Ex 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

def palindrome(int):
  #if negative return false
  if int < 0:
    return False
  #convert to string and break up each digit
  input = list(str(int))
  #target first digit from input  [1,2,1]
  for n in range(len(input)):
   if input[n] == input[len(input)-1-n]:
     if (len(input)-1-n)<0:
       break 
     continue
  #see if it equals last digit
  #if in any circumstance it doesn't match than return false
   else:
     return False
  #else return true
  return True

def assertPalindrome(actual, expected, description):
  if actual == expected:
    print('Test passed')
  else:
    print('Expected '+expected+'but got '+actual+ ': '+description)

assertPalindrome(palindrome(12345678900987654321),True, 'Supposed to return true or false if its input is reversed')
assertPalindrome(palindrome(344004040),False, 'Supposed to return true or false if its input is reversed')
assertPalindrome(palindrome(1000),False, 'Supposed to return true or false if its input is reversed')
assertPalindrome(palindrome(1234567890987654321),True, 'Supposed to return true or false if its input is reversed')




