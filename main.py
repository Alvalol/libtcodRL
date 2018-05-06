from GameObjects.World.Enemy import Enemy
from GameObjects.World.Map import *
from GameObjects.World.Player import *

from setup import *
import libtcodpy as libtcod


#initialize map
gameMap = Map()

gameMap.createMap(con)


# initialize player
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, con, gameMap)
enemy = Enemy((SCREEN_WIDTH/2)+ 1, SCREEN_HEIGHT/2,con)

entities = [player,enemy]

# core game loop
while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(con,libtcod.white)

    for ent in entities:
        ent.update()

    #blits the contents of con to the main console. The last two parameters of this function allow for fading
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0,1,1)
    libtcod.console_flush()
    player.clear(con)

    exit = handle_keys()
    if exit:
        break

