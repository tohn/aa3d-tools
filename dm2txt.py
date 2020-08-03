#!/usr/bin/env python
"""convert a depth map image to a 3d txt map to be used by `aa3d`"""

# inspiration:
# https://github.com/RameshAditya/asciify/blob/master/asciify.py

import sys
try:
    from PIL import Image
except ImportError:
    print("Unable to import pillow")
    sys.exit(1)

# main
#   - takes as parameters the image path [width and intensity]
#   - converts an image to a txt map
#   - prints result to console
if __name__ == '__main__':
    # try to load image
    try:
        image = Image.open(sys.argv[1])
    except IndexError:
        print("No image given")
        sys.exit(1)
    except IOError:
        print("Unable to load image")
        sys.exit(1)
    # set width (default: 80), in the range of 1-500
    try:
        WIDTH = max(1, min(abs(int(sys.argv[2])), 500))
    except (IndexError, ValueError):
        WIDTH = 80
    # set layers (default: 9), in the range of 1-9
    try:
        LAYERS = max(1, min(abs(int(sys.argv[3])), 9))
    except (IndexError, ValueError):
        LAYERS = 9
    # resize image
    image.thumbnail((WIDTH, WIDTH))
    # greyscale (8-bit pixels, black and white) since the input should
    # be like this anyways (this will also provide just one integer in
    # the range of 0-255 instead of a tuple)
    image = image.convert('L')
    # convert every pixel to a value 0-9 corresponding to their intensity
    pixels = [list(map(str, range(0, 9)))[p//(256//LAYERS)] for p in list(image.getdata())]
    # and join the result
    PIXELS_RES = ''.join(pixels)
    # construct the image from the character list
    new_image = [PIXELS_RES[i:i+WIDTH] for i in range(0, len(PIXELS_RES), WIDTH)]
    # and print the resulting lines
    print('\n'.join(new_image))
