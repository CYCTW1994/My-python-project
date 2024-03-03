"""
File: NA
Name:Cara
-------------------------
TODO: Do a continuous line drawing mechanism.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 15  # the size of the circle
window = GWindow(width=800, height=500, title='line Drawing')
count_click = 1  # to track how many times of click
line_start = None
event_x = 0
event_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(drawing)


def drawing(event):
    global count_click  # 表達當作變數使用 @staticmethod
    global event_x
    global event_y
    # circle will show up in the center of the click
    if count_click % 2 != 0:  # odd-number of click
        circle = GOval(SIZE, SIZE, x=event.x - SIZE / 2, y=event.y - SIZE / 2)
        window.add(circle)
        event_x = event.x
        event_y = event.y
    else:  # even-number of click
        line = GLine(event_x, event_y, event.x, event.y)
        window.add(line, x=event.x - SIZE / 2, y=event.y - SIZE / 2)

    count_click += 1


if __name__ == "__main__":
    main()
