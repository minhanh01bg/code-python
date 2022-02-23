check = [1]*1000000
prime = []
check[0] = 0
check[1] = 0
for i in range(1000000):
    if check[i] == 1:
        prime.append(i)
        for j in range(i**2, 1000000, i):
            check[j] = 0


def sol():
    n = int(input())
    cnt = 0
    ans = 0
    while prime[cnt] < n and cnt <= len(prime) - 3:
        if prime[cnt] + 6 > n:
            break
        if prime[cnt] + 2 == prime[cnt + 1] and prime[cnt+2] == prime[cnt] + 6:
            ans += 1
            cnt += 1
        elif prime[cnt] + 4 == prime[cnt + 1] and prime[cnt + 2] == prime[cnt] + 6:
            ans += 1
            cnt += 1
        else:
            cnt += 1
        if cnt >= n or cnt >= 1000000:
            break

    print(ans)


if __name__ == "__main__":
    for i in range(int(input())):
        sol()
