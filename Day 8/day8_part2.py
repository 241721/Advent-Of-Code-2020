from copy import deepcopy
def read_input(filename):
    file = open('input.py', 'r')
    Lines = file.readlines()
    Lines = [x.strip() for x in Lines]
    return Lines


def parse_input(input):
    for i in range(len(input)):
        input[i] = input[i].split(" ")
        input[i][1] = int(input[i][1])
    return input


def execute_code_and_validate(commands):
    executed = [False for x in range(len(commands))]

    accumulator = 0
    counter = 0
    while not executed[counter]:
        command = commands[counter][0]
        argument = commands[counter][1]
        if counter == len(commands)-1:
            if command == "nop":
                return True, accumulator
            elif command == "acc":
                return True, accumulator + argument
            elif argument > 0:
                return True, accumulator

        executed[counter] = True

        if command == "nop":
            counter += 1
        elif command == "acc":
            accumulator += argument
            counter += 1
        elif command == "jmp":
            counter += argument
    return False, accumulator


def modify_command_and_check(commands, index):
    if commands[index][0] == "nop":
        commands[index][0] = "jmp"
    elif commands[index][0] == "jmp":
        commands[index][0] = "nop"
    return execute_code_and_validate(deepcopy(commands))


if __name__ == '__main__':
    input = read_input("input.py")
    commands = parse_input(input)
    for i in range(len(commands)):
        result = modify_command_and_check(deepcopy(commands), i)
        if result[0]:
            print(result[1])



