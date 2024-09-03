s = list("`~!@#$%?^&*()-_=+[]{}\\|;:\",./<>")
l = list("qwertyuiopasdfghjklzxcvbnm")
def top_3_words(t):
    c = list(t)
    t = []
    for x in c:
        x = x.lower()
        if x not in l:
            x = " "
        t.append(x)
    t = "".join(t)
    return t
    '''t = t.split()
    z = []
    for x in t:
        x = list(x)
        g = x.copy()
        test = True
        if g != []:
            for r in list(g):
                if r in l:
                    test = False
            if test == False:
                g = "".join(g)
                z.append(g)
    b = dict.fromkeys(z, 0)
    for x in z:
        b[x] += 1
    q = dict(sorted(b.items(), key=lambda item: item[1], reverse = True))
    n = [x for x in q.keys()]
    return n[0:3] if len(n) > 2 else n'''
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
