draws = []
boards = []
board_scores = []
board_horz_sums = []
board_vert_sums = []
board_diag_sums = []

with open('input.txt', 'r') as file:
    new_board = False
    board_width = 0
    for i, line in enumerate(file.read().splitlines()):
        if i == 0:
            vals = list(map(int, line.split(',')))
            draws = vals
        elif len(line) < 1:
            new_board = True
        elif new_board:
            vals = [int(x) for x in line.split()]
            board_width = len(vals)
            boards.append([vals])
            board_scores.append([[0]*len(vals)])
            board_horz_sums.append([0]*board_width)
            board_vert_sums.append([0]*board_width)
            board_diag_sums.append([0]*2)
            new_board = False
        else:
            vals = [int(x) for x in line.split()]
            b = len(board_scores)-1
            boards[b].append(vals)
            board_scores[b].append([0]*board_width)

    print(f'scanned boards.')
    print(f'board width: {board_width}')
    
    def increment_and_test_win(sums: list, i: int, tag: str) -> bool:
        sums[i]+=1
        if sums[i] == board_width:
            raise AssertionError('Winner: ' + tag)

    try:
        for d in draws:
            for b, board in enumerate(boards):
                for y in range(board_width):        
                    for x in range(board_width):
                        val = board[y][x]
                        if d == val:
                            board_scores[b][y][x] = 1
                            if x==y:
                                increment_and_test_win(board_diag_sums[b], 0, 'diag0')
                            elif x+y==board_width:
                                increment_and_test_win(board_diag_sums[b], 1, 'diag1')
                            increment_and_test_win(board_horz_sums[b], x, 'horiz')
                            increment_and_test_win(board_vert_sums[b], y, 'vert')

    except AssertionError as e:
        board = boards[b]
        scores = board_scores[b]
        sum = 0
        for y in range(board_width):        
            for x in range(board_width):
                if scores[y][x] == 0:
                    sum += board[y][x]
        print(sum * d)

# store drawn numbers in array
# read boards into 2D arrays
# initialize each board's scores in a 2D array
# for each drawn number:
#   # go through each board, marking a score if the number matches
#   for each board b:
#     for each i:
#       for each j:
#         if board number matches drawn number:
#           store i, j score for board b
#           if test board scores for a win ():
#             process board and exit

# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33

# board length == width == B
# diag when x==y || x+y==B

# horiz_sums: [x, x, x]
# vert_sums: [y, y, y]
# diag_sums: [d, d]