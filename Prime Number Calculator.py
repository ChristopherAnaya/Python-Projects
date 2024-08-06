number = int(input("Input a whole number."))
list = []
check = 0
if number > 2:
    for x in range(2,number):
        if number%x == 0:
            list.append(x)
            check += 1
if number < 3:
    print("Invalid number")
elif check == 0:
    print(str(number) + " is a prime number!")
else:
    print(list)





