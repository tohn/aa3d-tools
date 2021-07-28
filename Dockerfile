FROM python:buster
RUN apt-get update \
	&& apt-get install -y --no-install-recommends aa3d=1.0-8+b2 \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& pip install --no-cache-dir pillow==8.3.1
WORKDIR /opt
COPY dm2txt.py .
