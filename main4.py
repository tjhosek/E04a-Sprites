#!/usr/bin/env python3

import utils, os, random, time, open_color, arcade, math

utils.check_version((3,7))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites Example"

# This code was addapted from kyong.com/python/python-how-to-list-all-files-in-a-directory/
# It puts every file in a directory in a list
png_list = []

for r, d, f in os.walk("assets/kenney_tankspack/PNG/Default_size"):
    for file in f:
        if '.png' in file:
            png_list.append(os.path.join(r, file))
# This is the end of the adapted

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(open_color.white)

        self.sprite_list = arcade.SpriteList()


    def setup(self):
        for i in range(20):
            self.sprite = arcade.Sprite(random.choice(png_list))
            self.sprite.center_x = random.randint(0,SCREEN_WIDTH)
            self.sprite.center_y = random.randint(0,SCREEN_HEIGHT)
            self.sprite_list.append(self.sprite)

    def on_draw(self):
        arcade.start_render()
        self.sprite_list.draw()

    def update(self, delta_time):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        for i in self.sprite_list:
            if math.sqrt((x-self.sprite.center_x)**2 + (y-self.sprite.center_y)**2) < 10:
                if self.sprite.center_x > x:
                    self.sprite.center_x+=1
                else:
                    self.sprite.center_x-=1
                if self.sprite.center_y > y:
                    self.sprite.center_y+=1
                else:
                    self.sprite.center_y-=1

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()