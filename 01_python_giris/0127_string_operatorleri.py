#region string_operatorleri
"""
+ = concatenation
* = replication
a = "A"
b = "B"
c = "C"
yazdir = a + b + c
print(yazdir)  → ABC
"""

"""
print(3*3)
print("istanbul"*3)
print("+"*50)
print("+"*50)
print("+")"""
#endregion

#region ornek


"""
okulTuru = "Anadolu"
seviye = 12
print(okulTuru + " " + str(seviye))
#endregion

bu hata verir
"""


"""
bolumu = "hukuk"
seviye = 3
adSoyad = "Ali Kemal"
print(bolumu + " fakültesi" + seviye + ". sınıf öğrencisi" + adSoyad)

#burda hata alırız çünkü seviyeyi str yapmamız lazım çünkü diğerleri str

"""


bolumu = "hukuk"
seviye = 3
adSoyad = "Ali Kemal"
print(bolumu + " fakültesi" + str(seviye) + ". sınıf öğrencisi" + adSoyad)