frequency = 0

try:
    datafile = open('input.txt', 'r').readlines()
    print("Open!")

    for line in datafile:
        frequency += int(line)
    print(frequency)
except IOerror:
    print("Error. File not found.")