# SWAPI
## The Star Wars API

Source code for [swapi.co](https://swapi.co)

[![Circle CI](https://circleci.com/gh/phalt/swapi.svg?style=svg)](https://circleci.com/gh/phalt/swapi)

# This is an Docker Image Ready version

~~~
docker run -d -p 8000:8000 codegazers/swapi:slim
~~~

# To change API path (for development, testing, etc...) use BASE_API_PATH environment variable:
~~~
docker run -p 8000:8000 -e BASE_API_PATH="dev" -d codegazers/swapi:slim
~~~
This creates a container with API listening  on 8000 and path /dev/api
```
curl http://0.0.0.0:8000/dev/api/planets/
```

