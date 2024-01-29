import pygame
import sys

pygame.init()

screen=pygame.display.set_mode([300, 300])
pygame.display.set_caption("Lumemees - Reijo Sild")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.VIDEORESIZE:
            # Käitle ekraani suuruse muutmise sündmust
            new_size = event.size
            screen = pygame.display.set_mode(new_size, pygame.RESIZABLE)
    #Lumemees
    pygame.draw.circle(screen, [255, 255, 255], [150,75], 30)
    pygame.draw.circle(screen, [255, 255, 255], [150,140], 40)
    pygame.draw.circle(screen, [255, 255, 255], [150,225], 50)
    
    #Silmad
    pygame.draw.circle(screen, [0, 0, 0], [140,70], 5)
    pygame.draw.circle(screen, [0, 0, 0], [160,70], 5)
    
    #Nina
    pygame.draw.polygon(screen, (255, 0, 0), [[145, 80], [150, 95], [155, 80]])
           
    pygame.display.flip()
     
pygame.quit()
sys.exit()