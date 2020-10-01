#!/usr/bin/env python
# -*- coding: utf-8 -*-


from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    return { some_list[i] : i for i in range(len(some_list)) }


def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
    return [ ( colors[i] , cnames[ colors[i] ] ) for i in range(len(colors)) ]


def odd_integer_for_loop(end: int) -> list:
    odd_integer = list()

    for i in range(end) :
        if i % 2 != 0 :
            odd_integer.append(i)

    return odd_integer


def odd_integer_list_comprehension(end: int) -> list:
    return [ i for i in range(end) if i % 2 != 0 ]


def loop_traversal(integers: list) -> None:

    for i in range(len(integers)) :
        print(f"Indice -> {i} , element -> {integers[i]}")


def Upper(string) :
    # Renvoie la premiere lettre en majuscule s'il se trouve sinon la premiere lettre de mot
    found , i = False , 0
    while i < len(string) and found == False :
        if string[i].isupper() :
            letter = string[i]
            found = True
        i += 1
    if found == True : 
        return letter
    else :
        return string[0] 


def word_dict_for_loop(words : list) -> dict:
    d = dict()

    for word in range(len(words)) :
        d[Upper(words[word])] = words[word]

    return d


def word_dict_comprehension(words : list) -> dict:
    return { Upper(words[i]) : words[i] for i in range(len(words)) }


def dictionary_traversal(words: dict) -> None:
    # afficher les elements on ordre alphabetique par valeur de dictionnaire
    l = [sorted(words.values())]
    for word in l :
        print(word)
        for k , v in enumerate(words) :
            if v == word :
                print(f"({k} , {word})")


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    integer = 13
    integers_for = odd_integer_for_loop(integer)
    print(f"Liste avec boucle for et le nombre 13: {integers_for}")
    integers_comprehension = odd_integer_list_comprehension(integer)
    print(f"Liste avec list comprehension et le nombre 13: {integers_comprehension}")
    print(f"Les 2 listes sont-elles identiques? {integers_for == integers_comprehension}")

    print(f"Parcours d'une des 2 listes...")
    loop_traversal(integers_for)

    words = ["initiAlisation", "ajOut", "modification", "suppression", "diCtionnaire"]
    words_for = word_dict_for_loop(words)
    print(f"Dictionnaire avec la boucle for: {words_for}")
    words_comprehension = word_dict_comprehension(words)
    print(f"Dictionnaire avec le dictionary comprehension: {words_comprehension}")

    print(f"Les 2 dictionnaires sont-ils identiques? {words_for == words_comprehension}")
    print(f"Parcours d'un des 2 dictionnaires...")

    words = ["initiAlisation", "ajOut", "modification", "suppression", "diCtionnaire"]
    words_comprehension = word_dict_comprehension(words)
    dictionary_traversal(words_comprehension)


if __name__ == '__main__':
    main()
