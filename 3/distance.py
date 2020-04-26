


def get_coords(movements):
    '''return list of coords that were traversed'''
    coords = dict()
    x = y = 0

    #Keep track of steps
    steps = 0
    for move in movements:
        d = move[:1]
        dist = int(move[1:])
        x_movement = y_movement = 0

        if d == 'U':
            y_movement = 1
        elif d == 'D':
            y_movement = -1
        elif d == 'L':
            x_movement = -1
        elif d == 'R':
            x_movement = 1


        for i in range(dist):
            x += x_movement
            y += y_movement

            steps += 1

            if (x,y) not in coords:
                coords[(x,y)] = steps 
    return coords

def min_distance(coords):
    '''return the intersection closest to start'''
    min_distance = None 
    for coord in coords:
        [x,y] = coord
        distance = abs(x) + abs(y)
        if not min_distance or distance < min_distance:
            min_distance = distance

    return min_distance


def min_steps(coords1, coords2, itersections):
    '''determine num steps taken to reach intersection by both wires'''
    min = 0
    for coords in intersection:
        wire1_steps = coords1[coords]
        wire2_steps = coords2[coords]
        sum = wire1_steps + wire2_steps
        if not min or sum < min:
            min = sum
    return min


with open("input.txt") as file:
    wire1 = file.readline().strip().split(',')
    wire2 = file.readline().strip().split(',')

    wire1_coords = get_coords(wire1)
    wire2_coords = get_coords(wire2)

    intersection = list(set(wire1_coords.keys() & wire2_coords.keys()))
    print("Closest intersection:", min_distance(intersection))


    min_steps = min_steps(wire1_coords, wire2_coords, intersection)
    print("Min steps: ", min_steps) 

