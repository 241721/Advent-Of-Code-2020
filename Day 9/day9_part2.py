import itertools
from copy import deepcopy
from itertools import permutations
import threading

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


def thread(input, answer, rang):
    for start in range(len(input) - rang):
        previous_elements_list = input[start:start + rang + 1]
        previous_elements_list = [int(x) for x in previous_elements_list]
        if int(answer) == int(sum(previous_elements_list)):
            print(min(previous_elements_list) + max(previous_elements_list))
            return min(previous_elements_list) + max(previous_elements_list)


def search_for_encryption_weakness(input, answer):
    rang = len(input)
    threads = list()

    while rang >= 2:
        x = threading.Thread(target=thread, args=(input, answer, rang))
        threads.append(x)
        x.start()

        rang -= 1


if __name__ == '__main__':
    input = read_input("input.py")
    rang = 25

    for start in range(len(input) - rang):
        previous_elements_list = input[start:start + rang]
        checking_element = input[start + rang]
        element = is_sum_in_previous_list(previous_elements_list, checking_element)
        if not element[0]:
            answer = element[1]
            search_for_encryption_weakness(input, answer)
