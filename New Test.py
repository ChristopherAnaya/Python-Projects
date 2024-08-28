def base_convert_to_10(b, n):
    y = 0
    z =1
    for x in list(str(n)[len(str(n))::-1]):
        y += int(x) * z
        z *= b
    return y
def is_prime(n):
    if n < 2 :
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True
def is_valid(b, n):
    h = True
    end = len(str(n))
    while end >0:
        g = base_convert_to_10(b, n)
        h = is_prime(g)
        n = list(str(n))
        del n[-1]
        n = "".join(n)
        end -= 1
        if h == False:
            end = 0
    return h
def get_right_truncatable_primes(base):
    test_cases = [x for x in range(1, base)]
    final = []
    clone = []
    clone = test_cases.copy()
    stop = False
    end = True
    tests = 3
    times = 0
    while stop == False:
        for x in clone:
            z = is_valid(base, x)

            if z == True:
                end = False
                final.append(x)

        if end == True:
            stop = True
        end = True
        leg = len(final)
        
        clone = []
        hold = 0
        times += 1

        for x in final:
            z = final.copy()
            c = z.pop(hold)
            if c in z:
                del final[z.index(c) + 1]
            hold += 1
        if times > 1:
            for y in final[length:leg]:
                y = str(y)
                y = y[1:(len(str(y)))]
                for x in final[0:length]:
                    x = str(x)
                    if x == y:
                        del final[final.index(int(x))]

        if times > 1:
            for y in final[length:leg]:
                y = str(y)
                y = y[0:(len(str(y)))-1]
                for x in final[0:length]:
                    x = str(x)
                    if x == y:
                        del final[final.index(int(x))]
                        
        length = len(final)
        print("hello")
        

        for x in final:
            for y in test_cases:
                z = str(y) + str(x)
                z = int(z)
                clone.append(z)

    print(final)
    for x in final:
        z = final.index(x)
        x = base_convert_to_10(base, x)
        final[z] = x
    return final
print(get_right_truncatable_primes(6))

