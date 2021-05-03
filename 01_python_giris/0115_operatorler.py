#region aritmetik-operatorler
# aritmetik operatörler
"""
1→  +   toplama
2→  -   çıkarma
3→  *   çarpma
4→  /   bölme
5→  //  tam bölme
6→  **  üst alma
7→  %   mod alma
"""
#endregion

#region +,- → binary
"""
print(3+3)
print(-3+8)
print(3-9)
"""
print(5. + 8)     #-5.0 + 8
print(-5. + -6.0)   #-5.0 + 8
print(.5 + 2)
#endregion


#region +,- → unary
"""
print(+2)
print(-9)
"""
#endregion

#region *,/
"""
print(3*3)
print(3/3)
"""
#endregion


#region **
"""
print(2**2)
print(3**3)
print(3.**3.0)
"""
#endregion

#region //
"""
print(13/5)  #2.6
print(13//5)  #2
print(-13/5)  #-2.6
print(-13//5)  #-3
"""
#endregion

#region %
"""
print(15 % 4)  # 3
print(15 % 4.)  #3.0
"""
#endregion


#region operator_oncelikleri
"""
1→  +, -        unary
2→  **          üst alma
3→  *, /, %     çarpma, bölme, mod alma
4→  +,-         toplama çıkarma
"""
"""
print(3+4*5)   #23
print(15%4*2)   #% left-side binding  →6
print(15%4%2)   #% left-side binding  →1
print(2**2**3)  #** right-side binding  →256
"""
#endregion