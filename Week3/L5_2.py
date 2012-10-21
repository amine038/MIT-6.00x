def recurPower(base, exp):
    # Your code here
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if (exp % 2 == 0):
        #even exponent
        return (recurPower(base * base, (exp/2)))
    else:
        #odd exponent
        return (base * recurPower(base, (exp-1)))
