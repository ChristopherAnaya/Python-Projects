def pentagonal(n):
    print(n)
    if n <= 0:
        return -1
    center = 1
    sides = (n - 1) * 5 
    midle = sum(x for x in range(1, n-1)) * 5 if n >= 2 else 0
    print(sides, midle)


pentagonal(4) 