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

def romanToInt(s):
  #create a table to define each roman number to a value 
  table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
  # Break input into list [X, I, V]
  input = list(s) #[X, I, V]
  #loop thru table to find value
  total = 0
  keys = list(table.keys()) #an array of keys ['I', 'V', 'X', 'L', 'C', 'D', 'M']
  for r in range(len(input)): 
    # another loop that goes thru keys
    for n in range(len(keys)):
      if input[r] == keys[n]:
    # If is equal to one of the keys
        total = total + table[input[r]] 
        continue
  return total

def assertRoman(actual, expected, description):
  if actual == expected:
    print('Test passed')
  else:
    print('Expected '+str(expected)+'but got '+str(actual)+ ': '+description)

assertRoman(romanToInt("CMXLIX"), 949, "Supposed to return int from roman")
assertRoman(romanToInt("LIX"), 59, "Supposed to return int from roman")
assertRoman(romanToInt("XLI"), 41, "Supposed to return int from roman")
