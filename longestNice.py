"""
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.
"""

def longestNice(string):
    longestnice = ""
    start = 0 
    stop = len(string)
    while start <= stop:
        if isNice(string[start:stop]):
            longestnice = string[start:stop]
        start+=1
        stop-=1
    return longestnice

def isNice(string):
   if string == "":
       return False
   for nice in string:
     lowerNice = nice.lower()
     upperNice = nice.upper()
     if nice == lowerNice:
       if not nice.upper() in string:
          return False
     elif nice == upperNice:
         if not nice.lower() in string:
            return False
   return True

  
def assertLongestNice(actual, expected, description):
    if actual == expected:
        print('test passed')
    else:
        print(f'Expected {expected} but got {actual}, {description}')

assertLongestNice(longestNice('YazaAay'), 'aAa', 'Should return the longest nice substring')
assertLongestNice(longestNice('Bb'),'Bb', 'Should return the longest nice substring')
assertLongestNice(longestNice('c'), '', 'Should return the longest nice substring')
assertLongestNice(longestNice('abABB'), 'abABB', 'Should return the longest nice substring')




