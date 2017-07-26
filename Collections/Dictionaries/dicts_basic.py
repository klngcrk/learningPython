"""
Odpowiedzi na zadania umieszaj bezpośrednio pod poleceniem.
Zadania z gwiazdką są opcjonalne. Są to rzadko spotykane operacje w codziennej pracy.
Zadania z podwója gwiazdką są trudne i również są opcjonalne.
"""

1. Napisz program dodający do słownika nowy klucz (dowolna warość).
   D = {'perindoprilum':2, 'simvastatinum':1}
   D['atenololum'] = 2
   D
=> {'perindoprilum': 2, 'simvastatinum': 1, 'atenololum': 2}   

2. Napisz program wypisujący wartość ze słownika dla podanego klucza.
   D = {'perindoprilum':2, 'simvastatinum':1}
 D['simvastatinum']
=> 1

3. Napisz program wypisujący wartość ze słownika dla podanego klucza. Jeżeli klucz nie istnieje w słowniku, program nie zwróci błędu KeyError.
 D = {'perindolpilum':2, 'simvastatinum':1, 'atenololum':2}
 D.get('morfini', 0)
=>0   

4. Napisz program wypisujący wartość ze słownika dla podanego klucza. Jeżeli klucz nie istnieje w słowniku, program zwróci: None
	D = {'perindoprilum':2, 'simvastatinum':1}
print (D.get('morfini'))
None

5. Napisz program usuwający klucz ze słownika.
D = {'perindoprilum': 2, 'simvastatinum': 1, 'atenololum': 2}   
 del D['atenololum']
   D
=> {'perindoprilum': 2, 'simvastatinum': 1}   

6. Napisz program usuwający klucz ze słownika, pod warunkiem, że klucz w słowniku istnieje. 
   D = {'morfini':2, 'codeini':4, 'fentanyl':8}
   if 'key' in D: 
..   D.pop('key') 
..   print (D)     nie wychodzi mi w tym zapisie, myslałam o del ale jest 'pod warunkiem'. z del to prościzna 

del D['codeini']
D
=> {'morfini':2, 'fentanyl':8}

Zrobiłam cos takiego, niby wyszło ale jednocześnie wyskoczył bład :-(
	
D = {'morfini':2, 'codeini':3}
   for i in D: 
..   del D[i] 
..   print (D) 
.. print ('morfini')  
{'codeini': 3}
Traceback (most recent call last):
  File "python", line 1, in <module>
RuntimeError: dictionary changed size during iteration
	

7. Napisz program usuwający klucz ze słownika. Jeżeli klucz nie istnieje, program zwróci stringa 'Klucz nie istnieje w tym słowniku'.
D = {'perindoprilum': 2, 'simvastatinum': 1, 'atenololum': 2}
D.pop('morfini', 'KLucz nie istnieje w tym słowniku')
=> 'KLucz nie istnieje w tym słowniku'   

8. Napisz program usuwający wszystkie klucze ze słownika.

   D = {'atropini':2, 'fentanyl':4, 'morfini':6}
   D.clear()
   D
=> {}   

9. Napisz program wypisujący wszyskie klucze ze słownika.
   D = {'perindoprilum':2, 'simvastatinum':1,'atenololum':2, 'nilogrinum':3}
   D.keys()
=> dict_keys(['perindoprilum', 'simvastatinum', 'atenololum', 'nilogrinum'])   
or
   list(D.keys())
=> ['perindolpilum', 'simvastatinum', 'atenololum', 'nilogrinum']   

10. Napisz program wypisujący wszystkie wartości ze słownika.
D = {'perindoprilum':2, 'simvastatinum':1,'atenololum':2, 'nilogrinum':3}
D.values()
=> dict_values([2, 1, 2, 3])   

11. Napisz program dodający do istniejącego słownika, drugi słownik.
 D1 = {'morfini':1, 'codeini':4, 'fentanyl':5}
 D = {'perindolpilum':2, 'simvastatinum':1, 'atenololum':2}
   D.update(D1)
   D
=> {'perindolpilum': 2, 'simvastatinum': 1, 'atenololum': 2, 'morfini': 1, 'codeini': 4, 'fentanyl': 5}

12. Napisz program wypisujący minimalną oraz maksymalną wartość ze słownika.
D = {'perindolpilum': 2, 'simvastatinum': 1, 'atenololum': 2, 'morfini': 1, 'codeini': 4, 'fentanyl': 5}
max(D.values())
=> 5   
min(D.values())
=> 1

13. Napisz program przechodzący zwracający iloczyn wartości słownika. 


13.** Napisz program tworzący słownik z dwóch list, pierwsza lista reprezentuje klucze, druga wartości. Należy zachować kolejność list,
	 pierwszy klucz odpowiada pierwszej wartości itd. 
a = ['cukrzyca', 'nadcisnienie', 'impotencja']
b = ['siofor', 'nebiwolum', 'sildenafil']
D = dict(zip((a), (b)))
D
=> {'cukrzyca': 'siofor', 'nadcisnienie': 'nebiwolum', 'impotencja': 'sildenafil'}
