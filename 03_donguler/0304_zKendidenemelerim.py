# region ex1

"""
Ekrana Yazılacak Metni Giriniz: Ecodation
Ecodation
Ecodation
Ecodation
Ecodation
Ecodation



metin = input("ekrana yazılacak metni giriniz\t:")
i = 0
while i<5:
    print(metin)
    i += 1
"""
# endregion


# region ex2
"""
Aşağıdaki Pattern'i Python While Loop İle Yapınız
* * * * * * * * * *
 

i = 0
while i<10:
    print(" * ", end = " ")
    i += 1

"""

# endregion


# region ex3

"""
Aşağıdaki Pattern'i Python While Loop İle Yapınız
 * $ * $ * $ * $ * $


i = 0
while i<10:
    if i %2 == 0 :
        print(" * ", end = " ")
    else:
        print(" $ ", end = " ")
    i += 1

"""


# endregion


# region ex4
"""
Aşağıdaki Pattern'i Python While Loop İle Yapınız
 * * * * * * * * * *
 $ $ $ $ $ $ $ $ $ $
 * * * * * * * * * *
 $ $ $ $ $ $ $ $ $ $
 * * * * * * * * * *
 $ $ $ $ $ $ $ $ $ $
 * * * * * * * * * *
 $ $ $ $ $ $ $ $ $ $
 * * * * * * * * * *
 $ $ $ $ $ $ $ $ $ $


i, j = 0, 0
while i < 10:
    while j < 10:
        if i %2 == 0 :
            print("*", end = " ")
        else:
            print("$", end = " ")
        j += 1
    i +=1
    j = 0
    print()    
"""

# endregion


# region ex5

"""
1→  [1-99] arası tek sayıları yan yana yazdıralım
2→  Her bir 10 adet sayıda alt satıra alalım


i = 1
s = 0
while i < 100:
    if s % 10 == 0:
        print()
    print(i, end=" ")
    s += 1
    i += 2
"""

# endregion


# region ex6
"""
1→  [1-99] arası tek sayıların toplamını yazdıralım



i = 1
toplam=0
while i<100 :
    toplam += i
    i +=2
print(f"[1-99] arası tek sayıların toplamı {toplam} dır")            

"""


# endregion


# region ex7

"""
Lütfen Sayı Giriniz:    5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...


i = 1
sayi = int(input("Lütfen Sayı Giriniz: "))
while i <= 10:
    print(f"{sayi } x {i} = {sayi*i}")
    i += 1
"""

# endregion


"""
[19-99] arası tek sayıları yan yana yazdıralım


i = 19

while i < 100:
    if i % 2 == 1:
        print(i, end = " ")
    i += 1

"""





"""
[19-99] arası tek sayıları yan yana yazdıralım
10 ar 10 ar alta geçicek


i = 19
while i < 100 :
    if i % 2 != 0 :
        print(i, end= " ")
    if i % 20 == 17 :
        print()
    i += 1
"""






"""

Kırk Haramilerin hazine dolu mağarasından çıkmak için, gizli kelime olan
susamı bulmaya çalışan kahramanımızın hikayesini python ile yazalım
1→  kullanıcı gizli kelime girecek
2→  sonsuz döngü içinde kelimeyi bulmaya çalışırken, bulduğu anda döngüden çıkacak


gizliKelime = input("açıl .... açıl!!! lütfen boşluğu doldurun: \t")
while gizliKelime != "susam":
    print("hahahahahah ne oldu bilemedin ama :-)")
    gizliKelime = input("açıl .... açıl!!! lütfen boşluğu doldurun: \t")
print("başardın!!!")

"""







"""

Kullanıcıdan sonsuz döngü içinde sayı girmesi istenir. 0 girdiğinde döngüden çıkılacak.
1→  döngü sonunda girilen sayıların ortalaması hesaplanacak


adet, toplam = 0, 0
sayi = int(input("lütfen sayı giriniz, çıkmak için 0 giriniz... : "))
while sayi:
    toplam += sayi
    adet += 1
    sayi = int(input("lütfen sayı giriniz, çıkmak için 0 giriniz... : "))
print(f"girdiğiniz sayıların ortalaması → {toplam/adet}")

"""





"""
öğrencilerin vize final notlarını isticez sonra çıktı olarak genel ortalam bulucaz




secim = input("uygulamadan çıkmak için 'ç'")
i=1
ort =0
while secim != "ç":
    vize = int(input(f"{i}. öğrencinin vize notunu giriniz\t:"))
    final = int(input(f"{i}. öğrencinin final notunu giriniz\t:"))
    i +=1
    secim = input("uygulamadan çıkmak için 'ç'")
    ort += (vize + final)/2
genelort = ort/(i-1)
print(genelort)

"""






"""
Kullanıcının girdiği rakama göre aşağıdaki gibi bir seri ekrana yazılacak
x - 2x - 3x - 4x - 5x
1→  kullanıcı rakam girecek
2→  int dönüşümü yapılacak
3→  döngü 5 kez tekrar ederek ekrandaki gibi bir çıktı yazılacak
Lütfen [1-9] arası rakam giriniz:  4
4  8  12  16  20




i = 0
rakam =int(input("Lütfen [1-9] arası rakam giriniz\t:"))
while i <5:
    i+=1
    print(rakam*i, end = " ")

veya aynısı :

i = 0
rakam =int(input("Lütfen [1-9] arası rakam giriniz\t:"))
while i <5:
    print(rakam*(i+1), end = " ")
    i+=1
    
    
"""


"""

1→  sayıların faktoriyelini bulacağız: [1-5] arası
2→  döngü 5 kez tekrar edecek
Çıktı:
1   1
2   2
3   6
4   24
5   120




i =1
sonuc = 1
while i<6:
    sonuc *= i
    print(f"{i}  {sonuc} ")
    i +=1

"""



"""
rasgele sayı üreteceğiz [1, 99]
kullanıcı 3 kez sayı girecek, en yakın tahmin ekrana basılacak
örn →  54
34
50
99
en yakın sayı 50
örn →  54
51
4
99
en yakın sayı 51





import random
enKucukFark = 9999999
rSayi = random.randint(1, 99)
print(rSayi)  # bu satır bilgi amaçlıdır, publish etmeden önce sil
i = 0
while i < 3:
    tahmin = int(input("lütfen [1-99] arası sayı tahmin ediniz\t :"))
    fark = rSayi - tahmin
    if fark < 0:
        fark *= -1
    if fark < enKucukFark:
        enKucukFark = fark
        enYakinTahmin = tahmin
    i += 1
print(f"en yakın tahmininiz {enYakinTahmin}")



"""






"""



"""
