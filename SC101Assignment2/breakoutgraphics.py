"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        """

        :type brick_spacing: object
        """
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title="bricks game")

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=window_width * 0.5 - paddle_width * 0.5, y=window_height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=window_width * 0.5 - ball_radius, y=window_height * 0.5 - ball_radius)

        # Default initial velocity for the ball
        # Initialize our mouse listeners
        # onmouseclicked()
        onmousemoved(self.paddle_move)

        # Draw bricks
        self.brick = GRect(brick_width, brick_height)
        self.bc = brick_cols
        self.br = brick_rows
        self.set_brick_position()

        # Collision
        self.collision_check()
        self.if_collisions = False
        self.collision_feedback()

    def set_brick_position(self, brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET,
                           brick_spacing=BRICK_SPACING):
        for i in range(1, self.br + 1):
            for j in range(1, self.bc + 1):
                if i <= self.br / 5:
                    self.brick = GRect(brick_width, brick_height, x=brick_width * (j - 1) + brick_spacing * (j - 1),
                                       y=brick_offset + brick_height * (i - 1) + brick_spacing * (i - 1))
                    self.brick.filled = True
                    self.brick.fill_color = 'red'
                    self.window.add(self.brick)
                elif i <= self.br * 2 / 5:
                    self.brick = GRect(brick_width, brick_height, x=brick_width * (j - 1) + brick_spacing * (j - 1),
                                       y=brick_offset + brick_height * (i - 1) + brick_spacing * (i - 1))
                    self.brick.filled = True
                    self.brick.fill_color = 'orange'
                    self.window.add(self.brick)
                elif i <= self.br * 3 / 5:
                    self.brick = GRect(brick_width, brick_height, x=brick_width * (j - 1) + brick_spacing * (j - 1),
                                       y=brick_offset + brick_height * (i - 1) + brick_spacing * (i - 1))
                    self.brick.filled = True
                    self.brick.fill_color = 'yellow'
                    self.window.add(self.brick)
                elif i <= self.br * 4 / 5:
                    self.brick = GRect(brick_width, brick_height, x=brick_width * (j - 1) + brick_spacing * (j - 1),
                                       y=brick_offset + brick_height * (i - 1) + brick_spacing * (i - 1))
                    self.brick.filled = True
                    self.brick.fill_color = 'green'
                    self.window.add(self.brick)
                elif i <= self.br:
                    self.brick = GRect(brick_width, brick_height, x=brick_width * (j - 1) + brick_spacing * (j - 1),
                                       y=brick_offset + brick_height * (i - 1) + brick_spacing * (i - 1))
                    self.brick.filled = True
                    self.brick.fill_color = 'blue'
                    self.window.add(self.brick)

    def paddle_move(self, event):
        if event.x < self.paddle.width*0.5:  # paddle is at the most left
            self.paddle.x = 0
        elif event.x > self.window.width - self.paddle.width*0.5:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width*0.5

    def check_for_collisions(self):
        if self.window.get_object_at(self.ball.x, self.ball.y) is None:
            if self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y) is None:
                if self.window.get_object_at(self.ball.x, self.ball.y + self.ball_radius * 2) is None:
                    if self.window.get_object_at(self.ball.x + self.ball_radius * 2,
                                                 self.ball.y + self.ball_radius * 2) is None:
                        pass
                    else:
                        self.obj = self.window.get_object_at(self.ball.x + self.ball_radius * 2,
                                                             self.ball.y + self.ball_radius * 2)
                        self.collision_feedback()
                else:
                    self.obj = self.window.get_object_at(self.ball.x, self.ball.y + self.ball_radius * 2)
                    self.collision_feedback()
            else:
                self.obj = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y)
                self.collision_feedback()
        else:
            self.obj = self.window.get_object_at(self.ball.x, self.ball.y)
            self.collision_feedback()

    @staticmethod
    def get_vx():
        return random.randint(0, MAX_X_SPEED)

    @staticmethod
    def get_vy():
        return INITIAL_Y_SPEED

    # def ball_move(self, event):
    def collision_feedback(self):
        pass


