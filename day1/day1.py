# https://adventofcode.com/2021/day/1
# Count the number of times a depth measurement increases from the previous measurement
# How many measurements are larger than the previous measurement
input = []
increased = 0

with open('input') as f:
  input = [int(line) for line in f]

#print(input)

for i, j in zip(input, input[1:]):
  if (j > i):
    increased += 1
  print (i,j)

print("total:",increased)
