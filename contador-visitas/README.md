# 📊 Contador de Visitas con Flask + Redis

## 📋 Descripción
Aplicación web que cuenta visitas usando Flask como frontend y Redis como base de datos. Todo en un solo contenedor Docker.

## 💡 Warning
Las siguientes `warnings` son para crear el `dockerfile`
 * Se recomienda empezar desde la siguiente imagen: `python:3.9-slim`
 * No olvidar copiar los files dentro del docker
 * No olvidar instalar las dependencias durante el building del `docker image`
````bash
# Ejecutar el comando
apt-get update && apt-get install -y \
    redis-server \
    && rm -rf /var/lib/apt/lists/*

# Este comando tambien es necesario
pip install --no-cache-dir -r requirements.txt
````
 * Se tiene que exponer el `port` 5000. Podes hacerlo usando
````bash
# Exponer  el puerto 5000
EXPOSE 5000
````
 * Se tiene que dar permiso de ejecucion la fichero `start.sh`
````bash
# Asignar permiso de ejecución
chmod +x start.sh
````
 * Es fundamental que se ejecute el comando `CMD` al finalizar el buildeo de la `docker image`
````bash
# Ejecutar el proyecto
./start.sh
````

## 🚀 Actividades
Deben hacer el `DOCKER_SETUP.md` teniendo las siguientes consideraciones
>REDACTAR
```bash
# Construir la imagen
docker build -t contador-visitas .

# Ejecutar el contenedor
docker run -d -p 5000:5000 --name visitas-app contador-visitas

# Probar la aplicación (curl opcional, podes entrar desde el navegador)
curl http://localhost:5000
curl http://localhost:5000/health
curl http://localhost:5000/reiniciar

# Acceder a Redis
docker exec -it visitas-app redis-cli GET visitas
