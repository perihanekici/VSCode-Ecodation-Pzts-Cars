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



i=1
j=0
while i<100:
    if j%10==0:
        print()
    print(i, end=" ")
    j+=1
    i+=2

"""
# 1→  [1-99] arası tek sayıların toplamını yazdıralım

"""
Lütfen Sayı Giriniz:    5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...


i=1
sayi=int(input("lütfen bir sayı giriniz \t :"))
while i<=10:
    print(f"{sayi}x{i} = {sayi*i}")
    i+=1


[19-99] arası tek sayıları yan yana yazdıralım    

i=19
while i<100:
    print(i,end=" ")
    i+=2


[19-99] arası tek sayıları yan yana yazdıralım
10 ar 10 ar alta geçicek


i=19
j=0
while i<100:
    if j%10==0:
        print()
    print(i,end=" ")
    i+=2
    j+=1


i = 19
while i < 100 :
    if i % 2 != 0 :
        print(i, end= " ")
    if i % 20 == 17 :
        print()
    i += 1


print()
kelime= input("Açıl .......... açıl!!! \nLütfen boşluğu doldurunuz\t:")
while kelime!= "susam":
    print()
    print("bilemedin şaşkınnn....")
    print()
    kelime= input("Açıl .......... açıl!!! \nLütfen boşluğu doldurunuz\t:")
print()
print("helal sana beee")

Kullanıcıdan sonsuz döngü içinde sayı girmesi istenir. 0 girdiğinde döngüden çıkılacak.
1→  döngü sonunda girilen sayıların ortalaması hesaplanacak


adet,toplam=0,0
sayi = int(input("lütfen bir sayı giriniz, çıkmak için 0 \t :"))
while sayi != 0:
    adet +=1
    toplam += sayi
    sayi = int(input("lütfen bir sayı giriniz, çıkmak için 0 \t :"))
print(f"girdiğiniz sayıların ortalaması\t: {toplam/adet}")



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


Kullanıcının girdiği rakama göre aşağıdaki gibi bir seri ekrana yazılacak
x - 2x - 3x - 4x - 5x
1→  kullanıcı rakam girecek
2→  int dönüşümü yapılacak
3→  döngü 5 kez tekrar ederek ekrandaki gibi bir çıktı yazılacak
Lütfen [1-9] arası rakam giriniz:  4
4  8  12  16  20



i=1
rakam=int(input("1-9 arası bir rakam giriniz\t:"))
while i<6:
    print(rakam*i, end=" ")
    i+=1



1→  sayıların faktoriyelini bulacağız: [1-5] arası
2→  döngü 5 kez tekrar edecek
Çıktı:
1   1
2   2
3   6
4   24
5   120


i=1
fak = 1
while i<6:
    print(f"{i}   {fak}")
    i+=1
    fak *=i



import random
enkucukfark = 9999999999
rsayi=random.randint(1,99)
i=0
while i<3:
    tahmin=int(input("lütfen bir sayı tahmin ediniz\t:"))
    fark= rsayi-tahmin
    if fark<0:
        fark*=-1
    if fark<enkucukfark:
        enkucukfark=fark
        enyakintahmin=tahmin
    i+=1
print(f"en yakın tahmininiz\t: {enyakintahmin}")
print(rsayi)  # bilgi amaçlı


i, j = 0, 10
while i<10:
    while j>0:
        print(" * ", end= "")
        j -= 1
    i += 1
    j = 10 -i
    print()

i, j, n = 0, 0, 5
while i < 5:
    while j <=5:
        if n>0:
            print(" ", end="")
        else:
            print(" *", end="")     
        j += 1
        n -=1
    i += 1
    n = 5- i
    j = 0
    print()


1→  sonsuz döngü içinde kullanıcın girdiği sayıların
    tek olanlarının ortalamasını bulalım
2→  çift sayı girmeye çalıştığında ekrana uyarı verelim
3→  programı continue kulllanmalıyız

teklertoplami = 0
teksayiadedi = 0
while True:
    sayi = int(input("tek sayı giriniz,çıkmak için -1  :"))
    if sayi == -1:
        break
    if sayi % 2 == 1:
        teklertoplami += sayi
        teksayiadedi += 1
    else:
        print("çift sayı giremezsiniz")
print(f"girdiğiniz sayıların ortalaması: {(teklertoplami/teksayiadedi)}")





toplam = 0
j=1
sayi = int(input("lütfen bir sayı giriniz:"))
for j in range(1,sayi):
    if sayi % j == 0:
        toplam += j
if sayi==toplam:
    print(f"{sayi} sayısı mükemmeldir")
else:
    print(f"{sayi} sayısı mükemmel değildir")

a=list(range(5,10))
print(a)

sayi=int(input("3 veya 4 basamaklı bir sayı giriniz\t:"))
if sayi>99 and sayi<1000:
    kalan = sayi % 10
    birler = kalan // 1
    kalan = sayi % 100
    onlar = kalan // 10
    kalan = sayi % 1000
    yuzler = kalan //100
    top = (birler**3)+(onlar**3)+(yuzler**3)
    if top==sayi:
        print(f"{sayi} sayısı Armstrong sayısıdır.")
    else:
        print(f"{sayi} sayısı Armstrong sayısı değildir.")

if sayi>999 and sayi<10000:
    kalan = sayi % 10
    birler = kalan // 1
    kalan = sayi % 100
    onlar = kalan // 10
    kalan = sayi % 1000
    yuzler = kalan //100
    kalan = sayi % 10000
    binler = kalan//1000
    top = (birler**4)+(onlar**4)+(yuzler**4)+(binler**4)
    if top==sayi:
        print(f"{sayi} sayısı Armstrong sayısıdır.")
    else:
        print(f"{sayi} sayısı Armstrong sayısı değildir.")



sayı = input("Sayı:")
basamak_sayisi = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

gecici_sayı = sayı

while (gecici_sayı > 0):
    
    basamak = gecici_sayı % 10
    
    toplam += basamak ** basamak_sayisi
    
    gecici_sayı //= 10
    

if (toplam == sayı):
    print(sayı,"bir armstrong sayısıdır.")
else:
    print(sayı,"bir armstrong sayısı değildir.")


for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print()

toplam=0
while True:
    sayi=input("lütfen bir sayı giriniz, çıkmak için q:")
    if sayi == "q":
        break
    elif  sayi != "q" and type(sayi)== str :
        print("sayı dışı karakter girmeyiniz")
        continue
        
    else:
        a=int(sayi)
        toplam += a
print(toplam)



liste= ([3,5,9,8,4,15,17,18,20])
adet=0
for i in liste:
    if i%2==1:
        adet+=1
print(f"tek sayıların adedei : {adet}")


ogList = []
while True:
    ogr = input("eklemek istediğiniz öğrenci, çıkmak için -1 :")
    if ogr == "-1":
        break
    ogList.append(ogr)
for i in ogList:
    print(i)


listem = [1, 2, 3, 4, 5]
#temp = listem[2]
#listem[2] = listem[3]
#listem[3] = temp
listem[2], listem[3] = listem[3], listem[2]
print(listem)

"""