import libtcodpy as libtcod


class Entity:
    # this is a generic object: the player, a monster, an item, the stairs...
    def __init__(self, x, y, char, color, con):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.con = con

    def move(self, dx, dy, gameMap):

        if not gameMap.gameMap[self.x + dx][self.y + dy].blocked:
            # move by the given amount
            self.x += dx
            self.y += dy

    def draw(self,con):
        # set the color and then draw the character that represents this object at its position
        libtcod.console_set_default_foreground(con, self.color)
        libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)

    def clear(self,con):
        # erase the character that represents this object
        libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)