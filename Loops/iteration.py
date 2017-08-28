#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

  (\,/)
  oo   '''//,        _
,/_;~,        \,    / '
"'   \    (    \    !
      ',|  \    |__.'
      '~  '~----''
Write a function that compares masses of the laboratory rats.
Masess of 2 rats are stored in two lists. Each list relates to each rat.
Every rat was weighted once a day. Each element in list is result of that measurement.
Elements in list are sorted chronogically.
Functiion should print day number when second rat was heavier than first one.

"""
rat_1_mass = [125, 123, 129, 130, 130, 130, 128, 125, 123, 122]
rat_2_mass = [125, 126, 126, 123, 124, 126, 128, 130, 130, 130]


def mass_compare():
    pass
input
clear

   rat_1_mass = [124, 123, 129, 130, 130, 128, 125, 123, 122]
   rat_2_mass = [125, 126, 126, 123, 124, 126, 128, 130, 130]
    
   X = list(zip(rat_1_mass, rat_2_mass))
   X
=> [(124, 125), (123, 126), (129, 126), (130, 123), (130, 124), (128, 126), (125, 128), (123, 130), (122, 130)]
  for i in X: 
..     a, b = i 
..     if b >a: 
..       print(i) 
..       
(124, 125)
(123, 126)
(125, 128)
(123, 130)
(122, 130)  
