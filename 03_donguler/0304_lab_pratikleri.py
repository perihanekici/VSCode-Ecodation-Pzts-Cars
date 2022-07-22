#region ornek1

"""
lütfen ekrana yazılacak metni giriniz : Aziz
Aziz
Aziz
Aziz
Aziz
Aziz

metin = input("lütfen ekrana yazılacak metni giriniz :")

i = 0

while i<5 :
    i += 1
    print (metin)





metin = input("lütfen ekrana yazılacak metni giriniz :")

a= int(input("lütfen tekrar sayısını giriniz:"))

i = 0

while i<a :
    i += 1
    print (metin)





# * * * * * * * * * *  → 10 tane yan yana yıldız yaz


i = 0

while i<10 :
    i += 1
    print(" * ", end="")



# * $ * $ * $ * $ * $  → 10 tane yan yana yıldız ve dolar yaz


i = 0

while i<10:
    if i %2 == 0 :
        print(" * ", end = "")
    else :
        print(" $ ", end = "")
    i += 1
    
"""

"""
  * * * * * * * * * *
  $ $ $ $ $ $ $ $ $ $
  * * * * * * * * * *
  $ $ $ $ $ $ $ $ $ $
  * * * * * * * * * *
  $ $ $ $ $ $ $ $ $ $
  * * * * * * * * * *
  $ $ $ $ $ $ $ $ $ $
  * * * * * * * * * *
  $ $ $ $ $ $ $ $ $ $   çıktı bu olacak

i,j = 0,0

while i<10:


    while j<10:
        if i%2==0:
            print("*",end="")
        else:

            print("$",end="")
        j+=1



    print()
    i+=1
    j=0




"""


"""
  * $ * $ * $ * $ * $
  * $ * $ * $ * $ * $
  * $ * $ * $ * $ * $
  * $ * $ * $ * $ * $
  * $ * $ * $ * $ * $
  * $ * $ * $ * $ * $
  * $ * $ * $ * $ * $
  * $ * $ * $ * $ * $
  * $ * $ * $ * $ * $


i , j  = 0 , 0
while i<10 :
    while j<10 : 
        j += 1
        if j%2==1 :
            print(" * " , end=" " )
        else :
            print(" $ " , end= " ")
    i += 1
    j = 0 
    print()



"""

"""
  * $ * $ * $ * $ * $
  $ * $ * $ * $ * $ *
  * $ * $ * $ * $ * $
  $ * $ * $ * $ * $ *
  * $ * $ * $ * $ * $
  $ * $ * $ * $ * $ *
  * $ * $ * $ * $ * $
  $ * $ * $ * $ * $ *
  * $ * $ * $ * $ * $
  $ * $ * $ * $ * $ *

i=0
j=0
while i < 10:
    

    while j<10:
        j+=1
        if(i % 2 == 0 ):
            if(j%2==0):
                print("*",end="")
            else:
                print("$",end="")
        else:
                if(j%2==0):
                    print("$",end="")
                else:
                    print("*",end="")
    i+=1
    j=0
    print()

"""

"""
Lütfen Sayı Giriniz: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25


sayi = int (input("Lütfen sayı giriniz : "))
i = 1
while i <= 5 :
    print(f"{sayi} x {i} = {sayi*i}")  
    i += 1


"""

"""
* 
* * 
* * *
* * * *
* * * * * 
* * * * * *
* * * * * * *
* * * * * * * *





"""




#endregion




