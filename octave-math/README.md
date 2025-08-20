# 📈 GNU Octave CLI

## 📋 Descripción
Script matemático que ejecuta cálculos numéricos usando GNU Octave. Perfecto para procesamiento científico en Docker.

## 💡 Warning
Las siguientes `warnings` son para crear el `dockerfile`
 * Se recomienda empezar desde la siguiente imagen: `gnuoctave/octave:7.3.0`
 * No olvidar copiar el file `script.m` dentro del docker
 * Es fundamental que se ejecute el comando `CMD` al runnear la `docker image`
````bash
# Ejecutar el proyecto
octave script.m
````

## 🚀 Actividad
Documentar como construir la imagen y ejecutar el contenedor
