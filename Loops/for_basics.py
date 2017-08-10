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

# 4. Napisz program wypisujący liczby podzielne przez 8.

# 5. Napisz program wypisujący liczby podzielne przez 3 lub 5.

# 6. Napisz program wypisujący liczby podzielne przez 2 i 3.

# 7*. | Napisz program znajdujący największą liczbę podzielną przez 2,3,5,7
#     | ale mniejszą od 1000

# 8* | Napisz program wypisujący pojedynczo(!) każdą liczbę z poniższej listy:
lista = [[1, 2, 3], [9, 10, 11], [20, 30, 40]]
   L=[[1, 2, 3], [9, 10, 11], [20, 30, 40]]
   for (a, b, c) in L: 
..   print(a, b, c) 
..   
1 2 3
9 10 11
20 30 40

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

# 16**. | Napisz program sprawdzający czy numer PESEL jest poprawny.
#      | opis: https://pl.wikipedia.org/wiki/PESEL#Cyfra_kontrolna_i_sprawdzanie_poprawno.C5.9Bci_numeru
