import math

while 1:
    print("비행기 기종을 입력해주세요(-1 입력시 프로그램 종료): ", end='')
    x=input()
    if x=='A300':
        while 1:
            dist=int(input())
            if dist==-1:
                break
            print(round(-9.452*math.log(dist)+89.688))
    elif x=='B737':
        while 1:
            dist=int(input())
            if dist==-1:
                break
            print(round(0.000002*dist*dist-0.014*dist+36.421))
    elif x=='-1':
        break
    else:
        print("다시 입력해주세요.\n")



    