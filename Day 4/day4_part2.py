def read_input(filename):
    file = open('input.py', 'r')
    Lines = file.readlines()
    Lines = [x.strip() for x in Lines]
    return Lines


class Key:
    def __init__(self, name):
        self.name = name

    def validate(self, value):
        pass


class Byr(Key):
    def __init__(self):
        super().__init__("byr")

    def validate(self, value):
        if len(value) == 4 and 1920 <= int(value) <= 2002:
            return True
        else:
            return False


class Iyr(Key):
    def __init__(self):
        super().__init__("iyr")

    def validate(self, value):
        if len(value) == 4 and 2010 <= int(value) <= 2020:
            return True
        else:
            return False


class Eyr(Key):
    def __init__(self):
        super().__init__("eyr")

    def validate(self, value):
        if len(value) == 4 and 2020 <= int(value) <= 2030:
            return True
        else:
            return False


class Hgt(Key):
    def __init__(self):
        super().__init__("hgt")

    def validate(self, value):
        if value[-2:] == "cm":
            if 150 <= int(value[:-2]) <= 193:
                return True
        elif value[-2:] == "in":
            if 59 <= int(value[:-2]) <= 76:
                return True
        else:
            return False


class Hcl(Key):
    def __init__(self):
        super().__init__("hcl")

    def validate(self, value):
        return False


class Ecl(Key):
    def __init__(self):
        super().__init__("ecl")

    def validate(self, value):
        colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return value in colors


class Pid(Key):
    def __init__(self):
        super().__init__("pid")

    def validate(self, value):
        if not type(value) == int:
            return False
        return False


def is_passport_valid(passport):
    obligatory_keys = [Byr(), Iyr(), Eyr(), Hgt(), Hcl(), Ecl(), Pid()]
    for key in obligatory_keys:
        if key.name not in passport or not key.validate(passport.get(key.name)):
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
