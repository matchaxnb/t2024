"""Exercice 4: test avec des données externes

On veut réaliser une fonction qui prend en argument l'adresse
d'une page Web et renvoie le titre de la page et, le cas échéant,
le lien vers son flux de syndication RSS.

Un lien vers un flux RSS est:
- un élément HTML <link>
- avec l'une de ses propriétés rel définie à "alternate" (on peut avoir plusieurs "rel" sur un même élément)
- et la propriété type=application/rss+xml

On pourra utiliser la bibliothèque BeautifulSoup à installer avec la commande
pip install bs4
ainsi que la bibliothèque requests pour faire des requêtes http à installer avec
pip install requests

1) Écrire un test unitaire utilisant le site gameblog.fr et vérifiant que le titre contient bien la chaîne "Gameblog.fr"

2) Réaliser le test unitaire de la fonctionnalité d'extraction RSS.

3) Réaliser la fonction de recherche du lien RSS et du titre.
"""
from bs4 import BeautifulSoup
import requests

def test_gameblog():
    assert False

def get_web_page_infos() -> [str, str]:
    raise NotImplementedError("faire l'exercice")


def exemple_demo_beautifulsoup():
   kernel_org_homepage = requests.get('http://kernel.org', allow_redirects=True)
   contents = BeautifulSoup(kernel_org_homepage.text, 'html.parser')
   resources_on_page = contents.find_all('link')
   for resource in resources_on_page:
     # on affiche l'attribut "href" qui indique le lien à suivre vers la ressource
     resource_type = resource.get('type')
     resource_rel = ','.join(resource.get('rel'))
     resource_target = resource.get('href')
     print(f"Ressource de type {resource_type} avec rel = {resource_rel} et cible {resource_target}")

if __name__ == '__main__':
  exemple_demo_beautifulsoup()
