import re
s="a123aaaa.b?b+4-56bbccc"
a=re.findall("\d", s) #lay cac ki tu co trong chuoi
b=re.split("\.|\?|\!", s) #chat theo . or ? or !
s = re.sub("\w"," ",s) #thay ki tu bang khoang trang
'''
\d lay cac so   
\d+ lay cac so lien tiep   
\s+ lay cac khoang trang lien tiep
\.|\?|\! lay 1 trong 3 ki tren   
[a-z] chi cac chu thuong   
\W tat ca ki tu dau
\w tat ca ki tu khac ki tu dau   
\w+ tat ca tu lien tiep  
'''
#doi co so
def convertTo(n, new_base):
    p = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = ""
    while n > 0:
        s += p[n % new_base]
        n //= new_base
    return s[::-1]

print("{:02d}/{:02d}/{:04d}".format(1, 2, 2014)) #format ngay
print("{:.2f}".format(2.567))

from datetime import date
da1 = date(2019,10,5)
da2 = date(2019,10,6)
print((da2 - da1).days)

prime = [1 for i in range(1000001)]
for i in range(2, 1000001):
    for j in range(2 * i, 1000001, i):
        prime[j] += i