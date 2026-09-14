from array2D import slice_me

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

family2 = [[1.80, 78.4],
           [2.15, 102.7],
           [2.10, 98.5],
           [4.14, 9],
           [22.31, -45],
           [1.88, 75.2]]

print(slice_me(family2, 0, 2))
print(slice_me(family2, 1, -2))


family3 = []
print(slice_me(family3, 1, 5))


'''
  Ce qui pose problème dans array2D.py : la logique de slicing est juste, mais il n'y a aucune gestion d'erreur, alors que
  le sujet demande de vérifier les entrées. J'ai testé quelques cas hors de tester.py :

  - Lignes de tailles différentes comme [[1, 2], [3]] : numpy lève une ValueError non attrapée, donc traceback brut.
  - Types mélangés comme [[1, 2], [3, 'a']] : numpy convertit tout en chaînes silencieusement et renvoie [['1', '2']].
    Aucune erreur, résultat faux.
  - Pas une liste comme une chaîne ou un entier : le shape affiché est () puis IndexError non attrapée.
  - start ou end non entier : TypeError non attrapée.
  - Liste vide : le shape affiché est (0,) au lieu d'un message d'erreur. Selon la lecture du sujet, ce n'est pas vraiment
    un tableau 2D.

  Ce que je recommande : avant l'appel à numpy, vérifier que l'argument est une liste non vide, que chaque élément est une
  liste, que toutes les lignes ont la même longueur et que start et end sont des int. En cas de problème, afficher un
  message et retourner une liste vide plutôt que de laisser remonter l'exception. Le commentaire "temporaire" sur l'import
  numpy peut partir : c'est bien la bibliothèque prévue par le requirements.txt et c'est elle qui donne le .shape.
'''
