def sol():
    s = input()
    a = []
    d = 1
    for i in range(len(s)):
        if s[i] == '(':
            a.append(d)
            print(d,end=" ")
            d += 1
        elif s[i] == ')':
            print(a.pop(-1), end=' ')
    print()


if __name__ == "__main__":
    for i in range(int(input())):
        sol()
