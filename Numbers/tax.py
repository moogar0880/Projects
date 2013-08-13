'''
Asks the user to enter a cost and either a country
or state tax. It then returns the tax plus the
total cost with tax.
'''

cost = input('Enter cost: ')
tax  = input('Enter tax %: ')
tax  = float(tax)/100.0
taxVal = cost*tax
total  = cost + taxVal
print "Tax: {}\nTotal: {}".format(taxVal,total)