#output anıdna casting - dönüşüm ile ilgili efor harcamamak için format yöntemleri kullanırız

#region format
#ekrana output formatlarken ilk yöntem → format
"""
rakam = int(input("lütfen 0-9 arası rakam giriniz\t: "))
print("girdiğiniz rakamın bir fazlası {}".format(rakam+1))
print("girdiğiniz {} rakamının bir fazlası {}".format(rakam, (rakam+1)))
a = int(input("l. a. de. giriniz: "))
b = int(input("l. b. de. giriniz: "))
print("{} değeri ile {} değerinin toplamı {}". format(a, b, (a+b)))
"""
#endregion

#region fstring
#ekrana output formatlarken ilk yöntem → fstring
"""
rakam = int(input("lütfen 0-9 arası rakam giriniz\t: "))
print(f"girdiğiniz {rakam} rakamının bir fazlası {rakam+1}")
a = int(input("l. a. de. giriniz: "))
b = int(input("l. b. de. giriniz: "))
print(f"{a} değeri ile {b} değerinin toplamı {a+b}")
"""
#endregion

#region ornek
"""
s1 = int(input("l. s. g. : "))
s2 = int(input("l. s. g. : "))
print(f"girdiğiniz sayıların toplamı {s1+s2}")
print(f"{s1} + {s2} = {s1+s2}")
"""
"""
#girdiğiniz sayıların toplamı 8
#3 + 5 = 8
"""
#endregion-


#region ornekler

"""
sayi=int(input("Bir sayi girin\t: "))
sayi_2=sayi**2
print("sayinin karesi= ",sayi_2)

bunu f stringle yazıcaz


sayi=int(input("Bir sayi girin\t: "))
print(f"{sayi} değerinin karesi {sayi**2}")



kilo = int(input("Lütfen kilonuzu giriniz:"))
boy = float(input("lütfen boyunuzu giriniz"))
v_k_e = kilo/(boy**2)
v_k_e = round(v_k_e, 3)
print("vucut kitle indeksiniz:",v_k_e)

bunu f stringle


kilo = int(input("Lütfen kilonuzu giriniz:"))
boy = float(input("lütfen boyunuzu giriniz"))
v_k_e = kilo/(boy**2)
v_k_e = round(v_k_e, 3)
print(f"kilosu {kilo} ve boyu {boy} olan kişi için vücut kitle indeksiniz: {v_k_e}")


Lütfen 1. Sayıyı Giriniz : 10
Lütfen 2. Sayıyı Giriniz : 15
Lütfen 3. Sayıyı Giriniz : 30
10, 15 ve 30 sayılarının ortalaması → 15.0



sayi1 = int(input("Lütfen 1. Sayıyı Giriniz :"))
sayi2 = int(input("Lütfen 2. Sayıyı Giriniz :"))
sayi3 = int(input("Lütfen 3. Sayıyı Giriniz :"))
ort = (sayi1 + sayi2 + sayi3)/3
print(f"{sayi1},{sayi2} ve {sayi3} sayılarının ortalaması → {round(ort,2)}")

"""


# ödev →
"""
Lütfen Üçgenin A Kenarı Açısını Giriniz: 30
Lütfen Üçgenin B Kenarı Açısını Giriniz: 60
C Kenarı 90 Derecedir


ilk_kenar = int(input("Lütfen Üçgenin A Kenarı Açısını Giriniz: "))
ikinci_kenar = int(input("Lütfen Üçgenin B Kenarı Açısını Giriniz: "))
ucuncu_kenar = (180 - (ilk_kenar + ikinci_kenar))
print(f"C kenarı {ucuncu_kenar} derecedir")

"""

# örnek →

"""
Lütfen A Kenarı Giriniz:  10
Lütfen B Kenarı Giriniz : 30
Dörtgenin Alanı  → 300 metre karedir
"""



# örnek →

"""
- Kullanıcıdan x1,x2,y1,y2 değerleri alınır
- uzaklik =[ (x1-x2)karesi + (y1-y2)karesi ] karekök
- format : (x1,x2) ve (y1,y2) noktaları arasındaki uzaklık .. birimdir.
- virgülden 2 basamak olacaktır.


x1 = int(input("x1 : "))
x2 = int(input("x2 : "))
y1 = int(input("y1 : "))
y2 = int(input("y2 : "))

uzaklik = (((x1 - x2)**2)+((y1 - y2)**2))**.5

print(f"({x1},{x2}) ve ({y1},{y2}) noktaları arasındaki uzaklık {round(uzaklik,2)} birimdir.)" )

"""

#endregion