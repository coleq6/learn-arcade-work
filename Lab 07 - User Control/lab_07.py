""" Lab 7 - User Control """

import arcade
from arcade import draw_arc_filled

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


class Sponge:
    def __init__(self, position_x, position_y, change_x, change_y):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.hurt_sound = arcade.load_sound(":resources:/sounds/hurt3.wav")
        self.hurt_sound_player = None

    def draw(self):
        """ Draw Spongebob with the instance variables we have. """
        draw_spongebob(self.position_x, self.position_y)

    def update(self):
        # move the sponge
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the sponge hit the edge of the screen. If so, change direction
        if self.position_x < 30:
            if not self.hurt_sound_player or not self.hurt_sound_player.playing:
                self.hurt_sound_player = arcade.play_sound(self.hurt_sound)
            self.position_x = self.position_x + 3
        if self.position_x > SCREEN_WIDTH - 30:
            if not self.hurt_sound_player or not self.hurt_sound_player.playing:
                self.hurt_sound_player = arcade.play_sound(self.hurt_sound)
            self.position_x = SCREEN_WIDTH - 30
        if self.position_y < 50:
            if not self.hurt_sound_player or not self.hurt_sound_player.playing:
                self.hurt_sound_player = arcade.play_sound(self.hurt_sound)
            self.position_y = self.position_y + 3
        if self.position_y > 300:
            if not self.hurt_sound_player or not self.hurt_sound_player.playing:
                self.hurt_sound_player = arcade.play_sound(self.hurt_sound)
            self.position_y = SCREEN_HEIGHT - 300

class Pat:
    def __init__(self, position_x, position_y):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.hurt_sound = arcade.load_sound(":resources:/sounds/hurt3.wav")
        self.hurt_sound_player = None

    def draw(self):
        """ Draw Patrick with the instance variables we have. """
        draw_patrick(self.position_x, self.position_y)
        if self.position_x < 30:
            if not self.hurt_sound_player or not self.hurt_sound_player.playing:
                self.hurt_sound_player = arcade.play_sound(self.hurt_sound)
        if self.position_x > SCREEN_WIDTH - 30:
            if not self.hurt_sound_player or not self.hurt_sound_player.playing:
                self.hurt_sound_player = arcade.play_sound(self.hurt_sound)
        if self.position_y < 50:
            if not self.hurt_sound_player or not self.hurt_sound_player.playing:
                self.hurt_sound_player = arcade.play_sound(self.hurt_sound)
        if self.position_y > SCREEN_HEIGHT - 30:
            if not self.hurt_sound_player or not self.hurt_sound_player.playing:
                self.hurt_sound_player = arcade.play_sound(self.hurt_sound)

# make ground function
def draw_ground():
    """Draw the ground"""
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 2, 0, (252, 231, 194))


