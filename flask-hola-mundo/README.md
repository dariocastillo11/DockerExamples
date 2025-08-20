# 🐍 Hola Mundo con Flask

## 📋 Descripción
Un servidor web minimalista construido con Flask que responde con mensajes de saludo. Perfecto para aprender los conceptos básicos de Docker con Python.

## 💡 Warning
Las siguientes `warnings` son para crear el `dockerfile`
 * No olvidar copiar los files `requirements.txt` y `app.py` dentro del docker
 * No olvidar instalar las dependencias durante el building del `docker image`
````bash
# Ejecutar el comando
pip install --no-cache-dir -r requirements.txt
````
 * Se tiene que exponer el `port` 5000. Podes hacerlo usando
````bash
# Exponer  el puerto 5000
EXPOSE 5000
````
 * Es fundamental que se ejecute el comando `CMD` al runnear de la `docker image`
````bash
# Ejecutar el proyecto
python app.py
````

## 🚀 Actividades
Deben hacer el `DOCKER_SETUP.md` teniendo las siguientes consideraciones
 * ¿Qué pasa si corremos la `docker image` sin asignar ninguna flag a `docker run`? ¿Podemos usar la misma terminal para correr otros comandos?
 * El proyecto usa el usa el port `5000`. Intentar hacer `docker run` con y sin los parametros correspondientes. ¿Qué ocurre en cada caso?
 * Ejecutar `docker stop <container>`. ¿Qué pasa si al hacer `docker run` no le asigno un nombre al contenedor? ¿Qué debo poner en `<container>`para poder hacer `docker stop <container>`?
 * Si corro el contenedor en segundo plano, no veo información de la dirección IP que necesito para usar mi proyecto. Documentar qué se debe poner en el navegador
```bash
# Construir la imagen
docker build -t flask-hola .

# Ejecutar el contenedor
docker run -d -p 5000:5000 --name flask-app flask-hola

# Probar la aplicación (curl opcional, podes entrar desde el navegador)
curl http://localhost:5000
curl http://localhost:5000/saludo/Maria
