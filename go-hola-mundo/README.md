# 🐹 Hola Mundo con Go

## 📋 Descripción
Servidor web minimalista escrito en Go. Perfecto para aprender Docker con el lenguaje Go.

## 💡 Warning
Las siguientes `warnings` son para crear el `docker image`
 * Se recomienda empezar desde la siguiente imagen: `golang:1.19-alpine`
 * No olvidar copiar los files `go.mod` y `main.go` dentro del docker
 * No olvidar buildear el proyecto antes del building del `docker image`
````bash
# Ejecutar el comando
go build -o main .
````
 * Se tiene que exponer el `port` 8080. Podes hacerlo usando
````bash
# Exponer  el puerto 5000
EXPOSE 8080
````
 * Es fundamental que se ejecute el comando `CMD` al finalizar el buildeo de la `docker image`
````bash
# Ejecutar el proyecto
./main
````

## 🚀 Cómo usar
```bash
# Construir la imagen
docker build -t flask-hola .

# Ejecutar el contenedor
docker run -d -p 8080:8080 --name go-server go-app

# Probar la aplicación (curl opcional, podes entrar desde el navegador)
curl http://localhost:8080
curl "http://localhost:8080/saludo?nombre=Juan"
