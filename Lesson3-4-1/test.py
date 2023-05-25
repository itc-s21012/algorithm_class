LEFT = 0
RIGHT = 1
DATA = 2
node = [
    [1, 2, "Iカレ"],
    [3, 4, "プログラム"],
    [5, None, "就活"],
    [None, None, "java"],
    [6, 7, "python"],
    [None, None, "コミニュケーション"],
    [None, None, "DATA試験"],
    [None, None, "実習アルゴリズム"]
]
MAX = len(node)


def print_tree(node, index):
    if index is None:
        return

    print("ノード{}の値は{}".format(index, node[index][DATA]))
    left_child = node[index][LEFT]
    if left_child is not None:
        print("左の子は" + str(node[left_child][DATA]))
        print_tree(node, left_child)
    else:
        print("左の子は存在しません")

    right_child = node[index][RIGHT]
    if right_child is not None:
        print("右の子は" + str(node[right_child][DATA]))
        print_tree(node, right_child)
    else:
        print("右の子は存在しません")

# ツリーの表示
print_tree(node, 0)