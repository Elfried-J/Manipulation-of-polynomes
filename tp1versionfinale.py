# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 09:55:24 2022
@author: 2230701
Coéquipiers: Jeffrey et Iaris
"""

# TP 1 – Manipulation de polynômes

# Partie A

def normalise(poly):
    """Retourne une liste normalisée représentant un polynôme."""
    normalised = poly.copy()
    while normalised and normalised[-1] == 0:
        normalised.pop()
    return normalised


# Partie B

def degree(poly):
    """Retourne le degré du polynôme."""
    return len(normalise(poly)) - 1


# Partie C

def evalue(poly, a):
    """Évalue le polynôme au point x = a."""
    return sum(coef * (a ** i) for i, coef in enumerate(normalise(poly)))


# Partie D

def polystr(poly):
    """Retourne une chaîne représentant le polynôme en notation standard."""
    poly = normalise(poly)
    terms = []
    for i, coef in enumerate(poly):
        if coef != 0:
            terms.append(f"{coef}x^{i}")
    return " + ".join(terms)


# Partie E

def somme(p1, p2):
    """Retourne la somme de deux polynômes: p1 + p2."""
    Np1, Np2 = normalise(p1), normalise(p2)
    max_len = max(len(Np1), len(Np2))
    result = []
    for i in range(max_len):
        val1 = Np1[i] if i < len(Np1) else 0
        val2 = Np2[i] if i < len(Np2) else 0
        result.append(val1 + val2)
    return normalise(result)


def multiple(n, poly):
    """Retourne le produit du polynôme par l'entier n."""
    return normalise([coef * n for coef in normalise(poly)])

def difference(p1, p2):
    """Retourne la différence de deux polynômes: p1 - p2."""
    return somme(p1, multiple(-1, p2))


def produit(p1, p2):
    """Retourne le produit de deux polynômes: p1 * p2."""
    Np1, Np2 = normalise(p1), normalise(p2)
    result = [0] * (len(Np1) + len(Np2) - 1)
    for i in range(len(Np1)):
        for j in range(len(Np2)):
            result[i + j] += Np1[i] * Np2[j]
    return normalise(result)


def puissance(n, poly):
    """Retourne la puissance n-ième du polynôme."""
    result = poly.copy()
    for _ in range(n - 1):
        result = produit(result, poly)
    return result


# Partie F

def derivee(poly):
    """Retourne la dérivée du polynôme."""
    poly = normalise(poly)
    return [i * poly[i] for i in range(1, len(poly))]


def tvm(poly, a, b):
    """Retourne le taux de variation moyen du polynôme entre x=a et x=b."""
    return (evalue(poly, b) - evalue(poly, a)) / (b - a)


def zeros(poly):
    """Affiche les zéros du polynôme s'il s'agit d'un polynôme de degré 1 ou 2."""
    poly = normalise(poly)
    deg = degree(poly)

    if deg == 1:
        c, b = poly[0], poly[1]
        zero = -c / b
        print(f"Le zéro de la fonction {polystr(poly)} est {zero}")

    elif deg == 2:
        c, b, a = poly[0], poly[1], poly[2]
        discriminant = b ** 2 - 4 * a * c

        if discriminant > 0:
            zero1 = (-b + discriminant ** 0.5) / (2 * a)
            zero2 = (-b - discriminant ** 0.5) / (2 * a)
            print(f"Les zéros de la fonction {polystr(poly)} sont {zero1} et {zero2}")
        elif discriminant == 0:
            zero = -b / (2 * a)
            print(f"Le zéro de la fonction {polystr(poly)} est {zero}")
        else:
            print("Il n'y a pas de zéros réels.")

    else:
        print("Je ne peux pas trouver les zéros pour les polynômes de degré > 2.")


def run_tests():
    # Test normalise
    assert normalise([1, 2, 0, 0]) == [1, 2]
    assert normalise([0, 0, 0]) == []
    assert normalise([]) == []

    # Test degree
    assert degree([1, 2, 0, 0]) == 1
    assert degree([0, 0, 3]) == 2
    assert degree([]) == -1

    # Test evalue
    assert evalue([1, 2, 3], 0) == 1
    assert evalue([1, 2, 3], 1) == 6
    assert evalue([1, 2, 3], 2) == 17

    # Test polystr
    assert polystr([1, 0, 3]) == "1x^0 + 3x^2"
    assert polystr([0, 0, 0]) == ""
    assert polystr([5]) == "5x^0"

    # Test somme
    assert somme([1, 2], [3, 4]) == [4, 6]
    assert somme([1], [1, 2, 3]) == [2, 2, 3]

    # Test multiple
    assert multiple(2, [1, 2, 3]) == [2, 4, 6]
    assert multiple(0, [1, 2, 3]) == []

    # Test difference
    assert difference([5, 3], [2, 1]) == [3, 2]
    assert difference([1], [1, 1]) == [0, -1]

    # Test produit
    assert produit([1, 1], [1, 1]) == [1, 2, 1]  # (x+1)^2
    assert produit([2], [3, 0, 1]) == [6, 0, 2]

    # Test puissance
    assert puissance(2, [1, 1]) == [1, 2, 1]
    assert puissance(3, [1]) == [1]

    # Test derivee
    assert derivee([1, 2, 3]) == [2, 6]  # Derivative of 1 + 2x + 3x^2
    assert derivee([0, 0, 5]) == [0, 10]
    assert derivee([10]) == []

    # Test tvm
    assert tvm([1, 2], 0, 1) == 2  # fonction lineaire
    assert round(tvm([1, 0, 1], 0, 2), 2) == 2.0  # f(x) = 1 + x^2 → (5 - 1)/(2 - 0)

    # Test zeros
    print("Testing zeros:")
    zeros([1, -3])
    zeros([1, 0, -4])
    zeros([1, 0, 4])
    zeros([1, 2, 1])
    zeros([1])
run_tests()
