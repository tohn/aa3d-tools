# dm2txt

I'm very fascinated by [autostereograms][], especially [single image
random dot (auto)stereogram][sirds]s (SIRDS) where no equipment is
needed to view a 3d image within a single image by using random dots
(pixels).

But only just recently I discovered [single image random text
(auto)stereogram][sirts]s (SIRTS), which are of course also very fun and
nerdy to look at ;-)

With the small program [`aa3d`][aa3d] it's possible to convert 3d txt
files into a SIRTS. A few examples for such txt files [are listed
here][aa3dexamples].

But it's quite inconvenient to create these txt files, so I created a
small python script (my first!) based on [asciify][] to convert a
depth map image like [`dm.png`][dm.png] to a 3d txt map to be used by
`aa3d`.

## Installation

### Native

Supported are only Arch Linux ([`yay`][yay]) and Debian/Ubuntu
(`apt-get`).  
First install `aa3d`, [`python`][python] and
[`pip`][pip]:

```bash
yay -S aa3d python python-pip # Arch Linux with yay as AUR helper
apt-get -y install aa3d python3 python3-pip # Debian/Ubuntu
```

Afterwards install [`pillow`][pillow] via `pip`:

```bash
pip install pillow
```

### Docker

With [`docker`][docker] installed, we can use it and the provided
`Dockerfile` to install `python`, `pip`, `pillow`, `aa3d` and
`dm2txt.py` and tag the image with `aa3d`.  
I used `python:buster` (Debian 10 with Python 3) as the base image.

```bash
docker build -t aa3d .
```

## Usage

Now you can use `dm2txt.py` to convert an image ([`dm.png`][dm.png]) to
a 3d txt map and use `aa3d` to convert the map to a [SIRTS][sirts].

`dm2txt.py` accepts at least an image file as the first parameter.

The second parameter can be used to set the width of the resulting "txt
image" since an image with a width of 1920 wouldn't look good on a
terminal.

The third parameter can be used to set the number of layers used by
`aa3d`. Only 10 are possible with 0 as the lowest layer (aka the
background) and 9 as the highest one. The input has to be in the range
0-9.

The parameters of `aa3d` are described in [`man 1 aa3d`][aa3dman].

```bash
aa3d <heart.txt
./dm2txt.py dm.png | aa3d -d
./dm2txt.py dm.png 80 3 | aa3d -t tohn
```

With the docker image `aa3d` we can now mount the folder `pwd` (use
`(pwd)` instead of `$(pwd)` in [`fish`][fish]) and run the same commands
as above.

```bash
docker run --rm -v $(pwd):/opt -i aa3d /usr/bin/aa3d <heart.txt
docker run --rm -v $(pwd):/opt -i aa3d /bin/bash -c "./dm2txt.py dm.png | aa3d -d"
docker run --rm -v $(pwd):/opt -i aa3d /bin/bash -c "./dm2txt.py dm.png 80 3 | aa3d -t tohn"
```

## Sources

* [dm.png][]
* [heart.txt][aa3dexamples] (`heart_n_heart`)

[aa3d]: http://aa-project.sourceforge.net/aa3d/
[aa3dexamples]: http://mewbies.com/geek_fun_files/aa3d/aa3d_3dmaps_input_examples.txt
[aa3dman]: https://manpages.ubuntu.com/manpages/bionic/man1/aa3d.1.html
[asciify]: https://github.com/RameshAditya/asciify
[autostereograms]: https://en.wikipedia.org/wiki/Autostereogram
[dm.png]: https://blender.stackexchange.com/questions/132810/rendering-depth-map-that-is-linear-aliased-normalized
[docker]: https://www.docker.com/
[fish]: https://fishshell.com/
[pillow]: https://pillow.readthedocs.io/en/stable/
[pip]: https://pypi.org/project/pip/
[python]: https://www.python.org/
[sirds]: https://en.wikipedia.org/wiki/SIRDS
[sirts]: https://en.wikipedia.org/wiki/ASCII_stereogram
[yay]: https://github.com/Jguer/yay
