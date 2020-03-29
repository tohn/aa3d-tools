#!/usr/bin/env python

# inspiration:
# https://github.com/RameshAditya/asciify/blob/master/asciify.py

import sys
from PIL import Image

'''
main
    - takes as parameters the image path [width and intensity]
    - converts an image to a txt map
    - prints result to console
'''
if __name__ == '__main__':
    # try to load image
    try:
        image = Image.open(sys.argv[1])
    except Exception:
        print("Unable to load image")
        exit(1)
    # set width (default: 80)
    try:
        width = abs(int(sys.argv[2]))
    except Exception:
        width = 80
    # set layers (default: 9), in the range of 1-9
    try:
        layers = max(1, min(abs(int(sys.argv[3])), 9))
    except Exception:
        layers = 9
    # resize image
    image.thumbnail((width,width))
    # greyscale (8-bit pixels, black and white) since the input should
    # be like this anyways (this will also provide just one integer in
    # the range of 0-255 instead of a tuple)
    image = image.convert('L')
    # convert every pixel to a value 0-9 corresponding to their intensity
    pixels = [list(map(str, range(0,9)))[p//(256//layers)] for p in list(image.getdata())]
    # and join the result
    pixels = ''.join(pixels)
    # construct the image from the character list
    new_image = [pixels[i:i+width] for i in range(0, len(pixels), width)]
    # and print the resulting lines
    print('\n'.join(new_image))
