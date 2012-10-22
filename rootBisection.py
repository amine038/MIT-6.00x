def rootBisection(num, E):
    upper = num/ 2.0
    lower = 1
    iters = 0
    mid = (lower + upper)/2.0

    while(abs((mid ** 2) - num) > E):
        iters += 1
        if (mid ** 2) > num:
            upper = mid
        elif (mid ** 2) < num:
            lower = mid
        mid = (lower + upper)/2.0
        ##print iters, upper, lower, mid, abs(mid ** 2 - num)
    return mid, iters
