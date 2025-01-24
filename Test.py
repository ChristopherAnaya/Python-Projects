def name(x):
    return "".join([(f"{x}{str(y)} + ") for y in range(1, 6)])
print(name(input("name")))