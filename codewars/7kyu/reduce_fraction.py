def reduce_fraction(fraction):
    divisors = []
    bigDivisor = 0

    for i in range(1, ((fraction[0] + 1))):
        if fraction[0] % i == 0:
            divisors.append(i)
    
    divisors.sort(reverse=True)
    for i in divisors:
        if fraction[1] % i == 0:
            bigDivisor = i
            break

    if bigDivisor != 0:
        return (round(fraction[0] / bigDivisor), round(fraction[1] / bigDivisor))
    else:
        return tuple(fraction)
    
print(reduce_fraction([60, 20]))