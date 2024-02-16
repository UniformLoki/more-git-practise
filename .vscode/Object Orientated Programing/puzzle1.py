def number_checker():
    count = 0
    i = 0
    while i <= 1000000:
        j = str(i)
        number = [*j]
        for y in number:
            r = int(y)
            if r == 0:
                count += 1
        number.clear()
        i += 1
    print (count)


number_checker()
print("done")