import io, os, time
import sys


class pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def first(self):
        return self.a

    def second(self):
        return self.b


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def get_ints():
    return list(map(int, sys.stdin.readline().strip().split()))


def sol():
    n, m = map(int, input().split())
    # if len(z) == 1:
    #     m = int(input())
    # else:
    #     m = z[1]
    a = [[int(j) for j in input().split()] for i in range(n)]
    d = []

    for i in range(n):
        d.append([10000] * m)

    queue = []
    queue.append(pair(0, 0))
    d[0][0] = a[0][0]
    while len(queue) > 0:
        x = queue[0].first()
        y = queue[0].second()
        queue.pop(0)
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if x1 < 0 or y1 < 0 or x1 >= n or y1 >= m:
                continue
            # print(d[x][y])
            if d[x1][y1] > d[x][y] + a[x1][y1]:
                d[x1][y1] = d[x][y] + a[x1][y1]
                queue.append(pair(x1, y1))

    print(d[n - 1][m - 1])


if __name__ == "__main__":
    # input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

    # start = time.perf_counter()
    test = int(sys.stdin.readline())
    while test > 0:
        test -= 1
        sol()
