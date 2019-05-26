FROM ubuntu
RUN apt-get update -qq \
&& apt-get install -qq \
python \
make \
python-pip \
libpq-dev \
libmemcached-dev \
zlib1g-dev \
python-pygresql

COPY . /src
WORKDIR /src

RUN make install build load_data

EXPOSE 8000

CMD make serve
