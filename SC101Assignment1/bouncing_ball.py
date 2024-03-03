"""
File:NA
Name:Cara
-------------------------
TODO: Deal with the speed in vertical(vy) and horizontal(vx). There is some speed loss in vx(reduce).
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
# put global variant here
window = GWindow(800, 500, title='bouncing_ball.py')
b_color = 'black'
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
ball.fill_color = 'black'


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX aall = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
ball.fills x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball)
    onmouseclicked(start_fall)


def start_fall(event):
    """
    view displacement and v as same thing and calculate
    for horizontal, vx is always the same
    """
    global ball
    vy = 0
    vx = VX
    x = START_X
    y = START_Y
    while True:  # ball falling
        ball.move(vx, vy)
        vy += GRAVITY
        pause(DELAY)
        if ball.y + ball.height >= window.height:  # ball comes to ground and to bounce
            vy *= -REDUCE
        if ball.x + ball.width >= window.width:  # to check if ball goes out the window
            ball = GOval(20, 20, x=START_X, y=START_Y)
            window.add(ball)


if __name__ == "__main__":
    main()
