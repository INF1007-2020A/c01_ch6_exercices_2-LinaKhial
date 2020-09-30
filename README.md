[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect-0.herokuapp.com/)

# Exercices en vrac (chapitre 6.2)

Avant de commencer, consultez les instructions à suivre dans [instructions.md](instructions.md)

## Objectifs

Compléter les quelques exercices suivants en modifiant le code de [exercice.py](exercice.py):

1. Écrire un programme qui transforme une liste en dictionnaire. Les éléments de la liste deviennent les clés du dictionnaire et les indexes de chaque élément deviennent la valeur associée à chaque clé.
2. Écrire un programme qui trouve la valeur hex de chaque couleur d'une liste et crée une liste de tuples où le premier élément est le nom de la couleur et le deuxième est la valeur hex.
3. a) Avec une boucle for, écrire un programme qui crée une liste des entiers impairs de 1 à un nombre donné.
   b) Même chose que a), mais avec une list comprehension.
   c) Parcourir la liste obtenue en a) ou en b) et afficher les éléments ainsi que leur index, sans déclarer de variable à l'extérieur de la boucle.
4. a) Avec une boucle for, écrire un programme qui crée un dictionnaire dont les valeurs sont des mots donnés et  dont les clefs sont les premières lettre mises en majuscules de ces mots.
   b) Même chose que a), mais avec un dictionary comprehension.
   c) Parcourir le dictionnaire obtenu en a) ou en b) et afficher les éléments ainsi que leur index en ordre alphabétique, sans déclarer de variable à l'extérieur de la boucle.

### À compléter
Vous devez compléter les fonctions suivantes du fichier [exercice.py](exercice.py).

```python
def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs

    return {}

def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex

    return []

def odd_integer_for_loop(end: int) -> list:
    return []

def odd_integer_list_comprehension(end: int) -> list:
    return []

def loop_traversal(integers: list) -> None:
    pass

def word_dict_for_loop() -> dict:
    return {}

def word_dict_comprehension() -> dict:
    return {}

def dictionary_traversal(words: dict) -> None:
    pass
```
