from Entity import *

import libtcodpy as libtcod

class Player(Entity):

    def __init__(self, posX , posY, con, gameMap):
        self.con = con
        self.gameMap = gameMap
        Entity.__init__(self,posX,posY,"@",libtcod.white, self.con)


    def update(self):
        self.movement()

    def movement(self):
        if libtcod.console_is_key_pressed(libtcod.KEY_UP):
            self.move(0,-1, self.gameMap)


        elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
            self.move(0, 1,self.gameMap)


        elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
            self.move(-1, 0,self.gameMap)


        elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
            self.move(1,0,self.gameMap)

        #only display after movement so that we can clean up the past player
        self.draw(self.con)



