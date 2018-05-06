from Tile import *
import libtcodpy as libtcod

class Map(object):
    def __init__(self):
        self.MAP_WIDTH = 80
        self.MAP_HEIGHT = 40
        self.gameMap = []

    def generateMap(self):
        self.gameMap = [
            [Tile(False) for y in range(self.MAP_HEIGHT)]
            for x in range(self.MAP_WIDTH)
            ]
        # place two pillars to test the map
        self.gameMap[30][22].blocked = True
        self.gameMap[30][22].block_sight = True
        self.gameMap[50][22].blocked = True
        self.gameMap[50][22].block_sight = True


    def renderMap(self,con):
        for y in range(self.MAP_HEIGHT):
            for x in range(self.MAP_WIDTH):
                wall = self.gameMap[x][y].block_sight
                if wall:
                    libtcod.console_set_char_background(con, x, y, libtcod.yellow, libtcod.BKGND_SET)
                else:
                    libtcod.console_set_char_background(con, x, y, libtcod.black, libtcod.BKGND_SET)

    def createMap(self, con):
        self.generateMap()
        self.renderMap(con)