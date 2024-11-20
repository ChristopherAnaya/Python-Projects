def find(a, b, c, d):
    m1 = (b[1] - a[1])/(b[0] - a[0])
    m2 = (d[1] - c[1])/(d[0] - c[0])
    b1 = a[1] - m1 * a[0]
    b2 = c[1] - m1 * c[0]
    x = (b2 - b1)/(m1 - m2)
    return x
print(find((5,3), (10,4), (5,7.5), (10,7)))
