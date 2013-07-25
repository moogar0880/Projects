'''
Pig Latin is a game of alterations played on the English language game. To create the Pig Latin 
form of an English word the initial consonant sound is transposed to the end of the word and an 
ay is affixed (Ex.: "banana" would yield anana-bay).
'''

vowels = ['a','e','i','o','u']
suffix = 'ay'

def toLatin(s):
  if s[0] in vowels:
    return s + suffix
  else:
    return s[1:] + s[0] + suffix

print toLatin('banana')