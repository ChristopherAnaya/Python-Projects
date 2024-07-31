people = int(input("How many people will be in your party"))
print("You will need...")

large = int(people / 7)
large_ex = int(people) % 7
medium = int(large_ex / 3)
medium_ex = int(large_ex) % 3

string1 = ("{} large pizzas")
alt_string1 = ("1 large pizza")
string2 = ("{} medium pizzas")
alt_string2 = ("1 medium pizza")
string3 = ("{} small pizzas")
alt_string3 = ("1 small pizza")

if large == 1:
    print(alt_string1)
else:
    print(string1.format(large))
if medium == 1:
    print(alt_string2)
else:
    print(string2.format(medium))
if medium_ex == 1:
    print(alt_string3)
else:
    print(string3.format(medium_ex))

