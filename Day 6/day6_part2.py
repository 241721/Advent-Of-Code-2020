def read_input(filename):
    file = open('input.py', 'r')
    Lines = file.readlines()
    Lines = [x.strip() for x in Lines]
    return Lines

def pasre_input_to_groups(input):
    groups = []
    group = set()
    person = set()
    sw = True
    for line in input:
        if len(line) == 0:
            groups.append(set(group))
            group.clear()
            sw = True
        else:
            if sw:
                for l in line:
                    group.add(l)
                sw = False
            else:
                for l in line:
                    person.add(l)
                group = group.intersection(person)
                person.clear()
    groups.append(group)
    return groups



if __name__ == '__main__':
    input = read_input("input.py")
    groups = pasre_input_to_groups(input)
    sumOfYesAnswers = 0
    for group in groups:
        sumOfYesAnswers += len(group)
    print(sumOfYesAnswers)