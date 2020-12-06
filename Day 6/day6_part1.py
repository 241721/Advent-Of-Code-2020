def read_input(filename):
    file = open('input.py', 'r')
    Lines = file.readlines()
    Lines = [x.strip() for x in Lines]
    return Lines

def pasre_input_to_groups(input):
    groups = []
    groupAnswers = set()

    for line in input:
        if not (len(line)) == 0:
            for letter in line:
                groupAnswers.add(letter)
        else:
            groups.append(set(groupAnswers))
            groupAnswers.clear()
    groups.append(set(groupAnswers))
    return groups


if __name__ == '__main__':
    input = read_input("input.py")
    groupAnswers = pasre_input_to_groups(input)
    sumOfGroupAnswers = 0

    for group in groupAnswers:
        sumOfGroupAnswers += len(group)

    print(sumOfGroupAnswers)
