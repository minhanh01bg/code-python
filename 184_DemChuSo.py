def Count0(n):
    res = 1
    i = 1
    b = 0
    c = 0
    a = 0
    while True:
        b = n // i
        c = n % i
        a = b // 10
        b = b % 10
        if a == 0:
            return res
        if b == 0:
            res = res + (a - 1) * i + c + 1
        else:
            res = res + a * i
        i *= 10
        # if i >= 10000000:
            # break

def Count(number, d, k):
    powerOf10 = 10**d
    nextPowerOf10 = powerOf10 * 10
    right = number % powerOf10

    roundDown = number - number % nextPowerOf10
    roundup = roundDown + nextPowerOf10

    digit = (number // powerOf10) % 10

    if (digit < k):
        return roundDown // 10

    if (digit == k):
        return roundDown // 10 + right + 1

    return roundup // 10


def numberOfk(number, k):
    s = str(number)
    count = 0
    for digit in range(len(s)):
        count += Count(number, digit, k)
    return count


if __name__ == "__main__":
    for _ in range(int(input())):
        a, b = map(int, input().split())
        x = Count0(b) - Count0(a - 1)
        print(x, end=" ")
        for i in range(1, 10):
            x = numberOfk(a - 1, i)
            y = numberOfk(b, i)
            print(y-x, end=" ")
        print()
