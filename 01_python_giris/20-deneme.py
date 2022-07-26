"""

print("\"slm\"")



print(16**(1/2))

a = input("lütfen sayı giriniz")
print(a)


pd = "python"
os = "10"
ver = "3.9.2"

print("windows versiyonu" + os + " " + pd + "versiyonu" + ver)



s = 1.838983121212
print(round(s, 3))



a = 2
print("sayının bir fazlası :", a)



print(10 == 10)




sayi = int(input("Lütfen sayı giriniz :"))
if sayi <= 0 :
    print ("Sıfır veya negatif sayı giremezsiniz")
else:
    if sayi < 100 :
        print(f"{sayi} sayısı 100den küçüktür")
    elif sayi == 100 :
        print(f"{sayi} sayısı 100e eşittir")
    else:
        print(f"{sayi} sayısı 100den büyüktür")



devammi = True
sayac = 5
while devammi:
    print(sayac)
    if sayac == 2:
        devammi = False
    sayac -= 1



eb = -9999999999999999
sayi = int(input("Lütfen sayı giriniz, çıkmak için -1 giriniz \t :"))
while sayi != -1:
    if sayi> eb :
        eb = sayi
    sayi = int(input("Lütfen sayı giriniz, çıkmak için -1 giriniz \t :"))
print(f"girdiğiniz sayılardan en büyüğü \t: {eb}")



tekler, ciftler = 0, 0
sayi = int(input("Lütfen sayı giriniz, çıkmak için -1 giriniz \t :"))
while sayi != -1:
    if sayi % 2 == 0 :
        ciftler += 1
    else:
        tekler += 1
    sayi = int(input("Lütfen sayı giriniz, çıkmak için -1 giriniz \t :"))
print(f"çift sayıların adedi \t : {ciftler}")
print(f"tek sayıların adedi \t : {tekler}")


i, j = 0, 0
while i < 10:
    while j < 10:
        print(" * ", end = "")
        j += 1
    i += 1
    j = 0
    print()



i, j = 0, 0
while i < 10:
    while j < 10:
        if i % 2 == 0:
            print(" * ", end="")
        else:
            print(" ! ", end="")
        j += 1
    i += 1
    j = 0
    print()

"""