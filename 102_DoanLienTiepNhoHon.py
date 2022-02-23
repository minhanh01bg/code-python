def sol():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = []
    z = []
    z.append(1)
    b.append(0)
    for i in range(1,n):
        while len(b) > 0 and a[b[len(b)-1]] <= a[i]:
            b.pop()
        if len(b) == 0:
            z.append(i+1) 
        else:
            z.append(i-b[len(b)-1])
        b.append(i)
    
    for i in z:
        print(i,end=" ")
    print()    
    
if __name__ == "__main__":
    for i in range(int(input())):
        sol()