def sol():
    n = int(input())
    check = [1]*(n + 90000)
    prime = []
    check[0] = 0
    check[1] = 0
    for i in range((n + 90000)):
        if check[i] == 1:
            prime.append(i)
            for j in range(i**2, (n + 90000), i):
                check[j] = 0
    for i in range(len(prime)):
        if prime[i] >= n:
            break
        x = str(prime[i])
        revX = "".join(reversed(x))

        if check[int(revX)] == 1 and prime[i] != int(revX) and int(revX) > prime[i] and int(revX) < n:
            print(x, revX, end=" ")
    print()


if __name__ == "__main__":
    for i in range(int(input())):
        sol()
