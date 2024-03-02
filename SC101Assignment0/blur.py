"""
File: blur.py
Name: Cara
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage
BLUR = 5

def blur(img, new_img):
    """
    :param img: "images/smiley-face.png"
    :return: new_image
    """
    width = img.width
    height = img.height
    # get all the points of the image
    for y in range(0, height):
        for x in range(0, width):
            total_r, total_g, total_b = 0, 0, 0
            for i in range(-1,2):
                for j in range(-1,2):  # left and right side of the pixel(-1~1)
                    if 0 <= x+i < width and 0 <= y+j < height:  # to make sure the pixels are inside the image
                        r = img.get_pixel([x + i, y + j])
                        g = img.get_pixel((x + i, y + j))
                        b = img.get_pixel((x + i, y + j))
                        total_r += r
                        total_g += g
                        total_b += b
                        count = 9
            new_r = total_r // count
            new_g = total_g // count
            new_b = total_b // count

            new_img.putpixel([x, y], (new_r, new_g, new_b))
    return new_img


def main():
    """
    TODO: Create a new canvas and process blurring on it.
    """
    img = SimpleImage("images/smiley-face.png")
    img.show()

    new_img = SimpleImage.blank(img.width, img.height)

    blurred_img = blur(img, new_img)
    for i in range(BLUR):
        blurred_img = blur(img, new_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
