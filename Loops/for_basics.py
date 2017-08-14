#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Odpowiedzi na zadania umieszaj bezpośrednio pod poleceniem.
Zadania z gwiazdką są trudniejsze i są opcjonalne.
Zadania z podwója gwiazdką są bardzo trudne i również są opcjonalne.
"""


# region zadania z funkcją range()
# 1. Napisz program wypisujący co drugą liczbę z przedziału <1, 50>
  for i in range(1, 51, 2): 
..   print(i, end=' ') 
..   
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49    

# 2. Napisz program wypisujący kwadraty liczb z przedziału <1, 10>
   for i in range(1, 11): 
..   i *=i 
..   print(i) 
..   
1
4
9
16
25
36
49
64
81
100
   

# 3. Napisz program wypisujący liczby z przedziału <100, 1>
   for i in range(100, 1, -1): 
..   print(i, end='') 
..   
100999897969594939291908988878685848382818079787776757473727170696867
6665646362616059585756555453525150494847464544434241403938373635343332
3130292827262524232221201918171615141312111098765432   

# 4. Napisz program wypisujący liczby podzielne przez 8.
   for i in range(2, 110): 
..   if i%8 ==0: 
..     print(i, end=' ') 
..     
8 16 24 32 40 48 56 64 72 80 88 96 104    

# 5. Napisz program wypisujący liczby podzielne przez 3 lub 5.
   for i in range(2, 110): 
..   if i%3 ==0 or i%5 ==0: 
..     print(i, end=' ') 
..     
3 5 6 9 10 12 15 18 20 21 24 25 27 30 33 35 36 39 40 42 45 48 50 51 54 55 57 60 63 65 66 69 70 72 75 78 80 81 84
85 87 90 93 95 96 99 100 102 105 108 

# 6. Napisz program wypisujący liczby podzielne przez 2 i 3.
   for i in range(2, 110): 
..   if i%3 ==0 and i%2 ==0: 
..     print(i, end=' ') 
..     
6 12 18 24 30 36 42 48 54 60 66 72 78 84 90 96 102 108   

# 7*. | Napisz program znajdujący największą liczbę podzielną przez 2,3,5,7
#     | ale mniejszą od 1000

#załozyłam, że range wypisuje od 1~~999 wiec nie dalam warynku i<1000

   for i in range(1, 1000): 
..   if i%2 ==0 and i%3 ==0 and i%5 ==0 and i%7 ==0: 
..     print(i, end=' ') 
..     
210 420 630 840    

# 8* | Napisz program wypisujący pojedynczo(!) każdą liczbę z poniższej listy:
  L = [[1, 2, 3], [5, 6, 7], [21, 43, 545]]
   for i in L: 
..   for j in i: 
..     print(j) 
..     
1
2
3
5
6
7
21
43
545

# endregion
# region zadania z iterowaniem kolekcji

# 9. Napisz program wypisujący litery ze stringa.
   L = 'masakra'
   for i in L: 
..   print (i, end=' ') 
..   
m a s a k r a    

# 10. Napisz program wypisujący kolejne słowa ze stringa.
x = 'Taksanska masakra pila mechaniczna'
   for i in x: 
..   print (i, end='') 
..   
Taksanska masakra pila mechaniczna  

# 11. Napisz program wypisujący liczbę cyfr z liczby.
   x='1234567890098765'
   len(x)
=> 16   

# 12. Napisz program wypisujący cyfry z liczby. Cyfry nie mogą się powtarzać.
   L = [1, 2, 3, 3, 4, 5, 2, 3]
   set (L)
=> {1, 2, 3, 4, 5}   

# 13. Napisz program sprawdzający czy wszystkie cyfry liczby są parzyste.
   L=[1, 2, 3, 4, 6, 7, 88, 7, 62]
for i in L: 
..   if i % 2 == 1: 
..       continue 
..   print(i)      
..   
2
4
6
88
62

# 14. | Napisz program wypisujący zadaną liczbę zastępując jej kolejne cyfry liczbami powstałymi przez
#     | dodanie do cyfr liczby 1 (1598 = 26109)
   Z = 1598
   V = list(str(Z))
   V
=> ['1', '5', '9', '8'] 
   for i in V: 
..   print((int(i)+1), end='') 
..   
26109 

# 15. | Napisz program wypisujący przywitania z Pythonem w podanych poniżej językach świata.
#     | Oczekiwany wynik: 'Hello Python' i tak dalej dla każdego języka.
hellos = [
    "Hello",
    "Tungjatjeta",
    "Grüßgott",
    "Вiтаю",
    "dobrý den",
    "hyvää päivää",
    "你好",
    "早上好"]

#nie wiedzialam jak to przekopiowac do repl.it

   hellos = ['Hello', 'Tungjatjeta', Dobry den', 'Hyvaa paivaa']
for i in hellos: 
..   print (i + ' ' + 'Python') 
..   
Hello Python
Tungjatjeta Python
Dobry den Python
Hyvaa paivaa Python
              


# 16**. | Napisz program sprawdzający czy numer PESEL jest poprawny.
#      | opis: https://pl.wikipedia.org/wiki/PESEL#Cyfra_kontrolna_i_sprawdzanie_poprawno.C5.9Bci_numeru
