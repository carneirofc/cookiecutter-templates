FROM {{cookiecutter.docker_base_image}}

ENV TZ=America/Sao_Paulo

EXPOSE 8080

COPY / /app

WORKDIR /app

RUN pip install --verbose -e .

WORKDIR /app
