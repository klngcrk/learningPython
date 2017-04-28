#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys 
import io

s = sys.stdout
stream = io.StringIO()
sys.stdout = stream

try:
	import undefined_variable
except NameError:
	sys.stdout = s
	print('Kod dalej zwraca ten sam błąd: NameError.')
	sys.exit(0)
except Exception:
	sys.stdout = s
	print('Dodano nowy błąd do kodu, kod należy poprawiać, a nie psuć bardziej :-)')
	sys.exit(0)

sys.stdout = s
received = stream.getvalue()

expected = '4'
assert  expected in received, "Oczekiwano tekstu zawierajacego\n'{}'\n, a otrzymano:\n'{}'".format(expected,  received if received else 'Pusty tekst')
print("Success!")