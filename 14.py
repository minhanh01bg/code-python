def gc(x, num):
    if x == '?':
        return num
    return int(x)


def gop(x, num):
    if (x == '?'):
        if num:
            return '+'
        return '-'
    return x


def solve(n1, n2, n3, op):
    if op[0] == '/' or op[0] == '*':
        print("WRONG PROBLEM!")
        return

    for i in range(1, 10):
        s1 = gc(n1[0], i)
        for j in range(0, 10):
            s2 = s1 * 10 + gc(n1[1], j)
            for m in range(0, 10):
                a1 = gc(n2[0], m)
                for n in range(0, 10):
                    a2 = a1 * 10 + gc(n2[1], n)
                    for x in range(0, 10):
                        b1 = gc(n3[0], x)
                        for y in range(0, 10):
                            b2 = b1 * 10 + gc(n3[1], y)
                            for k in range(0, 10):
                                oprt = gop(op[0], k)
                                if (oprt == '+'):
                                    if (s2 + a2 == b2):
                                        print(str(s2) + " + " +
                                              str(a2) + " = " + str(b2))
                                        return
                                    else:
                                        if (s2 - a2 == b2):
                                            print(str(s2) + " - " +
                                                  str(a2) + " = " + str(b2))
                                            return
                            b2 -= b2
                    a2 -= a2
            s2 -= s2
    print("WRONG PROBLEM!")


for i in range(int(input())):
    n1, op, n2, n3, n4 = map(str, input().split())
    n3 = n4
    solve(n1, n2, n3, op)
