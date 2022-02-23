class HoaDon:
    def __init__(self, id, name, sL, gia, tien):
        self.id = id
        self.name = name
        self.sL = sL
        self.gia = gia
        self.tien = tien

    def sum(self):
        return self.gia*self.sL - self.tien

    def Prin(self):
        return str(self.id) + " " + str(self.name) + " " + str(self.sL) + " " + str(self.gia) + " " + str(self.tien)+" " + str(self.sum())


if __name__ == "__main__":
    l = []
    for i in range(int(input())):
        l.append(HoaDon(input(), input(), int(
            input()), int(input()), int(input())))

    l = sorted(l, key=lambda x: -x.sum())
    for i in l:
        print(i.Prin())
'''
3
ML01
May lanh SANYO
12
4000000
2400000
ML02
May lanh HITACHI
4
2550000000
0
ML03
May lanh NATIONAL
5
3000000
150000
'''
