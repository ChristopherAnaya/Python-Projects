def prime_factors(base):
    factors = {}
    d = 2
    while d * d <= base:
        print(d)
        while (base % d) == 0:
            if d not in factors:
                factors[d] = 0
            factors[d] += 1
            base //= d
        d += 1
    if base > 1:
        factors[base] = 1
    return factors


print(prime_factors(8))