p = [True] * 100 #要素数１００の配列を用意し、全てにTrueを代入
p[0] = False    #0は素数ではないのでFalseを代入
p[1] = False
n = 2

def hyou():
    s = ""
    for i in range(100):
        if p [i] == True:
            s += "{:2d}, ".format(i)
        else:
            s += "/, "
        if i%10 == 9:
            s += "\n"
    print(s)

def furui ():
    global n
    for i in range(n+n, 100, n):
        p[i] = False
        print(n, "の倍数をふるい落としました")
        hyou()
        while n<100: # 次に篩い落とす数
            n = n + 1
            if p[n] == True:
                break

hyou()
while n<10: # √99まで行う
    input("Enterキーを押してください")
    furui()