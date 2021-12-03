
horizontal = 0
aim = 0
depth = 0

with open('input.txt', 'r') as file:
    for line in file.read().splitlines():
        print(line)

        [cmd, val] = line.split()
        val = int(val)
        
        if 'forward' == cmd:
            horizontal += val
            depth += aim*val
        elif 'up' == cmd:
            aim -= val
        elif 'down' == cmd:
            aim += val
        else:
            raise ValueError('Unknown cmd: ' + cmd)
        
    mult = depth * horizontal

    print(horizontal)
    print(aim)
    print(depth)
    print(mult)