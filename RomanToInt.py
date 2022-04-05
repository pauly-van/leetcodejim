#! /usr/bin/python3

#input: A valid roman nume
#output: int
#edge case: 4 and 9, 14, etc etc
#contraint: can't be zero, input can only be characters ('I', 'V', 'X', 'L', 'C', 'D', 'M'), valid roman numerical in range [1,3999]

"""
Input: s = "III"
Output: 3
Explanation: III = 3

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

from ast import Num, Str


def romanToInt(s):
  #create a table to define each roman number to a value 
  table = {"I": 1, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
  # Break input into list [X, I, V]
  input = list(s) #[X, I, V, X] +1 === nothing
  #loop thru table to find value
  total = 0
  shouldContinue = False
  keys = list(table.keys()) #an array of keys ['I', 'V', 'X', 'L', 'C', 'D', 'M']
  for r in range(len(input)): 
    if shouldContinue == True:
      shouldContinue = False
      continue
    for n in range(len(keys)): #keys
      if r == len(input)-1 and input[r] == keys[n]:
        total = total + table[input[r]] 
        break
      key = input[r]+input[r+1] 
      if key in table.keys():
        total = total + table[key]
        shouldContinue = True
        break
      elif input[r] == keys[n]:
        total = total + table[input[r]] 
        continue
    # If is equal to one of the keys
  return total

def assertRoman(actual, expected, description):
  if actual == expected:
    print('Test passed')
  else:
    print('Expected '+str(expected)+' but got '+str(actual)+ ': '+description)

assertRoman(romanToInt("CMXLIX"), 949, "Supposed to return int from roman")
assertRoman(romanToInt("LIX"), 59, "Supposed to return int from roman")
assertRoman(romanToInt("XLI"), 41, "Supposed to return int from roman")

#overflow of lists should probably be taken care of from beginning
#look s[i:i+2]  
#while - full control of the looping variable