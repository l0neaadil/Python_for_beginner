# if...elif ...else
x = float(input("enter a no.: "))
if x == 0:
    print("no. is neither positive nor negative")
elif x < 0:
    print("no. is negative")
else:
    print("no. is positive")
print("Done")



# Nested if_else
x = int(input("enter any integer:  "))
if x == 0:
    print("no. is neither positive nor negative")
elif (x > 0) and x <= 100:
    print("no. is positive but very small")
    if (x % 2) == 0:
        print("even")
    else:
        print("odd")
elif (x < 0) and x >= -100:
    print("no. is negative but very small")
    if (x % 2) == 0:
        print("even")
    else:
        print("odd")
elif 100 < x < 10000 or -10000 < x < -100:
    print("no. contains three or more digits")
    if (x % 2) == 0:
        print("even")
    else:
        print("odd")
else:
    print("only smaller integral values are to be entered")
print("Done")
