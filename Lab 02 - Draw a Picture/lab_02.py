# import arcade library
import arcade
from arcade import draw_arc_filled

# open window

arcade.open_window(600, 600, "Lab 2 Drawing")

# set background


arcade.set_background_color(arcade.csscolor.DODGER_BLUE)

# get ready to draw

arcade.start_render()

# draw ground

arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, (252, 231, 194))

# draw road

arcade.draw_rectangle_filled(300, 0, 600, 75, arcade.csscolor.BLACK)
arcade.draw_rectangle_filled(295, 0, 50, 400, arcade.csscolor.BLACK)

# draw Patrick's rock

draw_arc_filled(295, 200, 450, 400, arcade.csscolor.SADDLE_BROWN, 0, 180)

# - - - draw weathervane on house - - -

# vertical and horizontal parts

arcade.draw_rectangle_filled(295, 415, 5, 30, arcade.csscolor.TAN)
arcade.draw_rectangle_filled(295, 428, 50, 5, arcade.csscolor.TAN)

# arrow-looking parts

arcade.draw_line(278,440,267,425, arcade.csscolor.TAN, 5)
arcade.draw_line(267,430,278,415, arcade.csscolor.TAN, 5)

# slight angled rightmost parts

arcade.draw_line(305,438,309,420, arcade.csscolor.TAN, 4)
arcade.draw_line(313,438,317,420, arcade.csscolor.TAN, 4)

# - - - draw Patrick - - -

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

# - - - face - - -

# eyes

arcade.draw_ellipse_filled(297, 230, 4, 8, arcade.csscolor.WHITE)
arcade.draw_ellipse_filled(303, 230, 4, 8, arcade.csscolor.WHITE)
arcade.draw_circle_filled(297, 230, 1, arcade.csscolor.BLACK)
arcade.draw_circle_filled(303, 230, 1, arcade.csscolor.BLACK)

# eyebrows

arcade.draw_line(295,233,299,233, arcade.csscolor.BLACK, 1)
arcade.draw_line(301,233,305,233, arcade.csscolor.BLACK, 1)

# mouth

arcade.draw_arc_outline(300, 222, 13, 3, arcade.csscolor.BLACK, 0, 210, 2, 175)

# belly button

arcade.draw_arc_outline(300, 192, 5, 3, arcade.csscolor.BLACK, 0, 210, 2, 175)
arcade.draw_arc_outline(300, 194, 1, 1, arcade.csscolor.BLACK, 0, 210, 2, 175)

# - - - decor - - -

# rocks

draw_arc_filled(100, 120, 65, 50, arcade.csscolor.GRAY, 0, 180)
arcade.draw_circle_filled(90, 122, 2, arcade.csscolor.PINK)
arcade.draw_circle_filled(100, 135, 2, arcade.csscolor.GREEN)
arcade.draw_circle_filled(120, 125, 2, arcade.csscolor.BLUE)
draw_arc_filled(500, 80, 40, 85, arcade.csscolor.GRAY, 0, 180)
arcade.draw_circle_filled(500, 84, 2, arcade.csscolor.YELLOW)
arcade.draw_circle_filled(495, 96, 2, arcade.csscolor.INDIANRED)
arcade.draw_circle_filled(510, 110, 2, arcade.csscolor.MAGENTA)

# finish drawing

arcade.finish_render()

# keep window up

arcade.run()




































