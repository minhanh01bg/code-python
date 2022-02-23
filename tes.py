import math
math.ceil(9.23) #lam tron ve so nguyen lon hon nhung van o kieu float
math.floor(8.67) #lam tron ve so nguyen lon hon nhung van o kieu float
math.comb(9, 6) #to hop chap k, n
math.ceil(9) #lam tron ve so nguyen
math.factorial(5) #tinh giai thua
f = math.factorial

round(9) #lam tron nhung phia sau ko co so 0
format(9, ".5f") #lam tron co n so 0 phia sau
import itertools
a=[1, 2, 3, 4, 5]
list(itertools.combinations(a, 3)) #liet ke to hop n, k
a=[1, 2, 3, 4, 5]
list(itertools.permutations(a)) #liet ke hoan vi n
#sort dict
a=dict()
a=dict(sorted(a.items(), key=lambda x: x[0]))
#sang nguyen to
prime = [i for i in range(1000001)] i = 2
while i*i < 1000001: if prime[i] == i:
        for j in range(i*i, 1000001, i):
            prime[j] = 0
    i += 1
s=""
s.islower() #kiem tra tat ca viet thuong khong
s.isdigit() #kiem tra toan bo chuoi la so hay khong
a=[]
b=[1, 2, 3]
a.extend(b) #them phan tu tu list b vao list a
d={i:a.count(i) for i in a} #tao 1 dict voi key va value la cac phan tu cua a
ord('9') #chuyen ki tu ve ma ascii
bin(12)
oct(123)
hex(1234)
#tu dong dung khi ket thuc nhap
while True: try: s = input().strip() except EOFError: break\