terrain = []
with open('input.txt') as fp:
       for cnt, line in enumerate(fp):
           terrain.append(line.strip('\n'))


def part_1(num_over):
    x, count = 0, 0
    for (i, row) in enumerate(terrain):
        if i == 0:
            continue
        x = (x + num_over) % len(row)
        if row[x] == '#':
            count += 1
    print(count)

def part_2(num_over, num_down):
    cur_x, count = 0, 0
    for i in range(0,len(terrain),num_down):
        if i == 0:
            continue
        cur_x = (cur_x + num_over) % len(terrain[cur_x])
        print(i, cur_x)
        if terrain[i][cur_x] == '#':
            count += 1
    return count


print(part_2(1,1) * part_2(3,1) * part_2(5,1) * part_2(7,1) * part_2(1,2))
