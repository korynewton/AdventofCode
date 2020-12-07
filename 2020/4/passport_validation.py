import re

with open('input.txt') as f:
    data = f.read().split('\n\n')

passports = [d.replace('\n', ' ') for d in data]

passports = [{key: value for word in passport.split() for key, value in [word.split(':')]} for passport in passports]


def val_byr(byr):
    return 1920 <= int(byr) <= 2002


def val_iyr(iyr):
    return 2010 <= int(iyr) <= 2020


def val_eyr(eyr):
    return 2020 <= int(eyr) <= 2030


def val_hgt(hgt):
    if hgt[-2:] not in ['in', 'cm']:
        return False
    if hgt[-2:] == 'in':
        return 59 <= int(hgt[:-2]) <= 76
    elif hgt[-2:] == 'cm':
        return 150 <= int(hgt[:-2]) <= 193


def val_hcl(hcl):
    m = re.search(r'\#[0-9a-f]{6}', hcl)
    return m is not None


def val_ecl(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def val_pid(pid):
    m = re.search(r'^[0-9]{9}$', pid)
    return m is not None


validators = {'byr': val_byr,
              'iyr': val_iyr,
              'eyr': val_eyr,
              'hgt': val_hgt,
              'hcl': val_hcl,
              'ecl': val_ecl,
              'pid': val_pid,}


def validate(p):
    for field, func in validators.items():
        if field not in p.keys() and field != 'cid':
            return 0
        if field != 'cid':
            if not func(p[field]):
                return 0
    return 1


print(sum(validate(p) for p in passports))