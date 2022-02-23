class GV:
    def __init__(self, id, name, ma, dTH, dcm):
        self.id = "GV{:02d}".format(id)
        self.name = name
        self.ma = ma
        self.dTH = dTH
        self.dcm = dcm

    def diem(self):
        x = 0
        if int(self.ma[-1]) == 1:
            x = 2
        elif int(self.ma[-1]) == 2:
            x = 1.5
        elif int(self.ma[-1]) == 3:
            x = 1.0
        return self.dTH*2 + x + self.dcm
    def maM(self):
        if self.ma[0] == 'B':
            return "LY"
        elif self.ma[0] == 'A':
            return "TOAN"
        else:
            return "HOA"
    def check(self):
        if self.diem() >= 18:
            return "TRUNG TUYEN"
        else:
            return "LOAI"

    def Pin(self):
        return str(self.id) + " " + self.name + " " +self.maM()+" "+ "{:.1f}".format(self.diem())+ " " + self.check()


if __name__ == "__main__":
    l = []
    for i in range(1, int(input())+1):
        l.append(GV(i, input(), input(), float(input()), float(input())))
    l = sorted(l, key=lambda x: -x.diem())
    for i in l:
        print(i.Pin())
        
'''
12
Le Van Binh
A1
7.0
3.0
Tran Van Toan
B3
4.0
7.0
Hoang Thi Tam
C2
7.0
6.0
Le Van Binh
A1
7.0
3.0
Tran Van Toan
B3
4.0
7.0
Hoang Thi Tam
C2
7.0
6.0
Le Van Binh
A1
7.0
3.0
Tran Van Toan
B3
4.0
7.0
Hoang Thi Tam
C2
7.0
6.0
Le Van Binh
A1
7.0
3.0
Tran Van Toan
B3
4.0
7.0
Hoang Thi Tam
C2
7.0
6.0
'''