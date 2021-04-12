import pygame

width = height= 800
pygame.init()
screen = pygame.display.set_mode((width, height))

delay = 50



img = pygame.image.load('image1.jpg')
img = pygame.transform.scale(img,(800, 800))
screen.blit(img, (0,0)) # affiche img en (0,0)
rect = pygame.Rect(200, 400, 100, 100)
screen.blit(img.subsurface(rect), (0,0))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #screen.blit(img, (0,0)) # affiche img en (0,0)
    pygame.display.flip()
    pygame.time.delay(delay)

pygame.quit()
