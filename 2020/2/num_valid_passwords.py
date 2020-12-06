passwords = []
with open('input.txt') as fp:
       for cnt, line in enumerate(fp):
           passwords.append(line.strip('\n'))





def part_1():
    def valid_password(minimum, maximum, letter, password):
        count = 0
        for char in password:
            if char == letter:
                count += 1
        return count >= minimum and count <= maximum
    count = 0
    for password_rules in passwords:
        min_max, letter, password = password_rules.split(" ")

        minimum,maximum = min_max.split('-')
        minimum,maximum = int(minimum), int(maximum)
        letter = letter[0]


        if valid_password(minimum,maximum, letter, password):
            count += 1
    print(count)


def part_2():
    count = 0
    for password_rules in passwords:
        min_max, letter, password = password_rules.split(" ")

        position_1,position_2 = min_max.split('-')
        position_1,position_2 = int(position_1)-1, int(position_2)-1
        letter = letter[0]

        if bool(password[position_1]==letter) != bool(password[position_2]==letter):
            count += 1        
            
    print(count)

