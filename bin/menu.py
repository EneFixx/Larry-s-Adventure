import pygame as pg

color = (80,80,80,128)
couleur = pg.Color(0,0,0,a=120)


def menu_display(screen,screen_width,screen_height):
    
    

    screen.fill((0,0,0,128))
    pg.draw.rect(screen, color, pg.Rect((screen_width/2 - 250), (screen_height/7), 500, 160))
    pg.draw.rect(screen, color, pg.Rect((screen_width/2 - 250), (screen_height/7 + 2*screen_height/7 ), 500, 160))
    pg.draw.rect(screen, color, pg.Rect((screen_width/2 - 250), (screen_height/7 + 4*screen_height/7 ), 500, 160))
