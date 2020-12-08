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

if __name__ == '__main__':
    input = read_input("input.py")
    commands = parse_input(input)
    executed = [False for x in range(len(commands))]

    accumulator = 0
    counter = 0
    while not executed[counter]:
        command = commands[counter][0]
        argument = commands[counter][1]

        executed[counter] = True
        if command == "nop":
            counter += 1
        elif command == "acc":
            accumulator += argument
            counter += 1
        elif command == "jmp":
            counter += argument

    print(accumulator)
