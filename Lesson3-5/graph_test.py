data = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]

node = ["那覇", "糸満", "沖縄", "宜野湾", "名護"]
arrow = ["", "->", "<-", "<->"]

for y in range(5):
    for x in range(y, 5):
        e1 = data[y][x]
        e2 = data[x][y]
        a = e1 + e2*2
        if a > 0:
            print(node[y]+arrow[a]+node[x])

