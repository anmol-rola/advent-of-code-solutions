from os import path

input = open(f"{path.dirname(__file__)}/input.txt", 'r').read()

matrix = []
is_visible = []

for line in input.split('\n'):
  numbers = [int(x) for x in line]
  is_visible_row = [False for x in line]
  matrix.append(numbers)
  is_visible.append(is_visible_row)

n_rows = len(matrix)
n_cols = len(matrix[0])
for i in range(0, n_rows):
  row = matrix[i]
  left_max = row[0]
  right_max = row[n_cols-1]
  for j in range(0, n_cols):
    is_visible[i][j] = True if row[j] > left_max or j == 0 or j == n_cols-1 else is_visible[i][j]
    is_visible[i][n_cols-1-j] = True if row[n_cols-1-j] > right_max or j == 0 or j == n_cols-1 else is_visible[i][n_cols-1-j]
    left_max = max(row[j], left_max)
    right_max = max(row[n_cols-1-j], right_max)

for i in range(0, n_cols):
  top_max = matrix[0][i]
  bottom_max = matrix[n_rows-1][i]
  for j in range(0, n_rows):
    if j == 0 or j == n_rows-1:
      is_visible[j][i] = True
    if matrix[j][i] > top_max:
      is_visible[j][i] = True
    if matrix[n_rows-1-j][i] > bottom_max:
      is_visible[n_rows-1-j][i] = True
    top_max = max(top_max, matrix[j][i])
    bottom_max = max(bottom_max, matrix[n_rows-1-j][i])

count = 0
for x in is_visible:
  for y in x:
    if y: count += 1

print("PART_1", count)

max_view_dist = 0

def traverse(curr, i, j, x_diff, y_diff):
  if i < 0 or j < 0 or i >= n_rows or j >= n_cols:
    return 0
  
  if matrix[i][j] >= curr:
    return 1

  return 1 + traverse(curr, i + x_diff, j + y_diff, x_diff, y_diff)

for i in range(0, n_rows):
  for j in range(0, n_cols):
    curr = matrix[i][j]
    curr_dist = [traverse(curr, i+1, j, 1, 0), traverse(curr, i-1, j, -1, 0), traverse(curr, i, j+1, 0, 1), traverse(curr, i, j-1, 0, -1)]
    
    curr_dist_product = 1
    for dist in curr_dist:
      curr_dist_product *= dist
      
    max_view_dist = max(max_view_dist, curr_dist_product)

print("PART_2", max_view_dist)

