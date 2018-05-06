from Entity import *

class Enemy(Entity):

    def __init__(self, posX , posY, con):
        self.con = con
        Entity.__init__(self,posX,posY,"X" ,libtcod.yellow, self.con)


    def update(self):
        self.movement()

    def movement(self):

        #define movement
        self.draw(self.con)



