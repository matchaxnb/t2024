"""Exercice 1: palindromes

Un palindrome est une chaîne de caractères qui peut être lue de la même façon
de gauche à droite et de droite à gauche, en ignorant les espaces et les accents,
les majuscules etc.

Par exemple, KAYAK est un mot palindrome. CANOË ne l'est pas.

Un exemple de phrase palindrome est: "À l'étape, épate-la !"


1) Écrire un test unitaire pour la fonction palindrome. On ne testera que des simples mots, en majuscules et sans accents.
2) A partir du test unitaire écrit, créer la fonction palindrome

On utilisera la commande `pytest exercice1.py` pour tester.

Rappels:

- en python, on peut itérer sur une chaîne de caractères avec une boucle for
- en python, on peut parcourir une liste à l'envers avec la syntaxe de tranches

Vous pouvez regarder le code des fonctions demo_ pour les rappels utiles.

"""
import pytest


def demo_chaines():
  print("Demo chaines".center(40))
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  for num, caractere in enumerate(alphabet):
    print(f"Caractère {num + 1}: {caractere}")

def demo_liste():
  print("Demo liste".center(40))
  nombres = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 42, 613, 942, -3213, 18, 3.5]
  print("Liste dans l'ordre:", nombres)
  print("Liste à l'envers:", nombres[::-1])
  print("Troisième élément de la liste (indexation à partir de 0):", nombres[2])
  print("Quatrième élément de la liste à l'envers:", nombres[::-1][3])

def test_palindrome():
    with pytest.raises(NotImplementedError):
      print("Test non implémenté")
      palindrome("blabla")

def palindrome(s: str) -> bool:
    raise NotImplementedError("exercice 1.2")

if __name__ == '__main__':
  demo_chaines()
  demo_liste()
