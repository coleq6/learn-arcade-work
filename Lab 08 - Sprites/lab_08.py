""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.01
SPRITE_SCALING_APPLE = 0.012
APPLE_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Game")

        # Variables that will hold sprite lists
        self.player_list = None
        self.apple_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        self.apple_sound = arcade.load_sound(":resources:/sounds/coin2.wav")

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.apple_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from vecteezy.com
        # <a href="https://www.vecteezy.com/free-png/cartoon-pig">Cartoon Pig PNGs by Vecteezy</a>
        self.player_sprite = arcade.Sprite("pig2.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(APPLE_COUNT):

            # Create the apple instance
            # Apple image from vecteezy.com
            #<a href="https://www.vecteezy.com/free-png/apple">Apple PNGs by Vecteezy</a>
            apple = arcade.Sprite("apple.png", SPRITE_SCALING_APPLE)

            # Position the coin
            apple.center_x = random.randrange(SCREEN_WIDTH)
            apple.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.apple_list.append(apple)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.apple_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.apple_list.update()

        # Generate a list of all sprites that collided with the player.
        apples_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.apple_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for apple in apples_hit_list:
            apple.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.apple_sound)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()