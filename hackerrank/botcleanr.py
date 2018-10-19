#!/usr/bin/python


def nextMove(posr, posc, board):
    dirt_loc = [row.index('d') if 'd' in row else -1 for row in board]
    dr = next(data[0] for data in enumerate(dirt_loc) if data[1] != -1)
    dc = dirt_loc[dr]
    if(dr > posr):
        print 'DOWN'
    elif(dr < posr):
        print 'UP'
    elif(dc > posc):
        print 'RIGHT'
    elif(dc < posc):
        print 'LEFT'
    else:
        print 'CLEAN'


if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
