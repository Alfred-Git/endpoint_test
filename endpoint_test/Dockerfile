# Usa Alpine como base
FROM alpine:latest

# Actualiza el sistema y instala dependencias
RUN apk update && apk add --no-cache \
    python3 \
    py3-pip \
    build-base

# Crea un entorno virtual (opcional)
RUN python3 -m venv /venv

# Instala Flask y Requests usando pip
RUN /venv/bin/pip install flask requests

# Copia el archivo de tu aplicación Flask (si lo tienes)
COPY app.py /app/app.py

# Define el directorio de trabajo
WORKDIR /app

# Exponer el puerto donde correrá Flask (normalmente el 5000)
EXPOSE 5000

# Define la variable de entorno para Flask
ENV FLASK_APP=app.py

# Comando para iniciar Flask (actualízalo si es necesario)
CMD ["/venv/bin/flask", "run", "--host=0.0.0.0"]
