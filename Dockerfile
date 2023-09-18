# Usar una imagen base de Python 3
FROM python:3.11-slim

# Actualizar el sistema y las bibliotecas
RUN apt-get update && apt-get upgrade -y

# Instalar las dependencias necesarias para WeasyPrint y Python
RUN apt-get install -y libgirepository1.0-dev gcc libcairo2-dev libffi-dev pkg-config gir1.2-gtk-3.0 \
    python3-dev libpango1.0-dev libgdk-pixbuf2.0-dev libxml2-dev libxslt-dev default-libmysqlclient-dev

# Copiar requirements.txt y instalar dependencias
COPY requirements.txt .
RUN pip3 install --upgrade pip

RUN pip3 install --no-cache-dir -r requirements.txt

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el contenido del directorio actual (en tu máquina) al contenedor
COPY . .