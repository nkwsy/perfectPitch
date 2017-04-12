import random

doors = ['A', 'B', 'C']
mydoor = random.choice(doors)

monty = doors.pop(mydoor)
print monty