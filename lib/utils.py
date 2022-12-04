import os

def get_lines(file):
  path, _ = os.path.split(os.path.realpath(file))

  with open(os.path.join(path, "input.txt")) as f:
      lines = [line.rstrip() for line in f]
  
  return lines