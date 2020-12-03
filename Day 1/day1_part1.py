def read_input(filename):
    with open(filename) as f:
        return set(map(int, f))

def day1(input):
    for i in L:
        for j in L:
                if i+j == 2020:
                    return i*j


if __name__ == '__main__':
    L = read_input("input.py")
    print(day1(L))


