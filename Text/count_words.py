'''
Counts the number of individual words in a string. For added complexity 
read these strings in from a text file and generate a summary.
'''
def words(s):
  return len(s.split(' '))

print words('three words in')