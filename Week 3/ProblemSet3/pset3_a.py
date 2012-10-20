def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
 
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    # FILL IN YOUR CODE HERE...
    value = 0
    for index in range(0, len(poly)):
        value += (poly[index] * (x ** index))
    return float(value)

poly = [0.0, 0.0, 5.0, 9.3, 7.0]    
x = -13 
print evaluatePoly(poly, x) 
