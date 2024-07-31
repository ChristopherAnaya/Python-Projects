people = int(input("How many people will be in your party"))

large = int(people / 7)
large_ex = int(people) % 7
medium = int(large_ex / 3)
medium_ex = int(medium) % 3

print("You will need...")
string1 = ("{} large pizzas")
string2 = ("{} medium pizzas")
string3 = ("& {} small pizzas")
print(string1.format(large))
print(string2.format(medium))
print(string3.format(medium_ex))
