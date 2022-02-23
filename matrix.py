ind = []


class pair:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def first(self):
        return self.a

    def second(self):
        return self.b


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def check(x, y):
    if x < 0 or y < 0 or x >= 5 or y >= 5:
        return False
    return True


def bfs():
    map = []
    for i in range(5):
        map.append([0]*5)

    queue = []
    if ind[0] == 2 and ind[1] == 2:
        print(0)
        return
    queue.append(pair(ind[0], ind[1]))
    while len(queue) > 0:
        x = queue[0].first()
        y = queue[0].second()
        queue.pop(0)
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if check(x1, y1) == False:
                continue
            if x1 == 2 and y1 == 2:
                print(map[x][y] + 1)
                return
            map[x1][y1] = map[x][y] + 1
            queue.append(pair(x1, y1))


if __name__ == '__main__':
    a = [[int(j) for j in input().split()] for i in range(5)]
    for i in range(5):
        for j in range(5):
            if a[i][j] == 1:
                ind.append(i)
                ind.append(j)
    bfs()
