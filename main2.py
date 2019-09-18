#!/usr/bin/env python3

import utils, os, random, time, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites Example"


class Emote(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.frequency = 1 #update every second        
        self.timer = time.time()
        emotes = ['alert','anger','bars','cash','circle','cloud','cross','dots1','dots2','dots3','drop','drops','exclamation','exclamations','faceAngry','faceHappy','faceSad','heart','heartBroken','hearts','idea','laugh','music','question','sleep','sleeps','star','stars','swirl']
        self.emoteRange = len(emotes)-1
        for e in emotes:
            texture = arcade.load_texture("assets/emote/emote_{0}.png".format(e), scale=1)
            self.textures.append(texture)
        whichTexture = random.randint(0,self.emoteRange)
        self.set_texture(whichTexture)

    def update(self):
        now = time.time()
        #update once per minute
        if (now - self.timer) >= self.frequency:
            self.timer = time.time()
            whichTexture = random.randint(0,self.emoteRange)
            self.set_texture(whichTexture)



class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(open_color.blue_4)

        self.animal_list = arcade.SpriteList()
        self.emote_list = arcade.SpriteList()


    def setup(self):
        self.animal_sprite = arcade.Sprite("assets/crocodile.png", 0.5)
        self.animal_sprite.center_x = 200
        self.animal_sprite.center_y = 300
        self.animal_list.append(self.animal_sprite)

        self.emote_sprite = Emote()
        self.emote_sprite.center_x = 200
        self.emote_sprite.center_y = 360
        self.emote_list.append(self.emote_sprite)

        self.animal_sprite = arcade.Sprite("assets/crocodile.png", 0.5)
        self.animal_sprite.center_x = 600
        self.animal_sprite.center_y = 300
        self.animal_list.append(self.animal_sprite)

        self.emote_sprite = Emote()
        self.emote_sprite.center_x = 600
        self.emote_sprite.center_y = 360
        self.emote_list.append(self.emote_sprite)
        

    def on_draw(self):
        arcade.start_render()
        self.animal_list.draw()
        self.emote_list.draw()


    def update(self, delta_time):
        self.emote_list.update()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()