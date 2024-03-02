"""
File: mirror_lake.py
Name:
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename, new_canvas):
    """
    :param filename:
    :return:
    """
    original_mt = SimpleImage(filename)  # 需要讀檔將圖轉成一格一格pixel,後續作處理（如果是文字是用ｏｐｅｎ）
    for y in range(original_mt.height):
        for x in range(original_mt.width):
            # Colored Pixel
            img_pixel = original_mt.get_pixel(x, y)
            # process on Blank Pixel - the top
            new_canvas_pixel1 = new_canvas.get_pixel(x, y)
            new_canvas_pixel1.red = img_pixel.red
            new_canvas_pixel1.green = img_pixel.green
            new_canvas_pixel1.blue = img_pixel.blue
            # process on Blank Pixel - the bottom
            new_canvas_pixel2 = new_canvas.get_pixel(x, new_canvas.height - 1 - y)
            new_canvas_pixel2.red = img_pixel.red
            new_canvas_pixel2.green = img_pixel.green
            new_canvas_pixel2.blue = img_pixel.blue
    return new_canvas


def main():
    """
    TODO:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()

    new_canvas = SimpleImage.blank(original_mt.width, original_mt.height * 2)

    reflected = reflect('images/mt-rainier.jpg', new_canvas)
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
