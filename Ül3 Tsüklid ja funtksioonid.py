import pygame
import sys

#Defineerib ruudu joonistamise funktsiooni
def draw_grid(screen, square_size, ruut_fill_color, ruut_border_color):
    screen.fill(background_color)
    for x in range(0, screen_width, square_size):
        for y in range(0, screen_height, square_size):
            #joonistab ruudu, mis on täidetud
            pygame.draw.rect(screen, ruut_fill_color, (x, y, square_size, square_size))
            #Ruudu äärise joon
            pygame.draw.rect(screen, ruut_border_color, (x, y, square_size, square_size), 1)

    pygame.display.flip() #Uuendab ekrani

pygame.init()

#Ekraani seaded
screen_width, screen_height = 640, 480 #laius, kõrgus
screen = pygame.display.set_mode((screen_width, screen_height)) #Tekitab akna ülaltoodud parameetmetega
pygame.display.set_caption("Harjutamine") #Akna nimi, mis aknal olema hakkab on " " vahel

#Taustavärv
background_color = [255, 255, 255] #Tausta värv, mis on praegusel juhul valge, aga seda ei ole paista, kuna ees on ruudud, mis on täidetud värviga

#Ruudu info, mida läheb funktsioonil draw_grid vaja andmete näol
square_size = 20 #Ruudu suurus
ruut_fill_color = [153, 255, 153]  #roheline ruudu täide
ruut_border_color = [255, 0, 0]  #Punane äär ruutudel

#Joonistab ruudustiku ekraanile
draw_grid(screen, square_size, ruut_fill_color, ruut_border_color)

#Tsükkel, mis reageerib sündmustele, põhiliselt selle jaoks, et mängu ristist kinni panna
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#Sulgeb mängu
pygame.quit()
sys.exit()
