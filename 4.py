class pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def first(self):
        return self.a

    def second(self):
        return self.b


if __name__ == '__main__':

    test = int(input())
    while test > 0:
        test -= 1
        a = []
        n = int(input())
        for i in range(0, n):
            s = [float(i) for i in input().split()]
            a.append(pair(s[0], s[1]))

        f = []
        for i in range(0, n):
            f.append(1)
        for i in range(1, n):
            for j in range(0, i):
                if a[i].first() > a[j].first() and a[i].second() < a[j].second() and f[i] < f[j] + 1:
                    f[i] = f[j] + 1
        print(max(f))
'''
3
2
1.0 1.0
1.5 0.0
3
1.0 1.0
1.0 1.0
1.0 1.0
6
1.5 9.0
2.0 2.0
2.5 6.0
3.0 5.0
4.0 2.0
10.0 5.5
'''
