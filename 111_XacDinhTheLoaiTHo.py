def sol():
    n = int(input())
    cnt = []
    cur = 0
    z = 0
    for i in range(n//2):

        x = len([str(i) for i in input().split()])
        y = len([str(i) for i in input().split()])
        if x == 6 and y == 8:
            if cur == 2 or cur == 0:
                cnt.append(1)
            cur = 1
        elif x == 7 and y == 7:
            if z < 4:
                z += 2
            if cur == 1 or cur == 0 or z == 4:
                cnt.append(2)
                z = 0
            cur = 2

    print(len(cnt))
    for i in range(len(cnt)):
        print(cnt[i])


'''
16
Mot canh hai canh lai ba canh
Tran troc ban khoan giac chang lanh
Canh bon canh nam vua chop mat
Sao vang nam canh mong hon bay
Minh ve minh co nho ta
Muoi lam nam ay thiet tha man nong
Minh ve minh co nho khong
Nhin cay nho nui nhin song nho nguon
Mot canh hai canh lai ba canh
Tran troc ban khoan giac chang lanh
Canh bon canh nam vua chop mat
Sao vang nam canh mong hon bay
Mot canh hai canh lai ba canh
Tran troc ban khoan giac chang lanh
Canh bon canh nam vua chop mat
Sao vang nam canh mong hon bay
'''
if __name__ == "__main__":
    sol()
