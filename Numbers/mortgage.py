'''
Calculate the monthly payments of a fixed
term mortgage over given Nth terms at a given
interest rate. Also, figure out how long it
will take the user to pay back the loan.
'''
import math
principle = input('Loan amount: ')
length    = input('Length of mortgage (years): ')
interest  = input('Interest rate percentage (ie 7 = 7%): ')

interest = float(interest)/100.0

monthlyRate = interest/12.0
numPayments = length*12
term = math.pow(1+monthlyRate, numPayments)
monthly_payment = principle * (monthlyRate * (term/(term - 1)))

print "It will take {} months to pay back the ${} loan, at a rate of ${}/month".format(principle/monthly_payment,principle,monthly_payment)