def read_input(filename):
    file = open('input.py', 'r')
    Lines = file.readlines()
    Lines = [x.strip() for x in Lines]
    return Lines


def is_passport_valid(passport):
    obligatory_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for key in obligatory_keys:
        if key not in passport:
            return False
    return True


def pasre_input_to_passports(input):
    passports = []
    passport = {}

    for line in input:
        if not (len(line)) == 0:
            elements = line.split(" ")
            for element in elements:
                element = element.split(":")
                passport.update({element[0]: element[1]})
        else:
            passports.append(dict(passport))
            passport.clear()
    passports.append(dict(passport))
    return passports


if __name__ == '__main__':
    input = read_input("input.py")
    passports = pasre_input_to_passports(input)

    valid_passports = 0
    for passport in passports:
        if is_passport_valid(passport):
            valid_passports += 1

    print(valid_passports)