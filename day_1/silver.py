with open('input.txt') as f:
    lines = [int(line.rstrip()) for line in f]

    increase = 0
    decrease = 0

    for idx, i in enumerate(lines):

        if lines[idx] > lines[idx-1]:
            increase += 1
        if lines[idx] < lines[idx-1]:
            decrease += 1

    print(increase)
    print(decrease)