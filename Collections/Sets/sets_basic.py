"""
Odpowiedzi na zadania umieszaj bezpośrednio pod poleceniem.
Zadania z gwiazdką są opcjonalne. Są to rzadko spotykane operacje w codziennej pracy.
Zadania z podwója gwiazdką są trudne i również są opcjonalne.
"""

1. Napisz program tworzący nowy set z jednym element oraz drugi pusty set.
set()

set([3])
=> {3}

2. Napisz program wypisujący wszystkie elementy setu.

S = {4,5,6}
for i in S:
  print (i)
  4
  5
  6

3. Napisz program dodający do setu dwa różne stringi.

S =set()
S.add('asd')
S
{'asd'}
S.add('ZXC')
S
{'asd', 'ZXC'}

4. Napisz program usuwający element z setu.

S = {1, 2, 7, 'M', 'k'}
S - {2, 'k'}
{1, 'M', 7}

5. Napisz program usuwający element z setu, pod warunkiem, że jest element istnieje w secie.
   S = {123,345, 45}
   x = 45
   if x in S:
    S.remove(x)
    print (x)
  
6. Napisz program wypisujący elementy wspólne dwóch setów.
S = {1, 2, 7, 'M', 'k'}
S1 = {7, 'M'}
S & S1
=> {'M', 7}

7*. Napisz program wypisujący różnicę setów (elementy obecne w secie A, których nie ma w secie B)
  S = {'A', 'S', 'A', 'P', 9, 9}
   S1 = {'N', 'O', 'A', 'S', 'A', 'P'}
   S - S1
=> {9}   (set nie powtarza elementów dlatego wypisał jedna 9)
S1 - S
=> {'O', 'N'}   

8*. Napisz program wypisujący wartość maksymalną oraz minimalną z setu.
  S = {1, 2, 3}
  max(S)
  => 3
 min(S)
=> 1   

