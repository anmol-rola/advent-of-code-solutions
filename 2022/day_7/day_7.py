from os import path

input = open(f"{path.dirname(__file__)}/input.txt", 'r').read()

class Directory:
  def __init__(self, name):
    self.name = name
    self.sub_directories = []
    self.size = 0
    self.files = []
  
  def add_subdirectory(self, sub_directory):
    self.sub_directories.append(sub_directory)

  def add_file(self, file):
    self.files.append(file)

class File:
  def __init__(self, name, size):
    self.name = name
    self.size = size

location = Directory('/')
root = location
stack = []
stack.append(location)
result = 0

i = 1
commands = input.split('\n')
while i < len(commands):
  location = stack[-1]
  curr = commands[i].split(' ')
  if curr[0] == '$':
    command = curr[1]
    if command == 'cd':
      arg = curr[2]
      if arg != '..':
        location = [directory for directory in location.sub_directories if directory.name == arg][0]
        stack.append(location)
      else:
        curr_subdir_sizes = sum([dir.size for dir in location.sub_directories])
        curr_file_sizes = sum([file.size for file in location.files])
        location.size += curr_file_sizes + curr_subdir_sizes
        if location.size <= 100000:
          result += location.size
        stack.pop()
  elif curr[0] == 'dir':
    sub_dir = Directory(curr[1])
    location.add_subdirectory(sub_dir)
  else:
    file = File(curr[1], int(curr[0]))
    location.add_file(file)
  
  i += 1


while stack:
  location = stack[-1]
  curr_subdir_sizes = sum([dir.size for dir in location.sub_directories])
  curr_file_sizes = sum([file.size for file in location.files])
  location.size += curr_file_sizes + curr_subdir_sizes
  if location.size <= 100000:
    result += location.size
  stack.pop()

print("PART_1", result)

total_space = 70000000
required_space = 30000000
available_space = total_space - root.size
more_required = required_space - available_space

stack = []
stack.append(root)
minsize = root.size

while stack:
  location = stack[-1]
  if location.size >= more_required and location.size < minsize:
    minsize = location.size
  stack.pop()
  for sub_dir in location.sub_directories:
    stack.append(sub_dir)

print("PART_2", minsize)