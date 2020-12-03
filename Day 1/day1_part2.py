def read_input(filename):
    with open(filename) as f:
        return set(map(int, f))

def day1(input):
    for i in L:
        for j in L:
            for l in L:
                if i+j+l == 2020:
                    return i*j*l


if __name__ == '__main__':
    L = read_input("input.py")
    print(day1(L))

