# region infinite_looop→sonsuz_dongu
"""


eb = -99999999999
sayi = int(input("lütfen bir sayı giriniz, çıkmak için -1 giriniz \t : "))
while sayi != -1:
    if sayi>eb:
        eb = sayi
    sayi = int(input("lütfen bir sayı giriniz, çıkmak için -1 giriniz \t : "))
print(f"girdiğiniz sayılardan en büyüğü → {eb}")
"""
# endregion


# region infinite_looop_ornek_1
"""
tekSayilarinAdedi, ciftSayilarinAdedi = 0, 0
sayi = int(input("lütfen bir sayı giriniz, çıkmak için 0 giriniz \t : "))
while sayi != 0:
    if sayi % 2 == 0:
        ciftSayilarinAdedi += 1
    else:
        tekSayilarinAdedi += 1
    sayi = int(input("lütfen bir sayı giriniz, çıkmak için 0 giriniz \t : "))
print(f"girdiğiniz sayılar içinde {tekSayilarinAdedi} adet tek sayı var")
print(f"girdiğiniz sayılar içinde {ciftSayilarinAdedi} adet çift sayı var")
"""
# endregion


# region infinite_looop_ornek_1
"""
tekSayilarinToplami, ciftSayilarinToplami = 0, 0
sayi = int(input("lütfen bir sayı giriniz, çıkmak için 0 giriniz \t : "))
while sayi != 0:
    if sayi % 2 == 0:
        ciftSayilarinToplami += sayi
    else:
        tekSayilarinToplami += sayi
    sayi = int(input("lütfen bir sayı giriniz, çıkmak için 0 giriniz \t : "))
print(f"girdiğiniz sayılar içinde tek olanların toplamı →  {tekSayilarinToplami}")
print(f"girdiğiniz sayılar içinde çift olanların toplamı →  {ciftSayilarinToplami}")
"""
# endregion



"""
eb = -9999999999
sayi = int(input("lütfen sayı giriniz, çıkmak için -1 \t: "))
i = 0

while sayi != -1:
    i += 1
    if sayi > eb:
        eb = sayi
    sayi = int(input("lütfen sayı giriniz, çıkmak için -1 \t: "))
print(f"girilen {i} adet sayılardan en büyüğü {eb}")

"""



"""

tekSayilar=0
ciftSayilar=0


sayi = int(input("lütfen sayı giriniz, çıkmak için 0 \t: "))

while sayi != 0:
    if sayi %2 == 0:
        ciftSayilar += 1
    else:
        tekSayilar += 1
    sayi = int(input("lütfen sayı giriniz, çıkmak için 0 \t: "))

print(f"tek sayıların adedi {tekSayilar}")
print(f"çift sayıların adedi {ciftSayilar}")
"""