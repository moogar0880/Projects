'''
Checks if the string entered by the user is a palindrome. That is that it reads the same 
forwards as backwards
'''
def palindrome(s):
  def reverse(s):
    r = range(0,len(s))
    r.reverse()
    newString = ''
    for i in r:
      newString += s[i]
    return newString
  return s == reverse(s)