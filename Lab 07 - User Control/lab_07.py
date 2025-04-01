""" Lab 7 - User Control """

import arcade
from arcade import draw_arc_filled


# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


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


def draw_patrick():
    # torso
    arcade.draw_rectangle_filled(300, 200, 40, 40, arcade.csscolor.PINK)

    # head
    arcade.draw_triangle_filled(290, 220, 310, 220, 300, 250, arcade.csscolor.PINK)

    # arms
    arcade.draw_triangle_filled(280, 208, 280, 220, 260, 205, arcade.csscolor.PINK)
    arcade.draw_triangle_filled(320, 208, 320, 220, 340, 205, arcade.csscolor.PINK)

    # legs
    arcade.draw_triangle_filled(285, 180, 280, 190, 260, 155, arcade.csscolor.PINK)
    arcade.draw_triangle_filled(315, 180, 320, 190, 340, 155, arcade.csscolor.PINK)

    # shorts
    arcade.draw_rectangle_filled(300, 180, 48, 15, arcade.csscolor.YELLOW_GREEN)

    # eyes
    arcade.draw_ellipse_filled(297, 230, 4, 8, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(303, 230, 4, 8, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(297, 230, 1, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(303, 230, 1, arcade.csscolor.BLACK)

    # eyebrows
    arcade.draw_line(295, 233, 299, 233, arcade.csscolor.BLACK, 1)
    arcade.draw_line(301, 233, 305, 233, arcade.csscolor.BLACK, 1)

    # mouth
    arcade.draw_arc_outline(300, 222, 13, 3, arcade.csscolor.BLACK, 0, 210, 2, 175)

    # belly button
    arcade.draw_arc_outline(300, 192, 5, 3, arcade.csscolor.BLACK, 0, 210, 2, 175)
    arcade.draw_arc_outline(300, 194, 1, 1, arcade.csscolor.BLACK, 0, 210, 2, 175)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self, width, height, title):
        """ Initializer """

        # call the parent class initializer
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.DODGER_BLUE)


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

        # draw Patrick
        draw_patrick()


def main():
    window = MyGame(800, 600, "Lab 7 - User Control")

    arcade.run()


main()