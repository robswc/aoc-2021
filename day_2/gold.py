with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

    instruction_lines = [l.split(' ') for l in lines]
    print(instruction_lines)

    x = 0
    y = 0
    aim = 0

    for instruction in instruction_lines:
        if instruction[0] == 'forward':
            x += int(instruction[1])
            y += aim * int(instruction[1])
        if instruction[0] == 'up':
            aim -= int(instruction[1])
        if instruction[0] == 'down':
            aim += int(instruction[1])

        print(x, y)

    print(x * y)