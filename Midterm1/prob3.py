def myLog(x, b):
    # computes the logarithm of a number x relative ti a base b
    # ex: if x == 16 and base == 2, then result == 4 as 2^4 == 16
    # ex: if x == 15 and base == 3, then result == 2 as 3^2 is largest power of 3 less then 15

    # myLog should return the largest power of b
    # such that b to that power is LESS THAN OR EQUAL TO x.

    ans = 0
    while True:
        if b ** ans < x:
            ans += 1
            continue
        elif b ** ans == x:
            return ans
        elif b ** ans > x:
            return ans - 1
            
        
