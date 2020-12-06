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


if __name__ == '__main__':
    input = read_input("input.py")
    seatIDs = []
    for line in input:
        row, column = decodeSeat(line)
        seatIDs.append(row * 8 + column)
    print(max(seatIDs))
