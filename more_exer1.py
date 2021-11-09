i = 1
while i <= 100:
    if i % 21 == 0:
        print(i, "navgurukul")
    elif i % 3 == 0:
        print(i, "nav")
    elif i % 7 == 0:
        print(i, "guru")
    else:
        print(i)
    i += 1
print(i)
