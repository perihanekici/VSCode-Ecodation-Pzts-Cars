#region leylek_uygulamasi
""" 
print("Leylek Uygulamasına Hoş Geldiniz!!!
    Sürüş Ücreti → 0.59/dk")
s = int(input("sürüş için geçen süre (saat)\t : "))
d = int(input("sürüş için geçen süre (dakika)\t : "))
toplamDakika = s*60
toplamDakika += d   #shortcut operatörü
toplamTutar = 0.59 * toplamDakika
print(f"Sürüş için geçen süre (saat)\t: {s}")
print(f"Sürüş için geçen süre (dakika)\t: {d}")
print(f"sürüşün toplam süresi {s}:{d} - {toplamDakika} dakika da bitmiştir")
print(f"kartınızdan çekilen toplam tutar {round(toplamTutar,2)}")
"""

"""
 veya böyle de olabilir
print(
    "
    Leylek Uygulamasına Hoşgeldiniz!!!
    Sürüş Ücreti → 0.69/dk
    "
)
s = int(input("sürüş için geçen süre (saat)\t: "))
d = int(input("sürüş için geçen süre (dakika)\t: "))
toplamDakika = s*60
toplamDakika += d
toplamTutar = toplamDakika*0.69
print(f"sürüş için geçen süre {s}:{d} dakika.")
print(f"sürüş için kredi kartından çekilen tutar {round(toplamTutar, 2)} TL.")
"""

#endregion

# ödev →
"""
km cinsinden girilen mesafe bilgisini mil'e çeviren programı yazınız.
mil =  km / 1.609344
"""




# ödev →
"""
Lütfen Üçgenin A Kenarı Açısını Giriniz: 30
Lütfen Üçgenin B Kenarı Açısını Giriniz: 60
C Kenarı 90 Derecedir
"""


# ödev →
"""
- Kullanıcıdan x1,x2,y1,y2 değerleri alınır
- uzaklik =[ (x1-x2)karesi + (y1-y2)karesi ] karekök
- format : (x1,x2) ve (y1,y2) noktaları arasındaki uzaklık .. birimdir.
- virgülden 2 basamak olacaktır.
"""


# ödev 
"""
- Kısaltmalar;
    - at    aylık tüketim giriniz
    - aeb   aktif enerji bedeli
    - db    dağıtım bedeli
    - teb   toplam enerji bedeli
    - tp    trt payı
    - ef    enerji fonu
    - etv   elektrik tüketim vergisi
    - vt    vergiler toplamı
- elektrik faturamızı hesaplayalım
    - aylık tüketim giriniz ? [kWh]  : 500
    - aktif enerji bedeli = aylık tüketim x 0.39736
    - dağıtım bedeli = aktif enerji bedeli x 0,2474
    - toplam enerji bedeli = aktif enerji bedeli + dağıtım bedeli
    - trt payı = 3.97
    - enerji fonu = 1.39
    - elektrik tüketim vergisi = 9.92
    - KDV = (toplam enerji bedeli + trt payı + enerji fonu + elektrik tüketim vergisi) x 0.18
    - vergiler toplamı = trt payı + eerji fonu + elektrik tüketim vergisi + kdv
    - toplam fatura = vergiler toplamı + toplam enerji bedeli
"""


#örnek

miktar=float(input("lütfen benzin endeksini girin\t:"))
yakit_tuketimi=float(input("lütfen yakıt tüketimini(100 km )  girin\t: "))
alinan_yol=int(input("aracın aldığı yolu girin \t:"))
toplam_tuketim=(yakit_tuketimi*alinan_yol*miktar)/100

print(toplam_tuketim)