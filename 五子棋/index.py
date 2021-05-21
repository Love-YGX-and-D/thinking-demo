#设置棋盘大小
# size=int(input("请输入棋盘的大小（一个整数哦亲）："))
# arr=[]
#创建棋盘
def init():
    for i in range(size):
        arr.append([])
        for j in range(size):
            arr[i].append("口")
#绘制棋盘
def draw():
    for i in arr:
        for j in i:
            print(j,end=" ")
        print("")
# init()
# draw()

import random
# def luo(type="白"):
#     if type=="白":
#         string=input("请输入您要落子的位置：（例如 1，2）")
#         x,y=string.split(",")
#         x=int(x)
#         y=int(y)
#         if isluo(x,y):
#             arr[x][y]=type
#             draw()
#     elif type=="黑":
#         x=random.randint(0,size-1)
#         y=random.randint(0,size-1)
#         if isluo(x,y):
#             arr[x][y]=type
#             draw()
# def isluo(x,y):
#     if x<size and y<size :
#         if arr[x][y]=="口":
#             print("恭喜您，位置正确")
#             return True
#         else:
#             print("该位置已有旗子")
#     else:
#         print("您输入的位置越界啦")
#         return False
# type=input("请输入您的落子颜色:（亲只有黑白两种哦）")
# luo(type)
import random
def luobai():
    string=input("请输入您要落子的位置：（例如 1，2）")
    x,y=string.split(",")
    x=int(x)
    y=int(y)
    if x<size and y<size:
        if arr[x][y]=="口":
            arr[x][y]="白"
            print("警告，白衣军来了")
            draw()
            return True
        else:
            print("该位置已有旗子")
            return False
    else:
        print("索引超界")
        return False
    # draw()
def luohei():
    x=random.randint(0,size-1)
    y=random.randint(0,size-1)
    if arr[x][y]=="口":
        arr[x][y]="黑"
        print("前方高能，黑子来袭")
        draw()
        return True
    else:
        print("该位置已有旗子")
        return False
    
def issucess(type):
    #行
    for i in arr:
        str1=""
        for j in i:
            str1+=j
        if str1.find(type*5)>-1:
            print("%s子棋玩家，恭喜您，您赢了"%type)
            exit()
    #列
    for i in range(size):
        str2=""
        for j in range(size):
            str2+=arr[j][i]
        if str1.find(type*5)>-1:
            print("%s子棋玩家，恭喜您，您赢了"%type)
            exit()
    # \ 
    # for i in range(size):
    #     for j in range(size):
    #         str3+=arr[i][j]
    # num1=list(set(list(range(0,size-4,1))+list(range(0,(size-4)*size,size))))
    # for i in num1:
    #     str4=str3[i:size*5+1:size+1]
    #     if str4.find(type*5)>-1:
    #         print("%s子棋玩家，恭喜您，您赢了"%type)
    #         exit()
    hanglieshu=list(range(0,size-4))
    for i in hanglieshu:
        col=i
        row=0
        str1=""
        while col<size:
            str1+=arr[row][col]
            col+=1
            row+=1
        if str1.find(type*5)>-1:
            print("%s子棋玩家，恭喜您，您赢了"%type)
            exit()
    for i in hanglieshu:
        row=i
        col=0
        str1=""
        while row<size:
            str1+=arr[row][col]
            col+=1
            row+=1
        if str1.find(type*5)>-1:
            print("%s子棋玩家，恭喜您，您赢了"%type)
            exit()
    # /
    hanglieshu1=list(range(4,size-1))
    for i in hanglieshu1:
        col=i
        row=0
        str1=""
        while col>=0:
            str1+=arr[row][col]
            col-=1
            row+=1
        if str1.find(type*5)>-1:
            print("%s子棋玩家，恭喜您，您赢了"%type)
            exit()
    for i in hanglieshu:
        row=i
        col=size-1
        str1=""
        while row<size:
            str1+=arr[row][col]
            col-=1
            row+=1
        if str1.find(type*5)>-1:
            print("%s子棋玩家，恭喜您，您赢了"%type)
            exit()
if __name__ == "__main__":
    size = int(input("请输入棋盘的大小（一个整数哦亲）："))
    arr = []
    init()
    draw()
    while True:
        while True:
            boo=luobai()
            if not boo:
                continue
            # draw()
            issucess(type="白")
            break
        while True:
            boo=luohei()
            if not boo:
                continue
            issucess(type="黑")
            # draw()
            break
