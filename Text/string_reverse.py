'''
Enter a string and the program will reverse it and print it out.
'''
def reverse(s):
  r = range(0,len(s))
  r.reverse()
  newString = ''
  for i in r:
    newString += s[i]
  print newString