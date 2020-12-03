file = open('input.py', 'r')
Lines = file.readlines()
Lines = [x.strip() for x in Lines]
counter = 0

for line in Lines:
    split = line.split(sep=" ")
    interval = split[0].split(sep="-")
    sign = split[1][0]
    password = split[2]

    lowerInterval = int(interval[0])
    upperinterval = int(interval[1])

    counts = password.count(sign)
    if counts >= lowerInterval and counts <= upperinterval:
        counter += 1

print(counter)
