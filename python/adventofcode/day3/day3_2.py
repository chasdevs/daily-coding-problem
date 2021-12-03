
bitindex = 0
bitsums = []
linecount = 0

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
    bitlength = len(lines[0])
    print(lines)

    o2_int = 0
    co2_int = 0
    o2_candidates = lines
    co2_candidates = lines
    finished = 0
    for b in range(bitlength):
        lines_1 = []
        lines_0 = []
        zeroes = 0
        ones = 0
        for line in o2_candidates:
            bits = [int(x) for x in line]
            if bits[b] == 1:
                ones+=1
                lines_1.append(line)
            elif bits[b] == 0:
                zeroes+=1
                lines_0.append(line)
            else:
                raise ValueError('1')
        o2_candidates = lines_0 if zeroes > ones else lines_1

        lines_1 = []
        lines_0 = []
        zeroes = 0
        ones = 0
        for line in co2_candidates:
            bits = [int(x) for x in line]
            if bits[b] == 1:
                ones+=1
                lines_1.append(line)
            elif bits[b] == 0:
                zeroes+=1
                lines_0.append(line)
            else:
                raise ValueError('1')
        co2_candidates = lines_0 if zeroes <= ones else lines_1

        if len(o2_candidates) == 1:
            finished+=1
            o2_int = int(''.join(o2_candidates[0]), 2)
            print(f'o2: {o2_int}')


        if (len(co2_candidates) == 1):
            finished+=1
            co2_int = int(''.join(co2_candidates[0]), 2)
            print(f'co2: {co2_int}')
        
        if finished == 2:
            print(co2_int * o2_int)





# [a, b, c, d, ...] N

# 1 - [a, b, ..] Nc

# 0 - [c, d, ..] Nu

# for each bit index (b)
#    find the most common value
#    keep all of the lines which start with that index
#      if there is only one line, that is reading