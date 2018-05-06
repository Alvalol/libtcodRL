import libtcodpy as libtcod

##CONSTANTS

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20


#LIBTCOD SETUP
con = libtcod.console_new(SCREEN_WIDTH,SCREEN_HEIGHT)
libtcod.console_set_custom_font("arial10x10.png", libtcod.FONT_TYPE_GRAYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH,SCREEN_HEIGHT, "tutorial",False)


## this handles inputs and allows for console to be flushed
def handle_keys():
    key = libtcod.console_wait_for_keypress(True)  # turn-based

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

    elif key.vk == libtcod.KEY_ESCAPE:
        return True  # exit game
