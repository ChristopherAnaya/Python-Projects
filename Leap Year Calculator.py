year = input("What year would you like to check")
leap = int(year) % 4
reverse = year[len(year)::-1]
check = reverse[0:2]
century = int(year) % 400
if check == "00":
    if century == 0:
        print(year + " is a leap year")
    else:
        print(year +  " is not a leap year")
