def read_input(filename):
    file = open('input.py', 'r')
    Lines = file.readlines()
    Lines = [x.strip() for x in Lines]
    return Lines


def decodeSeat(seat):
    mydict = {70: 48,
              66: 49,
              76: 48,
              82: 49}
    seat = seat.translate(mydict)
    row = int(seat[:7], 2)
    column = int(seat[-3:], 2)
    return row, column


def fullFlight():
    row = 0
    column = 0
    IDs = []
    for row in range(6, 814):
        IDs.append(row)
    return IDs


def occupiedSeats(input):
    seatIDs = []
    for line in input:
        row, column = decodeSeat(line)
        seatIDs.append(row * 8 + column)
    return seatIDs


def listDiff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif

if __name__ == '__main__':
    input = read_input("input.py")
    diff = listDiff(fullFlight(), occupiedSeats(input))
    print(diff)
