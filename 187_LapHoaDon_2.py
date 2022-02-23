from datetime import date,datetime,time
class HoaDon:
    def __init__(self, id, name, sP, dF, dS, dV):
        self.id = "KH{:02d}".format(id)
        self.name = name
        self.sP = sP
        self.dF = dF
        self.dS = dS
        self.dV = dV

    

def sol():
    print("KH{:02d}".format(1))
    da1 = date(2019,10,5)
    da2 = date(2019,10,6)
    print((da2 - da1).days)


if __name__ == "__main__":
    sol()
