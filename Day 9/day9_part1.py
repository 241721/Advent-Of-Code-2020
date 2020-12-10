import itertools
from copy import deepcopy
from itertools import permutations


def read_input(filename):
    file = open('input.py', 'r')
    Lines = file.readlines()
    Lines = [x.strip() for x in Lines]
    return Lines


def is_sum_in_previous_list(previous, checking):
    permuts = permutations(previous, 2)
    valid = False
    for permutation in permuts:
        permutation = [int(c) for c in permutation]
        #print("{}: {}".format(sum(permutation), checking))
        if int(checking) == sum(permutation):
            if not permutation[0] == permutation[1]:
                valid = True
    return valid, checking


if __name__ == '__main__':
    input = read_input("input.py")
    rang = 25
    for start in range(len(input) - rang):
        previous_elements_list = input[start:start+rang]
        checking_element = input[start+rang]
        element = is_sum_in_previous_list(previous_elements_list, checking_element)
        if not element[0]:
            print(element[1])




