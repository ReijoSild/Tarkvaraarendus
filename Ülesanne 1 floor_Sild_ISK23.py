import pygame
import sys

screen=pygame.display.set_mode([300, 300])
pygame.display.set_caption("Foor - Reijo Sild")

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
            
    #Punane
    pygame.draw.circle(screen, [255, 0, 0], [150,60], 40)   
    #Kollane
    pygame.draw.circle(screen, [255, 255, 0], [150,145], 40)       
    #Roheline
    pygame.draw.circle(screen, [0, 255, 0], [150,230], 40)        
    #Riskülik
    pygame.draw.rect(screen, [128, 128, 128], [100, 10, 100, 270], 2)
    
    pygame.display.flip()
     
pygame.quit()
sys.exit()