"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    vx = graphics.get_vx()
    vy = graphics.get_vy()
    # Add the animation loop here!
    while True:
        # Update
        graphics.ball.move(vx, vy)
        # check
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            vx = -vx  # the ball gets out the left/right margin of the window
        if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height >= graphics.window.height:
            vy = -vy  # the ball gets out the top/bottom margin of the window
        # Pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
