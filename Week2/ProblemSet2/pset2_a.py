balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPaid = 0

for month in range(1, 13):
    minimumMonthlyPayment = balance * monthlyPaymentRate
    totalPaid += minimumMonthlyPayment
    balance = (balance - minimumMonthlyPayment)*(1 + (annualInterestRate / 12.0)) 
    print "Month:", month
    print "Minimum monthly payment:", round(minimumMonthlyPayment, 2)
    print "Remaining balance:", round(balance, 2)

print "Total paid:", round(totalPaid, 2)
print "Remaining balance:", round(balance, 2)
