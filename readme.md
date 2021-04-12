---
title: Réalisation d'un Taquin en pygame
---

![Jeu du Taquin](480px-15-puzzle.svg.png)

# Classe grille

On souhaite implémenter une classe `grille` pour gérer une grille de `i` 
lignes et de `j` colonne :

~~~python
+----+----+----+----+
| 1  | 2  | 3  | 4  |
+----+----+----+----+
| 5  | 6  | 7  | 8  |
+----+----+----+----+
| 9  | 10 | 11 | 12 |
+----+----+----+----+
| 13 | 14 | 15 | 16 |
+----+----+----+----+
~~~

1. ![Q] Créer l'initialisateur de la classe qui prend en paramètre
la largeur de la grille `width` et sa hauteur `height` et qui crée les
attributs :
    - `width`
    - `height`
    - `zero` initialisé par le tuple de la case en bas à droite
    - `grille` : liste des valeurs de la grille

2. ![Q] Créer la méthode `__str__` pour réaliser l'affichage

3. ![Q] Implémenter la méthode `est_dans_grille` qui prend en argument 
sous forme de `tuple` les coordonnées d'une case est renvoie `True`
si la case est dans la grille et `False` sinon.

4. ![Q] Implémenter à l'aide de la méthode précédente, la méthode
`mouvement_possible` qui renvoie un dictionnaire ayant pour clés les 
directions `UP`, `DOWN`, `LEFT` et `RIGHT` et pour valeurs les coordonnées
des cases accessibles en partant de la case `zero`. Exemple pour la case 
`(1, 2)`

    ~~~python
    {'LEFT': (0, 2), 'RIGHT': (2, 2), 'UP': (1, 1), 'DOWN': (1, 3)}
    ~~~

5. ![Q] Implémenter la méthode `mouvement` qui prend en argument un `point`
et échange la case `zero` est la case de coordonnée `point` 

6. ![Q] Implémenter la méthode `melange` qui prend en argument un entier 
`n`. Pour chaque valeur de `n`, choisir aléatoirement une case parmi la liste
des mouvements possibles et réaliser le mouvement. On pourras, pour choisir
un déplacement aléatoire utiliser l'instruction

    ~~~python
    case = random.choice(list(self.mouvement_possible().values()))
    ~~~

7. ![Q] Implémenter la méthode `place_en_bas_a_droite()` qui effectue
les mouvements nécessaires pour placer la case `zero` en bas à droite.

1. ![Q] Implémenter la méthode `est_dans_l_ordre` qui renvoie `True` si 
la grille est dans l'ordre et `False` sinon


~~~python
>>> g=Grille(3, 3)
>>> g
+----+----+----+
| 1  | 2  | 3  |
+----+----+----+
| 4  | 5  | 6  |
+----+----+----+
| 7  | 8  | 9  |
+----+----+----+
>>> g.mouvement_possible()
{'LEFT': (1, 2), 'UP': (2, 1)}
>>> g.mouvement_possible().values()
dict_values([(1, 2), (2, 1)])
>>> list(g.mouvement_possible().values())
[(1, 2), (2, 1)]
>>> random.choice(list(g.mouvement_possible().values()))
(2, 1)
>>> g.mouvement((2, 1))
>>> g
+----+----+----+
| 1  | 2  | 3  |
+----+----+----+
| 4  | 5  | 9  |
+----+----+----+
| 7  | 8  | 6  |
+----+----+----+
>>> list(g.mouvement_possible().values())
[(1, 1), (2, 0), (2, 2)]
>>> random.choice(list(g.mouvement_possible().values()))
(1, 1)
>>> g.mouvement((1, 1))
>>> g
+----+----+----+
| 1  | 2  | 3  |
+----+----+----+
| 4  | 9  | 5  |
+----+----+----+
| 7  | 8  | 6  |
+----+----+----+
>>> list(g.mouvement_possible().values())
[(0, 1), (2, 1), (1, 0), (1, 2)]
>>> g.zero
(1, 1)
>>> g.melange(1000)
>>> g
+----+----+----+
| 9  | 8  | 2  |
+----+----+----+
| 5  | 4  | 6  |
+----+----+----+
| 3  | 1  | 7  |
+----+----+----+
>>> g.place_en_bas_droite()
>>> g
+----+----+----+
| 8  | 2  | 6  |
+----+----+----+
| 5  | 4  | 7  |
+----+----+----+
| 3  | 1  | 9  |
+----+----+----+

~~~

# Pygame et les images

## Affichage

Pour afficher une image contenue dans le fichier `image1.png` avec pygame 
on peut utiliser :

~~~python
img = pygame.image.load('image1.png')
screen.blit(img, (0,0)) # affiche img en (0,0)
~~~

1. ![Q] Chercher une image libre de droit et éventuellement la modifier 
pour avoir une résolution `800x800`
1. ![Q] Réaliser le programme pygame pour afficher cette image "entièrement"

## Découpage

Pygame possède la méthode `subsurface` qui permet de "découper" un rectangle
dans l'image. Cette méthode prend en paramètre un objet de type `Rect`

Par exemple si on souhaite découper l'image en (200, 400) avec une taille
de (100, 100)

~~~python
rect = pygame.Rect(200, 400, 100, 100)
screen.blit(img.subsurface(rect), (0,0))
~~~

1. ![Q] Réaliser le programme pygame qui affiche une partie de l'image

# Réalisation du jeu

Vous avez tous les éléments nécessaires pour réaliser le jeu dit du `Taquin`

Je vous recommande :

- Utiliser la classe grille pour générer une grille 
- Générer une liste qui contient les morceaux d'image découpées selon
les caractéristiques de la grille
- Modifier cette liste pour placer en dernier élément une simple surface
(pygame.Surface())
- Réaliser la fonction `affiche` qui prend la valeur `n` contenu dans la grille
 et affiche la `n` ieme image
- Vérifier que l'image s'affiche dans "l'ordre" avec un carré noir en bas à droite.
- Utiliser les méthodes `melange` et `place_en_bas_a_droite` de la grille
pour mélanger le jeu
- Gérer les touches `UP`, `DOWN`, `LEFT` et `RIGHT` pour les déplacements
- Enfin utiliser la méthode `est_dans_l_ordre` pour tester la fin du jeu
- On pourra éventuellement simplifier le jeu en affichant l'entier `n` 
comme sur la figure d'introduction

 


[Q]: gears.png
