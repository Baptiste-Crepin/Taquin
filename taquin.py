# Créé par Crepin Baptiste, le 01/04/2021 en Python 3.7
import random
import pygame

class Cel():
    
    def __init__(self, name, coordo, img=None):
        self.name = name
        self.coordo = coordo
        self.img = img
        
    def setcoordo(self, newcord):
        self.coordo = newcord
        
    def setimg(self, newimg):
        self.img = newimg
        
    def fromcoordo(self,coordo):
        if self.coordo == coordo:
            return self

    def fromname(self,name):
        if self.name == name:
            return self
        
    def __repr__(self):
        return str(self.name)


class Grille():

    def __init__(self, width = 4, height = 4):
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
                        #print(cel, cel.coordo, cel.img)
                        liste.append(cel)
                        #screen.blit(cel.img, (0, 0))
            self.zero = Cel(i,(col//2, ligne//2), pygame.Surface((200, 200)))
            self.grille.append(liste)
            


    def couper_photo(self):
        x = y = 0
        largeur_carré = width//self.width
        hauteur_carré = height//self.height
        for ligne in self.grille:
            for cel in ligne:
                if type(cel) != str:
                    #if cel != self.zero:
                    #print(cel)
                    if x == width:
                        x = 0
                        y += hauteur_carré
                    rect = pygame.Rect(x, y, largeur_carré, hauteur_carré)
                    cel.setimg(img.subsurface(rect))
                    x += largeur_carré
                    #self.zero.setimg(img.subsurface(rect))


    def affiche(self):
        y = 0
        for ligne in self.grille:
            x = 0
            #print(ligne)
            for cel in ligne:
                if type(cel) != str:
                    #print(cel, cel.coordo, cel.img)
                    screen.blit(cel.img, (x, y))
                    x+= width//self.width
                    #print(x)
            for car in ligne:
                if type(car) != str:
                    #print('car',car)
                    #print("y",y)
                    y+= 200//self.height


    def est_dans_grille(self, coordo):
        isin = False
        for ligne in self.grille:
            for cel in ligne:
                if type(cel) != str:
                    #print(cel.coordo)
                    if cel.coordo == coordo:
                        isin = True
        return isin


    def mouvement_possible(self):
        x,y = self.zero.coordo
        #print(self.zero.coordo)
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
            x, y = self.zero.coordo
            self.grille[y*2-1][x*2-1]= other_cel
            x1, y1 = other_cel.coordo
            temp = other_cel.coordo
            other_cel.setcoordo(self.zero.coordo)
            self.grille[y1*2-1][x1*2-1]= self.zero
            self.zero.setcoordo(temp)


    def melange(self, n=1):
        for i in range(n):
            case = random.choice(list(self.mouvement_possible().values()))
            self.mouvement(case)

    def place_en_bas_a_droite(self):
        x, y = self.zero.coordo
        while x != self.height:
            x, y = self.zero.coordo
            if x < self.height:
                self.mouvement(self.mouvement_possible()['RIGHT'])
        while y < self.width:
            x, y = self.zero.coordo
            if y < self.width:
                self.mouvement(self.mouvement_possible()['DOWN'])

    def est_dans_l_ordre(self):
        actual_cel = 0
        for ligne in self.grille:
            for cel in ligne:
                if type(cel) != str:
                    #print(cel)
                    if not cel.name > actual_cel:
                        return False
                    actual_cel = cel.name
        return True
        



width = height= 800
pygame.init()
screen = pygame.display.set_mode((width, height))
delay = 10
img = pygame.image.load('image.png')
img = pygame.transform.scale(img,(width, height))



g1 = Grille()
g1.creation_grille()
g1.couper_photo()
g1.affiche()
"""
g1.est_dans_l_ordre()
"""


running = True
started = game_over = cheat = False
score = 0

while running:
    for event in pygame.event.get():

        key = pygame.key.get_pressed()


        #start the game
        if not started or game_over:
            if key[pygame.K_s]:
                g1.melange(250)
                g1.place_en_bas_a_droite()
                g1.affiche()
                started = True
                game_over = cheat = False
                score = 0

        else:
            #movement
            if key[pygame.K_UP]:
                try:
                    g1.mouvement_possible()["UP"]
                    g1.mouvement(g1.mouvement_possible()["UP"])
                except KeyError:
                    pass
            if key[pygame.K_DOWN]:
                try:
                    g1.mouvement_possible()["DOWN"]
                    g1.mouvement(g1.mouvement_possible()["DOWN"])
                except KeyError:
                    pass
            if key[pygame.K_LEFT]:
                try:
                    g1.mouvement_possible()["LEFT"]
                    g1.mouvement(g1.mouvement_possible()["LEFT"])
                except KeyError:
                    pass
            if key[pygame.K_RIGHT]:
                try:
                    g1.mouvement_possible()["RIGHT"]
                    g1.mouvement(g1.mouvement_possible()["RIGHT"])
                except KeyError:
                    pass

        if event.type == pygame.QUIT:
            running = False
    
    
    
    g1.affiche()
    
    
    #before start
    if not started:
        myfont = pygame.font.SysFont('monospace', width//20)
        start_txt = myfont.render("Press 'S' to start playing", False, (255, 0, 0))
        screen.blit(start_txt, (width//2-start_txt.get_width()//2, height//2-start_txt.get_height()*3))

    #game started
    if started and not game_over:
        
        
        #score
        score += 1
        #print(score/100)

    if started:
        #game_over
        if g1.est_dans_l_ordre() or cheat:
            start_txt = myfont.render("Press 'S' if you want to replay", False, (255, 0, 0))
            screen.blit(start_txt, (width//2-start_txt.get_width()//2, height//2-start_txt.get_height()*2))
            game_over_txt = myfont.render('You finished in '+str(score/100) + ' seconds', False, (255, 0, 0))
            screen.blit(game_over_txt, (width//2-game_over_txt.get_width()//2, height//2-game_over_txt.get_height()*3))
            game_over = True

    if key[pygame.K_c]:
        cheat = True


    pygame.display.flip()
    pygame.time.delay(delay)


pygame.quit()





if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)

