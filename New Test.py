def expanded_form(n):
    n = list(str(n))
    final = ""
    for x in list(n):
        if x != "0":
            final += (x + "0" * (len(n) - n.index(x) - 1)) + " + "
        n[n.index(x)] = " "
        print(n)
    return final[0:-3]
print(expanded_form(4982342))
