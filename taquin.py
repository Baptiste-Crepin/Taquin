# Créé par Crepin Baptiste, le 01/04/2021 en Python 3.7
import random


class Cel():
    
    def __init__(self, name, coordo):
        self.name = name
        self.coordo = coordo

    def getname(self):
        return self.name

    def getcoordo(self):
        return self.coordo
        
    def setcoordo(self, newcord):
        self.coordo = newcord
        
    def fromcoordo(self,coordo):
        if self.coordo == coordo:
            return self
        
    def __repr__(self):
        return str(self.name)
        #return str(self.coordo)


class Grille():

    def __init__(self, width, height):
        """
        >>> g1 = Grille(7,4)
        >>> print(g1)
        []
        >>> g1.creation_grille()
        >>> g1.est_dans_grille((1, 1))
        True
        >>> g1.est_dans_grille((15, 1))
        False
        """
        self.width = width
        self.height = height
        self.zero = None
        self.grille = []

    def __str__(self):
        return str(self.grille)


    def creation_grille(self):
        i = 0
        for ligne in range(2*self.width+1):
            liste = []
            for col in range(2*self.height+1):
                if ligne % 2 == 0:
                    if col % 2 == 0:
                        liste.append("+")
                    else:
                        liste.append("-")
                else:
                    if col % 2 == 0:
                        liste.append("|")
                    else:
                        i+= 1
                        cel = Cel(i,(col//2+ 1, ligne//2+ 1))
                        liste.append(cel)
            self.zero = Cel(i,(col//2, ligne//2))
            self.grille.append(liste)

    def affiche(self):
        for i in self.grille:
            print(i)

    def est_dans_grille(self, coordo):
        isin = False
        for ligne in self.grille:
            for cel in ligne:
                if type(cel) != str:
                    #print(cel.getcoordo())
                    if cel.getcoordo() == coordo:
                        isin = True
        return isin


    def mouvement_possible(self):
        x,y = self.zero.getcoordo()
        #print(self.zero.getcoordo())
        mvt_possibles = {}
        if self.est_dans_grille((x-1, y)):
            mvt_possibles['LEFT'] = (x-1, y)
        if self.est_dans_grille((x+1, y)):
            mvt_possibles['RIGHT'] = (x+1, y)
        if self.est_dans_grille((x, y-1)):
            mvt_possibles['UP'] = (x, y-1)
        if self.est_dans_grille((x, y+1)):
            mvt_possibles['DOWN'] = (x, y+1)
        #print(mvt_possibles)
        return mvt_possibles


    def mouvement(self, point):
        if self.est_dans_grille(point):
            for ligne in self.grille:
                for cel in ligne:
                    if type(cel) != str:
                        other_cel_temp = cel.fromcoordo(point)
                        if other_cel_temp != None:
                            other_cel = other_cel_temp
                            #print(other_cel)
            #print(self.zero.coordo)
            x, y = self.zero.coordo
            self.grille[y*2-1][x*2-1]= other_cel
            x1, y1 = other_cel.coordo
            #print("o",other_cel.getcoordo())
            temp = other_cel.getcoordo()
            other_cel.setcoordo(self.zero.getcoordo())
            #print("z",self.zero.getcoordo())
            self.grille[y1*2-1][x1*2-1]= self.zero
            self.zero.setcoordo(temp)
            #print("nz", self.zero.getcoordo())
            #print(self.zero.getcoordo())


    def melange(self, n):
        for i in range(n):
            case = random.choice(list(self.mouvement_possible().values()))
            self.mouvement(case)

    def place_en_bas_a_droite(self):
        x, y = self.zero.getcoordo()
        while x != self.height:
            x, y = self.zero.getcoordo()
            if x < self.height:
                self.mouvement(self.mouvement_possible()['RIGHT'])
        while y < self.width:
            x, y = self.zero.getcoordo()
            if y < self.width:
                self.mouvement(self.mouvement_possible()['DOWN'])

    def est_dans_l_ordre(self):
        actual_cel = 0
        for ligne in self.grille:
            for cel in ligne:
                if type(cel) != str:
                    #print(cel)
                    if cel.getname() > actual_cel:
                        pass
                    else:
                        return False
                    actual_cel = cel.getname()
        return True
                    

"""
g1 = Grille(7,4)
g1.creation_grille()
#g1.affiche()
#print(g1.est_dans_grille((3, 7)))
#print(g1.mouvement_possible())
g1.mouvement((4,6))
g1.affiche()
print('\n')
g1.mouvement((4,5))
g1.affiche()
print('\n')
g1.mouvement((4,6))
g1.affiche()
g1.melange(150)
#g1.affiche()
#g1.place_en_bas_a_droite()
#g1.affiche()
g1.est_dans_l_ordre()
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)

