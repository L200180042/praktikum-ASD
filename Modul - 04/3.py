class Mhs(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku
h0 = Mhs("Sony", 10, "Sukoharjo", 240000)
h1 = Mhs("Yuuki", 51, "Sragen", 230000)
h2 = Mhs("Lama", 2, "Surakarta", 250000)
h3 = Mhs("test1", 18, "Surakarta", 235000)
h4 = Mhs("www", 4, "Boyolali", 240000)
h5 = Mhs("Fatah", 31, "Salatiga", 250000)
h6 = Mhs("lamaa", 13, "Klaten", 245000)
h7 = Mhs("Kalid", 5, "Wonogiri", 245000)
h8 = Mhs("Deni", 23, "Klaten", 245000)
h9 = Mhs("Budi", 64, "Karanganyar", 270000)
h10 = Mhs("Eko", 29, "Purwodadi", 265000)


Daftar = [h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10]

def cariUangSakuTerkecil2(list):
    temp = [list[0]]
    for i in list[1:]:
        if i.uangSaku < temp[0].uangSaku:
            temp = [i]
        elif i.uangSaku == temp[0].uangSaku:
            temp.append(i)
    return temp

a = cariUangSakuTerkecil2(Daftar)
for i in a:
    print(i.nama)
