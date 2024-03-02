"""
File: blur.py
Name: Cara
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


BLUR = 5


def blur(img, new_img):
    """
    :param img: "images/smiley-face.png"
    :return: new_image
    """
    # Todo: create a new blank img that is as big as the original one
    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)
            new_img_pixel = new_img.get_pixel(x, y)
            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image. (3 neighbours)
                img_pixel = img.get_pixel(x, y)
                right_img_pixel = img.get_pixel(x + 1, y)
                bottom_right_img_pixel = img.get_pixel(x + 1, y + 1)
                bottom_img_pixel = img.get_pixel(x, y + 1)
                new_img_pixel.red = (img_pixel.red + right_img_pixel.red + bottom_right_img_pixel.red + bottom_img_pixel.red) // 3
                new_img_pixel.green = (img_pixel.green + right_img_pixel.green + bottom_right_img_pixel.green + bottom_img_pixel.green) // 3
                new_img_pixel.blue = (img_pixel.blue + right_img_pixel.blue + bottom_right_img_pixel.blue + bottom_img_pixel.blue) // 3

            elif x == img.width - 1 and y == 0:
                # Get pixel at the top-right corner of the image. (3 neighbours)
                img_pixel = img.get_pixel(x, y)
                left_img_pixel = img.get_pixel(x - 1, y)
                bottom_left_img_pixel = img.get_pixel(x - 1, y + 1)
                bottom_img_pixel = img.get_pixel(x, y + 1)
                new_img_pixel.red = (img_pixel.red + left_img_pixel.red + bottom_left_img_pixel.red + bottom_img_pixel.red) // 3
                new_img_pixel.green = (img_pixel.green + left_img_pixel.green + bottom_left_img_pixel.green + bottom_img_pixel.green) // 3
                new_img_pixel.blue = (img_pixel.blue + left_img_pixel.blue + bottom_left_img_pixel.blue + bottom_img_pixel.blue) // 3

            elif x == 0 and y == img.height - 1:
                # Get pixel at the bottom-left corner of the image (3 neighbours)
                img_pixel = img.get_pixel(x, y)
                right_img_pixel = img.get_pixel(x + 1, y)
                bottom_right_img_pixel = img.get_pixel(x + 1, y + 1)
                top_img_pixel = img.get_pixel(x, y - 1)
                new_img_pixel.red = (img_pixel.red + right_img_pixel.red + bottom_right_img_pixel.red + top_img_pixel.red) // 3
                new_img_pixel.green = (img_pixel.green + right_img_pixel.green + bottom_right_img_pixel.green + top_img_pixel.green) // 3
                new_img_pixel.blue = (img_pixel.blue + right_img_pixel.blue + bottom_right_img_pixel.blue + top_img_pixel.blue) // 3

            elif x == img.width - 1 and y == img.height - 1:
                # Get pixel at the bottom-right corner of the image (3 neighbours)
                img_pixel = img.get_pixel(x, y)
                left_img_pixel = img.get_pixel(x - 1, y)
                bottom_left_img_pixel = img.get_pixel(x - 1, y + 1)
                top_img_pixel = img.get_pixel(x, y - 1)
                new_img_pixel.red = (img_pixel.red + left_img_pixel.red + bottom_left_img_pixel.red + top_img_pixel.red) // 3
                new_img_pixel.green = (img_pixel.green + left_img_pixel.green + bottom_left_img_pixel.green + top_img_pixel.green) // 3
                new_img_pixel.blue = (img_pixel.blue + left_img_pixel.blue + bottom_left_img_pixel.blue + top_img_pixel.blue) // 3

            elif 0 < x < img.width - 1 and y == 0:
                # Get top edge's pixels (without two corners) (5 neighbours)
                img_pixel = img.get_pixel(x, y)
                left_img_pixel = img.get_pixel(x - 1, y)
                bottom_left_img_pixel = img.get_pixel(x - 1, y + 1)
                bottom_img_pixel = img.get_pixel(x, y + 1)
                bottom_right_img_pixel = img.get_pixel(x + 1, y + 1)
                right_img_pixel = img.get_pixel(x + 1, y)
                new_img_pixel.red = (img_pixel.red + left_img_pixel.red + bottom_left_img_pixel.red + bottom_img_pixel.red + bottom_right_img_pixel.red + right_img_pixel.red) // 5
                new_img_pixel.green = (img_pixel.green + left_img_pixel.green + bottom_left_img_pixel.green + bottom_img_pixel.green + bottom_right_img_pixel.green + right_img_pixel.green) // 5
                new_img_pixel.blue = (img_pixel.blue + left_img_pixel.blue + bottom_left_img_pixel.blue + bottom_img_pixel.blue + bottom_right_img_pixel.blue + right_img_pixel.blue) // 5

            elif 0 < x < img.width - 1 and y == img.height - 1:
                # Get bottom edge's pixels (without two corners) (5 neighbours)
                img_pixel = img.get_pixel(x, y)
                left_img_pixel = img.get_pixel(x - 1, y)
                top_left_img_pixel = img.get_pixel(x - 1, y - 1)
                top_img_pixel = img.get_pixel(x, y - 1)
                top_right_img_pixel = img.get_pixel(x + 1, y - 1)
                right_img_pixel = img.get_pixel(x + 1, y)
                new_img_pixel.red = (img_pixel.red + left_img_pixel.red + top_left_img_pixel.red + top_img_pixel.red + top_right_img_pixel.red + right_img_pixel.red) // 5
                new_img_pixel.green = (img_pixel.green + left_img_pixel.green + top_left_img_pixel.green + top_img_pixel.green + top_right_img_pixel.green + right_img_pixel.green) // 5
                new_img_pixel.blue = (img_pixel.blue + left_img_pixel.blue + top_left_img_pixel.blue + top_img_pixel.blue + top_right_img_pixel.blue + right_img_pixel.blue) // 5

            elif x == 0 and 0 < y < img.height - 1:
                # Get left edge's pixels (without two corners) (5 neighbours)
                img_pixel = img.get_pixel(x, y)
                top_img_pixel = img.get_pixel(x, y - 1)
                top_right_img_pixel = img.get_pixel(x + 1, y - 1)
                right_img_pixel = img.get_pixel(x + 1, y)
                bottom_right_img_pixel = img.get_pixel(x + 1, y + 1)
                bottom_img_pixel = img.get_pixel(x, y + 1)
                new_img_pixel.red = (img_pixel.red + top_img_pixel.red + top_right_img_pixel.red + right_img_pixel.red + bottom_right_img_pixel.red + bottom_img_pixel.red) // 5
                new_img_pixel.green = (img_pixel.green + top_img_pixel.green + top_right_img_pixel.green + right_img_pixel.green + bottom_right_img_pixel.green + bottom_img_pixel.green) // 5
                new_img_pixel.blue = (img_pixel.blue + top_img_pixel.blue + top_right_img_pixel.blue + right_img_pixel.blue + bottom_right_img_pixel.blue + bottom_img_pixel.blue) // 5

            elif x == img.width - 1 and 0 < y < img.height - 1:
                # Get right edge's pixels (without two corners) (5 neighbours)
                img_pixel = img.get_pixel(x, y)
                top_img_pixel = img.get_pixel(x, y - 1)
                top_left_img_pixel = img.get_pixel(x - 1, y - 1)
                left_img_pixel = img.get_pixel(x - 1, y)
                bottom_left_img_pixel = img.get_pixel(x - 1, y + 1)
                bottom_img_pixel = img.get_pixel(x, y + 1)
                new_img_pixel.red = (img_pixel.red + top_img_pixel.red + top_left_img_pixel.red + left_img_pixel.red + bottom_left_img_pixel.red + bottom_img_pixel.red) // 5
                new_img_pixel.green = (img_pixel.green + top_img_pixel.green + top_left_img_pixel.green + left_img_pixel.green + bottom_left_img_pixel.green + bottom_img_pixel.green) // 5
                new_img_pixel.blue = (img_pixel.blue + top_img_pixel.blue + top_left_img_pixel.blue + left_img_pixel.blue + bottom_left_img_pixel.blue + bottom_img_pixel.blue) // 5

            else:
                # Inner pixels. (9 neighbours)
                img_pixel = img.get_pixel(x, y)
                top_img_pixel = img.get_pixel(x, y - 1)
                bottom_img_pixel = img.get_pixel(x, y + 1)
                right_img_pixel = img.get_pixel(x + 1, y)
                left_img_pixel = img.get_pixel(x - 1, y)
                top_left_img_pixel = img.get_pixel(x - 1, y - 1)
                top_right_img_pixel = img.get_pixel(x + 1, y - 1)
                bottom_left_img_pixel = img.get_pixel(x - 1, y + 1)
                bottom_right_img_pixel = img.get_pixel(x + 1, y + 1)
                new_img_pixel.red = (img_pixel.red + top_img_pixel.red + top_left_img_pixel.red + left_img_pixel.red + bottom_left_img_pixel.red + bottom_img_pixel.red + top_right_img_pixel.red + right_img_pixel.red + bottom_right_img_pixel.red) // 9
                new_img_pixel.green = (img_pixel.green + top_img_pixel.green + top_left_img_pixel.green + left_img_pixel.green + bottom_left_img_pixel.green + bottom_img_pixel.green + top_right_img_pixel.green + right_img_pixel.green + bottom_right_img_pixel.red) // 9
                new_img_pixel.blue = (img_pixel.blue + top_img_pixel.blue + top_left_img_pixel.blue + left_img_pixel.blue + bottom_left_img_pixel.blue + bottom_img_pixel.blue + top_right_img_pixel.blue + right_img_pixel.blue + bottom_right_img_pixel.blue) // 9

    return new_img


def main():
    """
    create a blank canvas and process the blurring on it.
    """
    old_img = SimpleImage("images/smiley-face.png")  # image form, not str
    old_img.show()

    new_img = SimpleImage.blank(old_img.width, old_img.height)

    blurred_img = blur(old_img, new_img)
    for i in range(BLUR):
        blurred_img = blur(old_img, new_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
