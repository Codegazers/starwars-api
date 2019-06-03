# SWAPI
## The Star Wars API

Source code for [swapi.co](https://swapi.co)

[![Circle CI](https://circleci.com/gh/phalt/swapi.svg?style=svg)](https://circleci.com/gh/phalt/swapi)

# This is an Docker Image Ready version

~~~
docker container run --name swapi \
--restart unless-stopped \
-d \
-p 8000:8000 \
codegazers/swapi:slim
~~~

# It is possible to change API path (for development, testing, etc...) and api version (added version path) using API_VERSION and BASE_API_PATH environment variable:
~~~
docker container run --name swapi \
-p 8000:8000 \
--env BASE_API_PATH="dev" \
--env API_VERSION="v1" \
-d \
--restart unless-stopped \
codegazers/swapi:slim
~~~
This creates a container with API listening  on 8000 and path /dev/api
```
curl http://0.0.0.0:8000/dev/api/planets/
```

