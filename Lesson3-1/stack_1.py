MAX = 5
stack = [0]*MAX
sp = 0 #スタックポインタ

def push(d):
    global sp
    if sp < MAX:
        stack[sp] = d
        sp = sp + 1
        print("データ", d, "を追加しました")
    else:
        print("これ以上データを入れられません")

def pop():
    global sp
    if sp > 0:
        sp = sp - 1
        return stack[sp]
    else:
        print("取り出すデータが存在しません")
        return None

push(1)
push(2)

pop_item = pop()
if pop_item is not None:
    print("データ", pop_item, "を取り出しました")
else:
    print("スタックは空")

push(3)
push(4)
push(5)