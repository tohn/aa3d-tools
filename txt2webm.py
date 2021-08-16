#!/usr/bin/env python
"""move a text depth map around (left to right only at the moment) and
output as a SIRTS webm"""

# TODO more movements (right to left, up to down, down to up, random,
# ping pong, ...)

# inspiration:
# http://www.kammerl.de/ascii/AsciiStereoMovie.php

import sys, os, subprocess

# main
#   - takes as parameters the txt file path
if __name__ == '__main__':
    # try to load txt file
    try:
        txt      = open(sys.argv[1], "r")
        pathname = os.path.dirname(sys.argv[1])
        basename = os.path.basename(sys.argv[1])
        ( _pn := '.' ) if pathname == '' else ( _pn := pathname )
        bn       = _pn + '/' + os.path.splitext(basename)[0]
    except IndexError:
        print("No txt file given")
        sys.exit(1)
    except IOError:
        print("Unable to load txt file")
        sys.exit(1)

    # store in content
    content = txt.readlines()

    # close file again
    txt.close()

    # check for requirements on system
    for cmd in [ 'convert', 'ffmpeg' ]:
      subprocess.run('command -v ' + cmd + ' >/dev/null 2>&1 || exit 1',
              shell=True, check=True)
    # don't use docker, if aa3d is available on the system
    docker = 0
    try:
      subprocess.run('command -v aa3d >/dev/null 2>&1 || exit 1',
            shell=True, check=True)
    except subprocess.CalledProcessError:
      docker = 1

    # check if the lines in the file have all the same length
    # https://stackoverflow.com/a/36596039/2642656
    length = len(content[0])
    if all(len(line) == length for line in content):
        pass
    else:
        print("Lines don't always have the same length")
        sys.exit(1)

    # iterate over the length of the file
    #   shift the file one letter and write to new file
    for _len in range(length):
      filename = bn + '_' + str(_len).zfill(len(str(length))) + '.txt'
      f = open(filename, "w")
      for i in range(len(content)):
        _line = content[i].strip()
        # https://www.geeksforgeeks.org/python-shift-last-element-to-first-position-in-list/
        f.write(_line[_len:] + _line[:_len] + '\n')
      f.close()
      # convert the file to a SIRTS with aa3d and put the output in an
      # image
      # TODO parameters for `aa3d` and `convert`
      (_font := 'DejaVu-Sans-Mono') if docker == 0 else (_font := 'Courier')
      _convert = ' | convert -background black -fill white -font ' + _font + \
        ' -pointsize 14 -border 10 -bordercolor black label:@- ' \
        + os.path.splitext(filename)[0] + '.png >/dev/null 2>&1'
      if docker == 0:
        subprocess.run('aa3d <' + filename + _convert,
                shell=True, check=True)
      else:
        subprocess.run('docker run --rm -v $(pwd):/opt -i ghcr.io/tohn/aa3d aa3d <'
              + filename + _convert, shell=True, check=True)

    # create WebM file
    # TODO parameters for `ffmpeg`
    subprocess.run('ffmpeg -framerate 30 -f image2 -i ' + bn + '_%0' +
            str(len(str(length))) + 'd.png -c:v libvpx-vp9 -pix_fmt yuva420p '
            + bn + '.webm', shell=True, check=True)
