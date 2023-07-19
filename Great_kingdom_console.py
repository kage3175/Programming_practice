# 실제 플레이에 사용되는 보드는 9x9
# 1은 흑돌, 2는 백돌, 3은 중립돌

SIZE = 9
THECROSS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
BLANK = 0
BLACK = 1
WHITE = 2
NEUTRAL = 3

clusters_black = []
clusters_white = []
clusters_neutral = []
clusters_black_house = []
clusters_white_house = []
clusters_blank = []

def print_board(board, start, end):
    for i in range(start, end):
        for j in range(start, end):
            print(board[i][j], end = " ")
        print()

def count_house(board, start, end):
    house_black = 0
    house_white = 0
    flag = True
    for i in range(start, end):
        for j in range(start, end):
            if(board[i][j]==BLANK):
                #check if black house
                for k in range(4):
                    x, y = i+THECROSS[k][0], j+THECROSS[k][1]
                    if(board[x][y] != NEUTRAL and board[x][y] != BLACK):
                        flag = False
                        break
                if flag:
                    house_black+=1
                # check if white house
                for k in range(4):
                    x, y = i+THECROSS[k][0], j+THECROSS[k][1]
                    if(board[x][y] != NEUTRAL and board[x][y] != BLACK):
                        flag = False
                        break
                if flag:
                    house_white+=1
    return house_black, house_white


board = [[0 for i in range(SIZE+2)] for j in range(SIZE+2)]
board[int(SIZE/2)+1][int(SIZE/2)+1] = 3
for i in range(SIZE+2):
    board[0][i]=3
    board[SIZE+1][i]=3
    board[i][0]=3
    board[i][SIZE+1]=3

turn = 1

while 1:
    print("\n다음 수를 둘 좌표를 x y 형태로 입력해주세요: ", end = " ")
    x,y=map(int, input().split())
    board[x][y] = turn
    if turn == 1:
        turn = 2
    else:
        turn = 1
    house_black, house_white = count_house(board, 1, SIZE+1)
    print_board(board, 1, SIZE+1)
    print(f'흑: {house_black}집  백: {house_white}집')