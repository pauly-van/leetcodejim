"""
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.
"""

def longestNice(string):
   sameCh = ""
   counter=0
   while counter <= len(string):
     if counter+1 >= len(string):
        break
     if string[counter].lower()==string[counter+1].lower():
        sameCh += string[counter]+string[counter+1]
        counter+=1
     elif string[counter].lower() == string[counter-1].lower() and counter!=0:
         sameCh += string[counter]
     counter+=1
   if findNice(sameCh):
     return sameCh 
   else:
      return ""

def findNice(string):
   niceCount = 0
   for char in range(len(string)):
      if char+1 >= len(string):
         break
      if string[char].islower() and string[char+1].isupper():
         niceCount+=1
      elif string[char].isupper() and string[char+1].islower():
         niceCount+=1
   return len(string) == niceCount+1


  
def assertLongestNice(actual, expected, description):
    if actual == expected:
        print('test passed')
    else:
        print(f'Expected {expected} but got {actual}, {description}')

assertLongestNice(longestNice('YazaAay'), 'aAa', 'Should return the longest nice substring')
assertLongestNice(longestNice('Bb'),'Bb', 'Should return the longest nice substring')
assertLongestNice(longestNice('c'), '', 'Should return the longest nice substring')