def draw_road():
    arcade.draw_rectangle_filled(300, 0, 1000, 75, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(295, 0, 50, 400, arcade.csscolor.BLACK)


# make rock function
def draw_rock_1(x, y):
    """Draw rock style 1"""

    # draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # rock
    draw_arc_filled(x, y - 10, 65, 50, arcade.csscolor.GRAY, 0, 180)

    # spots
    arcade.draw_circle_filled(x - 10, y - 8, 2, arcade.csscolor.PINK)
    arcade.draw_circle_filled(x, y + 5, 2, arcade.csscolor.GREEN)
    arcade.draw_circle_filled(x + 20, y - 5, 2, arcade.csscolor.BLUE)


def draw_rock_2(x, y):
    """Draw rock style 2"""

    arcade.draw_point(x, y, arcade.color.RED, 5)

    # rock
    draw_arc_filled(x, y - 30, 40, 85, arcade.csscolor.GRAY, 0, 180)

    # spots
    arcade.draw_circle_filled(x, y - 24, 2, arcade.csscolor.YELLOW)
    arcade.draw_circle_filled(x - 5, y - 16, 2, arcade.csscolor.INDIANRED)
    arcade.draw_circle_filled(x + 10, y, 2, arcade.csscolor.MAGENTA)


def draw_house():
    """Draw Patrick's rock"""

    arcade.draw_point(295, 250, arcade.color.RED, 5)

    # draw Patrick's rock

    draw_arc_filled(295, 200, 450, 400, arcade.csscolor.SADDLE_BROWN, 0, 180)

    # vertical and horizontal parts

    arcade.draw_rectangle_filled(295, 415, 5, 30, arcade.csscolor.TAN)
    arcade.draw_rectangle_filled(295, 428, 50, 5, arcade.csscolor.TAN)

    # arrow-looking parts

    arcade.draw_line(278, 440, 267, 425, arcade.csscolor.TAN, 5)
    arcade.draw_line(267, 430, 278, 415, arcade.csscolor.TAN, 5)

    # slight angled rightmost parts

    arcade.draw_line(305, 438, 309, 420, arcade.csscolor.TAN, 4)
    arcade.draw_line(313, 438, 317, 420, arcade.csscolor.TAN, 4)


def draw_patrick(x, y):
    # torso
    arcade.draw_rectangle_filled(x, y + 8, 40, 40, arcade.csscolor.PINK)

    # head
    arcade.draw_triangle_filled(x - 10, y + 28, x + 10, y + 28, x, y + 58, arcade.csscolor.PINK)

    # arms
    arcade.draw_triangle_filled(x - 20, y + 16, x - 20, y + 28, x - 40, y + 13, arcade.csscolor.PINK)
    arcade.draw_triangle_filled(x + 20, y + 16, x + 20, y + 28, x + 40, y + 13, arcade.csscolor.PINK)

    # legs
    arcade.draw_triangle_filled(x - 15, y - 12, x - 20, y - 2, x - 40, y - 37, arcade.csscolor.PINK)
    arcade.draw_triangle_filled(x + 15, y - 12, x + 20, y - 2, x + 40, y - 37, arcade.csscolor.PINK)

    # shorts
    arcade.draw_rectangle_filled(x, y - 12, 48, 15, arcade.csscolor.YELLOW_GREEN)

    # eyes
    arcade.draw_ellipse_filled(x - 3, y + 38, 4, 8, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(x + 3, y + 38, 4, 8, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x - 3, y + 38, 1, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(x + 3, y + 38, 1, arcade.csscolor.BLACK)

    # eyebrows
    arcade.draw_line(x - 5, y + 41, x - 1, y + 41, arcade.csscolor.BLACK, 1)
    arcade.draw_line(x + 1, y + 41, x + 5, y + 41, arcade.csscolor.BLACK, 1)

    # mouth
    arcade.draw_arc_outline(x, y + 30, 13, 3, arcade.csscolor.BLACK, 0, 210, 2, 175)

    # belly button
    arcade.draw_arc_outline(x, y, 5, 3, arcade.csscolor.BLACK, 0, 210, 2, 175)
    arcade.draw_arc_outline(x, y + 2, 1, 1, arcade.csscolor.BLACK, 0, 210, 2, 175)


def draw_spongebob(x, y):

    # head
    arcade.draw_rectangle_filled(x, y, 40, 50, arcade.csscolor.YELLOW)

    # torso
    arcade.draw_rectangle_filled(x, y - 20, 40, 10, arcade.csscolor.FIREBRICK)
    arcade.draw_rectangle_filled(x, y - 15, 40, 5, arcade.csscolor.WHITE)

    # arms
    arcade.draw_rectangle_filled(x - 22, y - 20, 40, 2, arcade.csscolor.YELLOW, 100)
    arcade.draw_rectangle_filled(x + 22, y - 20, 40, 2, arcade.csscolor.YELLOW, 80)

    # legs
    arcade.draw_rectangle_filled(x - 10, y - 35, 20, 2, arcade.csscolor.YELLOW, 90)
    arcade.draw_rectangle_filled(x + 10, y - 35, 20, 2, arcade.csscolor.YELLOW, 90)

    # shoes
    arcade.draw_rectangle_filled(x- 12, y - 47, 10, 4, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(x + 12, y - 47, 10, 4, arcade.csscolor.BLACK)

    #  nose
    arcade.draw_arc_outline(x, y, 3, 7, arcade.csscolor.BLACK, 30, 210, 2, 360)

    # eyes
    arcade.draw_ellipse_filled(x - 3, y + 8, 9, 8, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(x + 3, y + 8, 9, 8, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x - 3, y + 8, 2, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(x + 3, y + 8, 2, arcade.csscolor.BLACK)

    # mouth
    arcade.draw_arc_outline(x, y - 5, 13, 3, arcade.csscolor.BLACK, 0, 210, 2, 175)

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        arcade.set_background_color(arcade.color.DODGER_BLUE)

        # draw Spongebob
        self.spongebob = Sponge(400, 200, 0, 0)

        # draw Patrick
        self.patrick = Pat(300, 200)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        self.laser_sound = arcade.load_sound(":resources:/sounds/laser1.wav")

    def on_draw(self):
        arcade.start_render()

        # draw ground function
        draw_ground()

        # draw road
        draw_road()

        # draw house function
        draw_house()

        # draw rocks function
        draw_rock_1(70, 80)
        draw_rock_1(570, 240)
        draw_rock_1(360, 60)
        draw_rock_2(500, 80)
        draw_rock_2(180, 130)
        draw_rock_2(700, 130)

        self.spongebob.draw()

        self.patrick.draw()

    def update(self, delta_time):
        self.spongebob.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.spongebob.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.spongebob.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.spongebob.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.spongebob.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.spongebob.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.spongebob.change_y = 0

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.patrick.position_x = x
        self.patrick.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.laser_sound)

def main():
    window = MyGame()
    arcade.run()

main()