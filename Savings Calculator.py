save = float(input("How many dollars do you want to save in a year?"))
print("To save $" + str(save) + " in a year, you will need to save...")
month = save/12
rounded_month = round(month, 2)
print("$" + str(rounded_month) + " a month")
week = save/52.1428571429
rounded_week = round(week, 2)
print("$" + str(rounded_week) + " a week")
day = save/365
rounded_day = round(day, 2)
print("$" + str(rounded_day) + " a day")
