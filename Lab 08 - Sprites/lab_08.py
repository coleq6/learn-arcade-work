""" Sprite Sample Program """

import random
import arcade
import math

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.01
SPRITE_SCALING_APPLE = 0.012
SPRITE_SCALING_FORK = 0.01
FORK_COUNT = 50
APPLE_COUNT = 50
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Apple(arcade.Sprite):
    """
    This class represents the apples on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def update(self):
        # Move the apple
        self.center_y -= 1

        # See if the apple has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)

class Pitchfork(arcade.Sprite):

    def __init__(self, pitchfork, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(pitchfork, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):

        """ Update the pitchfork's position. """
        # Calculate a new x, y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
            + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
            + self.circle_center_y

        # Increase the angle in prep for the next round.
        self.circle_angle += self.circle_speed


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Game")

        # Variables that will hold sprite lists
        self.player_list = None
        self.apple_list = None
        self.fork_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        self.apple_sound = arcade.load_sound("crunch.wav")
        self.fork_sound = arcade.load_sound(":resources:sounds/hurt3.wav")

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.apple_list = arcade.SpriteList()
        self.fork_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from vecteezy.com
        # <a href="https://www.vecteezy.com/free-png/cartoon-pig">Cartoon Pig PNGs by Vecteezy</a>
        self.player_sprite = arcade.Sprite("pig2.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the apples
        for i in range(APPLE_COUNT):

            # Create the apple instance
            # Apple image from vecteezy.com
            #<a href="https://www.vecteezy.com/free-png/apple">Apple PNGs by Vecteezy</a>
            apple = Apple("apple.png", SPRITE_SCALING_APPLE)

            # Position the apple
            apple.center_x = random.randrange(SCREEN_WIDTH)
            apple.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the apple to the lists
            self.apple_list.append(apple)

        # Create the pitchforks
        for i in range(FORK_COUNT):

            # Create the pitchfork instance
            # Pitchfork image from vecteezy.com
            # <a href="https://www.vecteezy.com/free-png/pitchfork">Pitchfork PNGs by Vecteezy</a>
            fork = Pitchfork("pitchfork.png", SPRITE_SCALING_FORK)

            # Position the center of the circle the coin will orbit
            fork.circle_center_x = random.randrange(SCREEN_WIDTH)
            fork.circle_center_y = random.randrange(SCREEN_HEIGHT)

            # Random radius from 10 to 200
            fork.circle_radius = random.randrange(10, 200)

            # Random start angle from 0 to 2pi
            fork.circle_angle = random.random() * 2 * math.pi

            # Add the fork to the lists
            self.fork_list.append(fork)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.apple_list.draw()
        self.player_list.draw()
        self.fork_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        # Prints "Game Over" when all the apples are eaten
        if len(self.apple_list) == 0:
            output = "Game Over"
            arcade.draw_text(output, 235, SCREEN_HEIGHT // 2, arcade.color.WHITE, 50)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        if len(self.apple_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        if len(self.apple_list) > 0:
            self.apple_list.update()
            self.fork_list.update()

        # Generate a list of all sprites that collided with the player.
        sprites_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.apple_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for apple in sprites_hit_list:
            apple.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.apple_sound)

        sprites_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.fork_list)
        for fork in sprites_hit_list:
            fork.remove_from_sprite_lists()
            self.score -= 1
            arcade.play_sound(self.fork_sound)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()