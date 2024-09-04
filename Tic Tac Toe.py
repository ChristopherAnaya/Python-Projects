board = [[False, False, False], [False, False, False], [False, False, False]]
while True:
    try:
        col = int(input("Select A Column 1 - 3"))
        if col > 3 or col < 1:
            test = 2/0
        row = int(input("Select A Row 1 - 3"))
        if row > 3 or row < 1:
            test = 2/0
        break
    except ZeroDivisionError:
        print("--------------------------------------")
        print("     Input Not In Range Try Again     ")
        print("--------------------------------------")
    except TypeError:
        print("--------------------------------------")
        print("Spot On Board Already Filled Try Again")
        print("--------------------------------------")
    except:
        print("--------------------------------------")
        print("     Input Not A Number Try Again     ")
        print("--------------------------------------")
print("""----------------------
|      |      |      |
| _____|      |      |
|
|
|""")
