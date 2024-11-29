"""
C'est a moi
"""


#### Imports et définition des variables globales
import sys
sys. setrecursionlimit(20000)

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne 
    de caractères passée en argument selon un algorithme 
    itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s :
        return[]
    # votre code ici
    c = [s[0]]
    o = [1]
    k = 1
    while k < len(s):
        if s[k] == s[k-1]:
            o[-1] +=1
        else:
            c.append(s[k])
            o.append(1)
        k +=1

    return list(zip(c, o))


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici

    # cas de base
    if not s:
        return []
    # recherche nombre de caractères identiques au premier
    def r(s, index, char, count, result):
        if index == len(s):
            result.append((char,count))
            return result
        if s[index] == char:
            return r(s, index + 1, char, count + 1, result)
        result.append((char, count))
        return r(s, index+1, s[index], 1, result)
    return r(s, 1, s[0], 1, [])

#### Fonction principale


def main():
    """
    permet de tester les fonctions secondaire
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
