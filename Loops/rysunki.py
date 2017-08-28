#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 Zadanie są o podwyższonym poziomie trudności.

 Zadanie należy wykonąć z użyciem pętli for.
 Rozmiary figur powinny być parmatryzowane, przykład.:
    Wielkość trójkąta w zadaniu 2, powinna być możliwa do zmienienia,
    i tak trójkąt o wielkości 3, powinien wyglądać tak:
    O
    OO
    OOO
'''

# 1. Napisz program wypisujący 17 gwiazdek (znak '*')
   for i in '*': 
..   print(i*17) 
..   
*****************


# 2. | Napisz program wypisujący wieżę z liter 'O':
#    | Oczekiwany wynik:
'''
O
OO
OOO
OOOO
OOOOO
'''
   x = '00000'
   while x: 
..   print(x, end='\n') 
..   x = x[1:] 
..   
00000
0000
000
00
0


# 3. Napisz program wypisujący prostokąt z liter 'X'. Oczekiwany wynik:
'''
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
'''
x = 'X'
   for i in (x*4): 
..   print(i*10, end='\n') 
..   
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
   

# 4. Napisz program wypisujący trójkąt z liter 'X'. Oczekiwany wynik:
'''
    X
   XXX
  XXXXX
 XXXXXXX
XXXXXXXXX
'''

# 5. Napisz program wypisujący kwadrat z liter 'K': Oczekiwany wynik:
'''
KKKK
KKKK
KKKK
KKKK
'''
x = 'KKKK'
 for i in x: 
..   print(i*4, end='\n') 
..   
KKKK
KKKK
KKKK
KKKK
