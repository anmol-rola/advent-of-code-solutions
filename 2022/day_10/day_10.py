from os import path

input = open(f"{path.dirname(__file__)}/input.txt", 'r').read()

target_cycles = [20, 60, 100, 140, 180, 220]

cycle = 0
value = 1
target_cycle_index = 0
max_index = 5
result = 0

for line in input.split('\n'):
  command = line.split(' ')[0]
  cycle += 1 if command == "noop" else 2
  value_to_add = 0 if command == "noop" else int(line.split(' ')[1]) 

  if target_cycle_index <= max_index and target_cycles[target_cycle_index] <= cycle:
    result += target_cycles[target_cycle_index] * value
    target_cycle_index += 1
  
  value += value_to_add
  
print("PART-1", result)

display = []
for _ in range(0, 6):
  display.append(['.' for _ in range(0, 40)])

commands = [line.split(' ') for line in input.split('\n')]
cycle = 0
sprite_center = 1

def draw(sprite_center, cycle):
  currently_drawing = cycle % 240
  if sprite_center >= currently_drawing % 40 - 1 and sprite_center <= currently_drawing % 40 + 1:
    display[int(currently_drawing/40)][currently_drawing % 40] = '#'

for command in commands:
  if command[0] == 'noop':
    draw(sprite_center, cycle)
    cycle += 1
  else:
    draw(sprite_center, cycle)
    cycle += 1
    draw(sprite_center, cycle)
    cycle += 1
    sprite_center += int(command[1])

print("PART-2")
for d in display:
  print("".join(d))