# 📊 Graficador con Matplotlib

## 📋 Descripción
Aplicación Python que genera gráficos de señales senoidales usando Matplotlib y NumPy. Los gráficos se guardan como archivos PNG.

## 💡 Warning
Las siguientes `warnings` son para crear el `docker image`
 * Se recomienda empezar desde la siguiente imagen: `python:3.9-slim`
 * No olvidar copiar los files dentro del docker
 * No olvidar instalar las dependencias antes del building del `docker image`
````bash
# Ejecutar el comando
pip install --no-cache-dir -r requirements.txt

# Tambien ejecutar el comando
mkdir -p /app/output
````
 * Es fundamental que se ejecute el comando `CMD` al finalizar el buildeo de la `docker image`
````bash
# Ejecutar el proyecto
python graficar.py
````

## 🚀 Cómo usar
```bash
# Construir la imagen
docker build -t flask-hola .

# Ejecutar el contenedor
docker run -it --rm -v $(pwd)/output:/app/output matplotlib-grafico

# Ver el gráfico generado
# El gráfico se guarda en ./output/senoidal.png
