"""
File: best_photoshop_award.py
Name: Cara
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


THRESHOLD = 1


def main():
    """
    Idea: remind me back to learn StanCode SC101 haha.
    """
    fig = SimpleImage('image_contest/me.jpg')
    bg = SimpleImage('image_contest/bg.jpg')
    bg.make_as_big_as(fig)
    new_img = combine(fig, bg)
    new_img.show()


def combine(fig, bg):
    for x in range(fig.width):
        for y in range(fig.height):
            fig_pixel = fig.get_pixel(x, y)
            avg = (fig_pixel.red + fig_pixel.green + fig_pixel.blue) // 3
            if fig_pixel.blue > avg * THRESHOLD:
                # blue screen
                bg_pixel = bg.get_pixel(x, y)
                fig_pixel.red = bg_pixel.red
                fig_pixel.green = bg_pixel.green
                fig_pixel.blue = bg_pixel.blue
    return fig





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
