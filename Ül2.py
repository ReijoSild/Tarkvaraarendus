import pygame
import sys

pygame.init()

# Akna suurus
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Harjutamine")

# Laadi pilt
bg_shop = pygame.image.load("bg_shop.png")

# Mees
seller = pygame.image.load("seller.png")
seller = pygame.transform.scale(seller, [250, 305])

# Chat kast
chat = pygame.image.load("chat.png")
chat = pygame.transform.scale(chat, [255, 210])

#font ja suurus
font = pygame.font.Font(None, 28)

# Tekst chat kasti
text = "Tere, olen Reijo Sild"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Kuvab taustapildi (0, 0) asukohast alates
    screen.blit(bg_shop, (0, 0))
    screen.blit(seller, [108, 160])
    screen.blit(chat, [246, 65])

    # Kuvab teksti
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(370, 155))
    screen.blit(text_surface, text_rect.topleft)

    # Uuenda ekraan
    pygame.display.flip()

pygame.quit()
sys.exit()
