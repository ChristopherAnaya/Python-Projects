def fact(n):
    total = 1
    while n >0:
        total *= n
        n -=1
    return total
number = int(input("Choose a number."))
new = 0
for i in range(1,number + 1):
    new += fact(i)
print(new)
