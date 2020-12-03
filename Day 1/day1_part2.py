from itertools import combinations

def read_input(filename):
    with open(filename) as f:
        return set(map(int, f))

def day1(input):
    L = list(combinations(input, 3))
    for l in L:
        if sum(l) == 2020:
            return l[0] * l[1] * l[2]

if __name__ == '__main__':
    L = read_input("input.py")
    print(day1(L))


