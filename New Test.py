def to_weird_case(w):
    wl = list(w.lower())
    final = []
    space_test = 0
    for x in wl:
        z = wl.index(x)
        wl[z] = ""
        z -= space_test
        if x == " ":
            final.append(x)
            space_test += 1
        elif z == 0:
            final.append(x.upper())
        elif z % 2 == 0:
            final.append(x.upper())
        else:
            final.append(x)
    finals = "".join(final)
    return finals
    



print(to_weird_case('THIs iS a TEST'))
