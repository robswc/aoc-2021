import math

with open('input.txt') as f:
    lines = [int(line.rstrip()) for line in f]

    increase = 0

    windows = [sum(lines[idx:idx+3]) for idx, i in enumerate(lines[:-2])]

    for idx, i in enumerate(windows):

        if windows[idx] > windows[idx-1]:
            increase += 1


    print(increase)
