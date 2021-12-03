
gamma = 0
epsilon = 0
bitlength = 0
bitsums = []
linecount = 0

def calc_gamma(ones: int, total: int):
    zeroes = total - ones
    if ones > zeroes:
        return 1
    elif ones < zeroes:
        return 0
    else:
        raise ValueError('Ones and zeroes equal... what to do?')

def calc_epsilon(ones: int, total: int):
    zeroes = total - ones
    if ones > zeroes:
        return 0
    elif ones < zeroes:
        return 1
    else:
        raise ValueError('Ones and zeroes equal... what to do?')

with open('input.txt', 'r') as file:
    for i, line in enumerate(file.read().splitlines()):
        linecount+=1
        bits = [int(b) for b in line]
        if i == 0:
            bitlength = len(bits)
            bitsums = [0] * bitlength
        elif bitlength != len(bits):
            raise ValueError(f'Bitlength of index {i} does not match initial bitlength')

        for b in range(bitlength):
            bitsums[b] += bits[b]

        print(f'{i} {line} {bitsums} {linecount}')
    
    gamma = [str(calc_gamma(s, linecount)) for s in bitsums]
    epsilon = [str(calc_epsilon(s, linecount)) for s in bitsums]

    gamma_int = int(''.join(gamma), 2)
    epsilon_int = int(''.join(epsilon), 2)

    print(gamma_int)
    print(epsilon_int)
    print(gamma_int * epsilon_int)
