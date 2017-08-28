#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Write a function that calculates mass of an element after decay for provided time.
Mass must be calcuted using half-life formula:
mass = initial_mass * (1/2)^(t/T)

mass 			- output mass [grams]
initial_mass 	- mass of element at begining [grams]
t 				- time of decay [years]
T 				- half-life time [years]

>>> mass_after_decay(10, 15, 5)
1,25
"""


def mass_after_decay(initial_mass, t, T):
    pass


   def mass_after_decay(initial_mass, t, T): 
..   return initial_mass*(1/2**(t/T)) 
..   
   mass_after_decay(10, 15, 5)
=> 1.25   
