balance = 4000
annualInterestRate  = 0.2
minimumMonthlyPayment = 10
numIter = 0
while(True):
    numIter += 1
    newBalance = balance
    for month in range(1, 13):
        newBalance = (newBalance - minimumMonthlyPayment) * ( 1 + (annualInterestRate / 12))
    if newBalance <= 0:
        break
    else:
        minimumMonthlyPayment += 10
print "Lowest Payment:", minimumMonthlyPayment
