#region tip_dönüşümü
"""
dTarihi = int(input("Doğum Tarihi Giriniz\t: "))
#dTarihi = int(dTarihi)
yas = 2021 - dTarihi
print(dTarihi, "doğum tarihli üyemizin yaşı", yas)
"""
#endregion




#region ornek
"""
a kenarı, b kenarı girilecek dörtgen için alan hesaplanacak
int dönüşümü yapılacak
"""
a = int(input("lütfen dörtgenin a kenarını giriniz : "))
b = int(input("lütfen dörtgenin b kenarını giriniz : "))
print("dörtgenin alanı", a*b, "metre kare.")
#endregion


"""
kilo = 70
boy = 1.75
v_k_e = kilo/(boy**2)
v_k_e = round(v_k_e, 3)
print("vucut kitle indeksiniz:",v_k_e)

bunu inputlu yapıcaz
"""

kilo = int(input("Lütfen kilonuzu giriniz :"))
boy = float(input("Lütfen boyunuzu giriniz :"))
v_k_e = kilo/(boy**2)
v_k_e = round(v_k_e, 3)
print("vucut kitle indeksiniz:",v_k_e)



sayi=int(input("Bir sayi girin\t: "))
sayi_2=sayi**2
print("sayinin karesi= ",sayi_2)



