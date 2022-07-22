#region atama_operatoru
"""
name = "Jhon"
print(name)
"""
#endregion

#region round
"""
s = 1.838983121212
print(round(s, 3))
"""
kg = 80
mt = 1.60
vki = kg/mt**2
print(round(vki, 2))
#endregion

#region sonucu_yine_kendi_degerine_atama
"""
i = 1
print(i)  →1
i = i + 1
print(i)    →2
sayi = 10
sayi = sayi - 1
sayi = sayi * 2
x=10
x = x + 1
print(sayi)   →18
print(x)
"""
#endregion

#region az_sayida_degisken_kullanma
"""
sayi = 5
toplam = 0
toplam = toplam + sayi
sayi = 10
sayi = sayi + 1
toplam = toplam + sayi
"""
#endregion



kg = 70
boy = 1.75
vki = kg/(boy**2)

print("vücut kitle indeksiniz:",vki)  #bunun cevabı 22.857142857...
#ama vki yi round(vki,3) yazarsak son 3 basamağı yazıp onu yuvarlar→cevap 22.857 olur.
print(round(123.565656,3))