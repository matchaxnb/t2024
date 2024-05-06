"""Exercice 2: conversion de chaînes de caractères en nombres

La fonction convert_float(s: str) -> float convertit une chaîne de caractères
en nombre à virgule.

La fonction convert_int(s: str) -> int convertit une cha6ine de caractères en
nombre entier.

Au cas où la chaîne fournie n'est pas un nombre valide, ou au cas où l'argument
fourni n'est pas une chaîne de caractère, ces fonctions doivent lever l'exception
BadNumber().

1) Écrire deux tests unitaires, un pour convert_float et un pour convert_int.
Les tests unitaires doivent couvrir les cas limites (chaîne de caractère invalide,
pas une chaîne de caractère...)
2) Corriger tout ce qui doit l'être dans convert_float et convert_int pour satisfaire
les contraintes posées.

Les deux fonctions doivent gérer les nombres en notation scientifique
(Ne^M, avec 0 < N < 10 et M entier quelconque) 
 0.31416e1 == 3.1416
 31416.0e-4 == 3.1416
et en notation exposant "E"
  1.5E3 == 1500

Une chaîne de caractères contenant des informations non-numériques est invalide.

On testera avec la commande `pytest exercice2.py`

Rappel: on peut utiliser pytest.raises pour vérifier qu'une exception a été levée. Voir l'exemple.
"""
import math
import pytest
def exemple_pytest_raises():
  with pytest.raises(ValueError):
    raise ValueError("exemple")

class BadNumber(Exception):
  pass

def convert_float(s: str) -> float:
  return float(s)

def convert_int(s: str) -> int:
  return math.floor(convert_float(s))
