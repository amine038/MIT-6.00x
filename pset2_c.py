balance = 999999
annualInterestRate = 0.18

# 13 October 2012
# jaskirat singh
# MIT 6.00x

# code starts here
#init the upper and lower bounds
lowerBound = balance / 12.0
upperBound = (balance * (1 + (annualInterestRate / 12.0)) ** 12) / 12.0

#define epsilon, to the cent (100 cents)
E = 0.01
iters = 0
while(True):
    iters += 1
    newBalance = balance
    monthlyPayout = (lowerBound + upperBound) / 2.0
    for month in range(1, 13):
        newBalance = (newBalance - monthlyPayout) * ( 1 + (annualInterestRate / 12))
    if round(newBalance, 2) < E:
        upperBound = monthlyPayout
    elif round(newBalance, 2) > E:
        lowerBound = monthlyPayout
    else:
        break
print "Lowest Payment:", round(monthlyPayout, 2)
print "iters:", iters

