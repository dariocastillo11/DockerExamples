# 🌐 Servidor Web Estático con Nginx

## 📋 Descripción
Servidor web que sirve archivos HTML, CSS y JavaScript estáticos usando Nginx. Ideal para aprender a servir contenido web con Docker.

## 💡 Warning
Las siguientes `warnings` son para crear el `dockerfile`
 * No olvidar copiar el file `nginx.conf` dentro de `/etc/nginx/nginx.conf` y folder `public/` dentro de `/usr/share/nginx/html` en el docker
 * Se tiene que exponer el `port` 80. Podes hacerlo usando
````bash
# Exponer  el puerto 5000
EXPOSE 80
````
 * Es fundamental que se ejecute el comando `CMD` al runnear la `docker image`
````bash
# Ejecutar el proyecto
nginx -g "daemon off;"
````

## 🚀 Actividades
Deben hacer el `DOCKER_SETUP.md` teniendo las siguientes consideraciones
 * ¿Qué pasa si corremos la `docker image` sin asignar ninguna flag a `docker run`? ¿Podemos usar la misma terminal para correr otros comandos?
 * El proyecto usa el port `80` ¿Qué parametro se tiene que usar en `docker run`?. Intentar hacer `docker run` con y sin el parametro correspondiente. ¿Qué ocurre en cada caso?
 * Ejecutar `docker stop <container>`. ¿Qué pasa si al hacer `docker run` no le asigno un nombre al contenedor? ¿Qué debo poner en `<container>`para poder hacer `docker stop <container>`?
 * Si corro el contenedor en segundo plano, no veo información de la dirección IP que necesito para usar mi proyecto. Documentar qué se debe poner en el navegador
```bash
# Construir
docker build -t nginx-static .

# Ejecutar
docker run -d -p 8080:80 --name static-server nginx-static

# Acceder
# Abre: http://localhost:8080
