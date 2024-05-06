"""Exercice 3: test de performance

On veut comparer deux méthodes pour calculer une suite de Fibonacci.

Rappel: la suite de Fibonacci est une suite mathématique F définie ainsi:

F(0) = 1
F(1) = 1
pour tout n entier supérieur à 1, F(n) = F(n-2) + F(n-1)

ainsi F(2) = F(0) + F(1) = 2
      F(3) = F(1) + F(2) = 3
      F(4) = F(2) + F(3) = 5
      F(5) = F(3) + F(4) = 8
      ...


La première méthode est l'approche récursive traditionnelle (fonction fibo_r).
La seconde méthode n'utilise pas la récursion mais une boucle (fonction fibo_i).

On souhaite savoir laquelle est la plus rapide en temps processeur.

La première implémentation est garantie comme correcte pour tout nombre entier
positif.

1) Implémenter un test unitaire vérifiant pour tout nombre de la suite F()
jusqu'à F(n) > 23788 que la seconde fonction est correcte aussi. Quel est l'élément?

2) En utilisant la fonction timeit.timeit qui est faite pour mesurer la performance de 
code établir une comparaison de performance sur 1000 itérations entre la fonction fibo_i()
et la fonction fibo_r() jusqu'au nombre trouvé à l'exercice 1.

On testera en utilisant `pytest -rP exercice3.py`. Le test de performance pourra être
exécuté avec `python exercice3.py`.

"""
import timeit
from time import sleep

def fibo_r(n: int) -> int:
  if n == 0:
    return 1
  elif n == 1:
    return 1
  else:
    return fibo_r(n - 2) + fibo_r(n - 1)

def fibo_i(n: int) -> int:
  stack = [1, 1]
  for i in range(2, n+1):
    fib_i = stack[i - 2] + stack[i -1]
    stack.append(fib_i)
  return stack[-1]

def test_if_fibo_i_is_correct():
  raise NotImplementedError("faire l'exercice 1")

def _test_performance():
  raise NotImplementedError("faire l'exercice 2")

# exemple timeit.timeit

def hello(name: str):
  sleep(0.001)
  return f"Hello {name}"

def goodbye(name: str):
  sleep(0.001)
  return f"Goodbye {name}"

def exemple_timeit():
  time_hello = timeit.timeit(lambda: hello("Toto"), number=10000)
  time_goodbye = timeit.timeit(lambda: goodbye("Tutu"), number=10000)
  print("Durée de hello:", time_hello)
  print("Durée de goodbye:", time_goodbye)

if __name__ == '__main__':
  exemple_timeit() # a supprimer pour le rendu
  test_performance()
