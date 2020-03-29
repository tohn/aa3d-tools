FROM python:buster
RUN apt-get update \
	&& apt-get install -y --no-install-recommends aa3d \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& pip install pillow
WORKDIR /opt
COPY dm2txt.py .
