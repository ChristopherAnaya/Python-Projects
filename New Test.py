def base_convert_to_10(b, n):
    y = 0
    z =1
    for x in list(str(n)[len(str(n))::-1]):
        y += int(x) * z
        z *= b
    return y
def is_prime(n):
    if n % 2 ==0 and n > 2:
        return False
    else:
        return True
def is_valid(t, q):
    h = True
    end = len(str(t))
    while end >0:
        g = base_convert_to_10(q, t)
        h = is_prime(g)
        t = list(str(t))
        del t[-1]
        t = "".join(t)
        end -= 1
        if h == False:
            end = 0
    return h
def get_right_truncatable_primes(base):
    works = True
    test = False
    hold = []
    test_case = []
    helpme = 2
    for x in range(1, base):
        test_case.append(x)
    while works == True:
        for x in test_case:
            l = x
            x = is_valid(x, base)
            if x == False:
                test = True
                hold.append(l)
        if test == False:
            works = False
        test = False
        copy = test_case.copy()
        print("hello")
        for x in hold:
            for y in range(len(copy)):
                print(copy)
                print(y)
                print(str(test_case[y-1]))
                print(test_case)
                z = str(test_case[y-1]) + str(x)
                print(z)
                test_case.append(int(z))
                print("------------")
            print("h")
        del test_case[0:len(copy)]
        print(test_case)
        helpme -= 1
        if helpme == 0:
            break
    print(hold)
    return test_case

print(get_right_truncatable_primes(6))






















def base_covert_from_10(b, n):
    x = ""
    while n >= b:
        x += str(n % b)
        n -= int(n % b)
        n = int(n/b)
    if n != 0:
        x += str(n)
    return x[len(x)::-1]
