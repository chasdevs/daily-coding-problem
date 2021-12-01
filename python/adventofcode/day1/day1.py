from collections import deque
import sys

with open('input.txt', 'r') as file:
    sound = file.read().splitlines()

inc = 0
dec = 0
last = 0
window = deque([0, 0, 0])
for i, depth in enumerate(sound):
    depth = int(depth)
    window.append(depth)
    window.popleft()

    if i < 2:
        print(f'............ - {i} {depth} {list(window)}')
        continue

    depth_sum = sum(window)
    if i == 2:
        print(f'{depth_sum} nothing  - {i} {depth} {list(window)}')
    elif depth_sum > last:
        inc+=1
        print(f'{depth_sum} increase - {i} {depth} {list(window)}')
    elif depth_sum < last:
        dec+=1
        print(f'{depth_sum} decrease - {i} {depth} {list(window)}')
    else:
        print(f'{depth_sum} nochange - {i} {depth} {list(window)}')


    last = depth_sum

print(inc)
