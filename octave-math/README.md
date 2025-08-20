# 📈 GNU Octave CLI

## 📋 Descripción
Script matemático que ejecuta cálculos numéricos usando GNU Octave. Perfecto para procesamiento científico en Docker.

## 💡 Warning
Las siguientes `warnings` son para crear el `docker image`
 * Se recomienda empezar desde la siguiente imagen: `gnuoctave/octave:7.3.0`
 * No olvidar copiar el file `script.m` dentro del docker
 * Es fundamental que se ejecute el comando `CMD` al finalizar el buildeo de la `docker image`
````bash
# Ejecutar el proyecto
octave script.m
````

## 🚀 Cómo usar
```bash
# Construir la imagen
docker build -t flask-hola .

# Ejecutar el contenedor
docker run -it --rm octave-math
