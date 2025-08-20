# 🌐 Servidor Web Estático con Nginx

## 📋 Descripción
Servidor web que sirve archivos HTML, CSS y JavaScript estáticos usando Nginx. Ideal para aprender a servir contenido web con Docker.

## 💡 Warning
Las siguientes `warnings` son para crear el `docker image`
 * No olvidar copiar los files `nginx.conf` dentro de `/etc/nginx/nginx.conf` y folder `public/` dentro de `/usr/share/nginx/html` en el docker
 * Se tiene que exponer el `port` 80. Podes hacerlo usando
````bash
# Exponer  el puerto 5000
EXPOSE 80
````
 * Es fundamental que se ejecute el comando `CMD` al finalizar el buildeo de la `docker image`
````bash
# Ejecutar el proyecto
nginx -g "daemon off;"
````

## 🚀 Cómo usar
```bash
# Construir
docker build -t nginx-static .

# Ejecutar
docker run -d -p 8080:80 --name static-server nginx-static

# Acceder
# Abre: http://localhost:8080
