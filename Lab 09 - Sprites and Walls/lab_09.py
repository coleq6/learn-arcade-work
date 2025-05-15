import random
import arcade
from pyglet.math import Vec2

SPRITE_SCALING = 0.5
SPRITE_SCALING_GRASS = 0.5

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

NUMBER_OF_GRASS = 50

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 5

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.grass_list = None

        # Set up the player info
        self.score = 0
        self.player_sprite = None
        self.score_text = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.grass_sound = arcade.load_sound("crunch.wav")


        # Create the cameras. One for the GUI, one for the sprites.

        # We scroll the 'sprite world' but not the GUI.

        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.grass_list = arcade.SpriteList()


        # Set up the player
        score = 0

        # Mouse from kenney.nl
        self.player_sprite = arcade.Sprite(":resources:images/enemies/wormGreen.png",
                                           scale=0.4, flipped_horizontally=True)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        # -- Set up border
        # Stone from kenney.nl
        for x in range(0, 960, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)
        for x in range(0, 1024, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 960
            self.wall_list.append(wall)

        for y in range(0, 960, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter.png", SPRITE_SCALING)
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)
        for y in range(0, 960, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter.png", SPRITE_SCALING)
            wall.center_x = 960
            wall.center_y = y
            self.wall_list.append(wall)

        # Set up walls (Lava)
        # Lava from kenney.nl
        for x in range(64, 940, 192):
            for y in range(64, 940, 128):
                    wall = arcade.Sprite(":resources:images/tiles/lava.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)
        for y in range(64, 940, 192):
            for x in range(64, 940, 128):
                    wall = arcade.Sprite(":resources:images/tiles/lava.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        # --- Place walls with a list
        coordinate_list = [[126, 704],
                           [64, 896],
                           [320, 896],
                           [256, 640],
                           [640, 640],
                           [256, 256],
                           [640, 256],
                           [128, 320],
                           [768, 896],
                           [384, 896],
                           [512, 704],
                           [256, 384],
                           [896, 576],
                           [768, 512],
                           [704, 128],
                           [448, 768],
                           [896, 320]]
        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite(":resources:images/tiles/lava.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # -- Randomly place grass where there are no walls
        # Create the grass
        for i in range(NUMBER_OF_GRASS):

            # Create the grass instance
            # grass image from kenney.nl
            grass = arcade.Sprite(":resources:images/tiles/grass_sprout.png", SPRITE_SCALING_GRASS)

            # --- IMPORTANT PART ---

            # Boolean variable if we successfully placed the grass
            grass_placed_successfully = False

            # Keep trying until success
            while not grass_placed_successfully:
                # Position the grass
                grass.center_x = random.randrange(64, 940)
                grass.center_y = random.randrange(64, 940)

                # See if the grass is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(grass, self.wall_list)

                # See if the grass is hitting another grass
                grass_hit_list = arcade.check_for_collision_with_list(grass, self.grass_list)

                if len(wall_hit_list) == 0 and len(grass_hit_list) == 0:
                    # It is!
                    grass_placed_successfully = True

            # Add the grass to the lists
            self.grass_list.append(grass)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.grass_list.draw()


        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 50, arcade.color.WHITE, 14)
        # Prints "Game Over" when all the grass is eaten
        if len(self.grass_list) == 0:
            output = "Game Over"
            arcade.draw_text(output, 235, DEFAULT_SCREEN_WIDTH // 2, arcade.color.WHITE, 50)

    def update_player_speed(self):

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
            self.update_player_speed()
        elif key == arcade.key.DOWN:
            self.down_pressed = True
            self.update_player_speed()
        elif key == arcade.key.LEFT:
            self.left_pressed = True
            self.update_player_speed()
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
            self.update_player_speed()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
            self.update_player_speed()
        elif key == arcade.key.DOWN:
            self.down_pressed = False
            self.update_player_speed()
        elif key == arcade.key.LEFT:
            self.left_pressed = False
            self.update_player_speed()
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
            self.update_player_speed()

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Call update on all sprites
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

        # Call update on all sprites
        if len(self.grass_list) > 0:
            self.grass_list.update()

        # Generate a list of all sprites that collided with the player.
        sprites_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.grass_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for grass in sprites_hit_list:
            grass.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.grass_sound)

    def scroll_to_player(self):

        position = Vec2(self.player_sprite.center_x - self.width / 2,

                        self.player_sprite.center_y - self.height / 2)

        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):

        self.camera_sprites.resize(int(width), int(height))

        self.camera_gui.resize(int(width), int(height))

def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()