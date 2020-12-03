file = open('input.py', 'r')
Lines = file.readlines()
Lines = [x.strip() for x in Lines]
counter = 0

for line in Lines:
    split = line.split(sep=" ")
    interval = split[0].split(sep="-")
    lowerInterval = split[2][int(interval[0])-1] == split[1][0]
    upperInterval = split[2][int(interval[1])-1] == split[1][0]
    if bool(lowerInterval) != bool(upperInterval):
        counter += 1

print(counter)

