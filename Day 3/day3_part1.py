file = open('input.py', 'r')
Lines = file.readlines()
Lines = [x.strip() for x in Lines]


def move(right, down):
    j = 0
    i = 0
    counter = 0
    for x in Lines:
        i += down
        if i >= len(Lines):
            break
        j += right
        if Lines[i][j % len(Lines[i])] == "#":
            counter += 1

    return counter


print(move(3, 1))
