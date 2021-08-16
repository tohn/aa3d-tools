FROM python:buster
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		aa3d=1.0-8+b2 \
		imagemagick \
		ffmpeg \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& pip install --no-cache-dir pillow==8.3.1 \
	&& rm -fv /etc/ImageMagick-6/policy.xml
WORKDIR /opt
COPY dm2txt.py /usr/local/bin
COPY txt2webm.py /usr/local/bin
