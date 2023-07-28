# 실제 플레이에 사용되는 보드는 9x9
# 1은 흑돌, 2는 백돌, 3은 중립돌

SIZE = 9
THECROSS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
BLANK = 0
BLACK = 1
WHITE = 2
NEUTRAL = 3

class cluster:
    def __init__(self):
        self.size = 0
        self.lst_cluster = []

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

def make_cluster(board, mark, start, end):
    global clusters_black
    global clusters_black_house
    global clusters_white
    global clusters_white_house
    global clusters_neutral
    global clusters_blank
    clusters_black = []
    clusters_black_house = []
    clusters_white = []
    clusters_white_house = []
    clusters_blank = []
    clusters_neutral = []
    for i in range(start, end):
        for j in range(start, end):
            if mark[i][j]:
                temp = []
                queue = []
                queue.append((i,j))
                mark[i][j] = False
                if board[i][j] == 0:#blank에 일단 넣는다.
                    while queue:
                        (x, y) = queue.pop()
                        temp.append((x,y))
                        for k in range(4):
                            newx, newy = x+THECROSS[k][0], y+THECROSS[k][1]
                            if board[newx][newy] == 0 and mark[newx][newy]:
                                queue.append((newx, newy))
                                mark[newx][newy] = False
                    clusters_blank.append(temp)
                elif board[i][j] == 1:
                    while queue:
                        (x, y) = queue.pop()
                        temp.append((x,y))
                        for k in range(4):
                            newx, newy = x+THECROSS[k][0], y+THECROSS[k][1]
                            if board[newx][newy] == 1 and mark[newx][newy]:
                                queue.append((newx, newy))
                                mark[newx][newy] = False
                    clusters_black.append(temp)
                elif board[i][j] == 2:
                    while queue:
                        (x, y) = queue.pop()
                        temp.append((x,y))
                        for k in range(4):
                            newx, newy = x+THECROSS[k][0], y+THECROSS[k][1]
                            if board[newx][newy] == 2 and mark[newx][newy]:
                                queue.append((newx, newy))
                                mark[newx][newy] = False
                    clusters_white.append(temp)
    flag = True
    for cluster in clusters_blank: ### check if black house
        flag = True
        for (x, y) in cluster:
            if board[x][y] == 2:
                flag = False
                break
        if flag:
            clusters_black_house.append(cluster)
            clusters_blank.remove(cluster)
    for cluster in clusters_blank: ### check if black house
        flag = True
        for (x, y) in cluster:
            if board[x][y] == 1:
                flag = False
                break
        if flag:
            clusters_white_house.append(cluster)
            clusters_blank.remove(cluster)
    for i in range(start, end):
        for j in range(start, end):
            mark[i][j] = True



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

def main():

    board = [[0 for i in range(SIZE+2)] for j in range(SIZE+2)]
    mark_cluster = [[True for i in range(SIZE+3)] for j in range(SIZE+2)]

    board[int(SIZE/2)+1][int(SIZE/2)+1] = 3
    for i in range(SIZE+2):
        board[0][i]=3
        board[SIZE+1][i]=3
        board[i][0]=3
        board[i][SIZE+1]=3

    turn = 1
    cnt_total_turn = 0
    trigger_wrong_input = False

    while 1:
        cnt_total_turn += 1
        print("\n다음 수를 둘 좌표를 x y 형태로 입력해주세요(-1 -1 입력시 계가): ", end = " ")
        x,y=map(int, input().split())
        if x == -1 and y == -1 and cnt_total_turn > 1:
            house_black = 0
            house_white = 0
            for cluster in clusters_black_house:
                for house in cluster:
                    house_black+=1
            for cluster in clusters_white_house:
                for house in cluster:
                    house_white+=1
            print(f'흑 집: {house_black}  백 집: {house_white}')
        else:
            if (x < 1 or x > 9) and (y < 1 or y > 9):
                continue
            board[x][y] = turn
            if turn == 1:
                turn = 2
            else:
                turn = 1
            make_cluster(board, mark_cluster, 1, SIZE+1)
            #house_black, house_white = count_house(board, 1, SIZE+1)
            print_board(board, 1, SIZE+1)
            #print(f'흑: {house_black}집  백: {house_white}집')
            print(clusters_blank, clusters_black, clusters_white, clusters_black_house, clusters_white_house)

main()