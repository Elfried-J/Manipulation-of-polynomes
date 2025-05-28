# Manipulation-of-polynomes
A python Project i did in cégep 
Présentation du projet – TP1 : Manipulation de polynômes
Réalisé par Jeffrey et Iaris – Créé le 11 octobre 2022

Ce projet Python a été développé dans le cadre du premier travail pratique (TP1) du cours, et porte sur la manipulation de polynômes représentés sous forme de listes. Dans cette représentation, chaque indice de la liste correspond au degré du terme, et chaque valeur représente le coefficient. Par exemple, la liste [1, 2, 3] représente le polynôme 1+2x+3x^2.
Le programme est organisé en plusieurs sections, chacune répondant à une fonctionnalité précise :
Partie A : la fonction normalise supprime les zéros inutiles à la fin du polynôme pour en garder une représentation fidèle et épurée.
Partie B : la fonction degree retourne le degré réel du polynôme, c’est-à-dire le plus haut degré dont le coefficient est non nul.
Partie C : la fonction evalue permet de calculer la valeur numérique du polynôme pour une valeur donnée de 𝑥.
Partie D : polystr génère une version lisible du polynôme sous forme de chaîne de caractères, par exemple "1x^0 + 3x^2".
La Partie E rassemble les fonctions essentielles pour effectuer des opérations algébriques sur les polynômes :
somme pour additionner deux polynômes, difference pour en faire la soustraction,multiple pour multiplier un polynôme par un entier,produit pour faire le produit de deux polynômes,et puissance pour élever un polynôme à une puissance entière 𝑛.
En Partie F, le programme aborde des notions d’analyse :derivee calcule la dérivée du polynôme,
tvm retourne le taux de variation moyen entre deux points,et zeros affiche les racines réelles si le degré du polynôme est 1 ou 2.
Enfin, la fonction run_tests à la fin du script permet de valider le bon fonctionnement de l’ensemble des fonctions à l’aide de tests unitaires basés sur assert. Les racines sont affichées directement avec print, tandis que les autres résultats sont vérifiés automatiquement.

Ce projet n’utilise aucun module externe, ce qui le rend simple à exécuter et à comprendre. Il met en pratique de nombreuses notions fondamentales du cours : manipulation de listes, utilisation des fonctions, conditions, boucles, gestion des cas limites, et tests automatisés.

Pour lancer les tests, il suffit d’exécuter le fichier avec la commande suivante :
