'''
Enter a string and the program counts the number of vowels in the text. 
For added complexity have it report a sum of each vowel found.
'''

vowels = ['a','e','i','o','u']

def countVowels(s):
  counts = {}
  for ch in s:
    if ch in vowels and ch in counts:
      counts[ch] += 1
    elif ch in vowels and ch not in counts:
      counts[ch] = 1
    else:
      pass
  print counts

countVowels('aeiou')
countVowels('hzvkd')
countVowels('This is a super long string and I don\'t even know how many vowels are in it!')