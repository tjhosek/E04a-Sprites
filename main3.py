#!/usr/bin/env python3

import utils, os, random, time, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites Example"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(open_color.blue_4)

        self.animal_list = arcade.SpriteList()


    def setup(self):
        self.animal_sprite = arcade.Sprite("assets/moose.png", 0.5)
        self.animal_sprite.center_x = 400
        self.animal_sprite.center_y = 300
        self.animal_list.append(self.animal_sprite)
        

    def on_draw(self):
        arcade.start_render()
        self.animal_list.draw()


    def update(self, delta_time):
        pass


    def on_mouse_motion(self, x, y, dx, dy):
        for a in self.animal_list:
            self.animal_sprite.center_x = x
            self.animal_sprite.center_y = y

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()