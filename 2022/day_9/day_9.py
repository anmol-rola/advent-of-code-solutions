from os import path

input = open(f"{path.dirname(__file__)}/input.txt", 'r').read()

tail_visits = []

def move_head(direction, head):
    match direction:
        case 'L':
            head['x'] -= 1
        case 'R':
            head['x'] += 1
        case 'U':
            head['y'] += 1
        case 'D':
            head['y'] -= 1
    return head

def move_tail(head, tail):
    x_diff = head['x'] - tail['x']
    y_diff = head['y'] - tail['y']

    if abs(x_diff) <= 1 and abs(y_diff) <= 1:
        return tail

    if x_diff == 0:
        tail['y'] += int(y_diff/abs(y_diff))
    elif y_diff == 0:
        tail['x'] += int(x_diff/abs(x_diff))
    else:
        tail['y'] += int(y_diff/abs(y_diff))
        tail['x'] += int(x_diff/abs(x_diff))

    tail_visits.append([tail['x'], tail['y']])
    return tail

def get_unique_positions(visits):
    unique = {}
    for visit in visits:
        curr = f"{visit[0]},{visit[1]}"
        unique[curr] = True

    return len(unique.keys())

def move(direction, value, head, tail):
    while value > 0:
        head = move_head(direction, head)
        tail = move_tail(head, tail)
        value -= 1

head = {"x": 0, "y": 0}
tail = {"x": 0, "y": 0}
for curr_move in input.split('\n'):
    curr_move = curr_move.split(' ')
    move(curr_move[0], int(curr_move[1]), head, tail)

print("PART-1", get_unique_positions(tail_visits))

head = {"x": 0, "y": 0}
tail = {"x": 0, "y": 0}
tail_visits = [[0,0]]
for curr_move in input.split('\n'):
    curr_move = curr_move.split(' ')
    move(curr_move[0], int(curr_move[1]), head, tail)

for i in range(1, 9):
    curr_head_visits = tail_visits
    tail_visits = [[0,0]]
    tail = {"x": 0, "y": 0}
    for head_position in curr_head_visits:
        tail = move_tail({"x": head_position[0], "y": head_position[1]}, tail)

print("PART-2", get_unique_positions(tail_visits))