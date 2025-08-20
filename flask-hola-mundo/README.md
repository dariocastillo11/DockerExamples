# 🐍 Hola Mundo con Flask

## 📋 Descripción
Un servidor web minimalista construido con Flask que responde con mensajes de saludo. Perfecto para aprender los conceptos básicos de Docker con Python.

## 💡 Warning
Las siguientes `warnings` son para crear el `docker image`
 * No olvidar copiar los files `requirements.txt` y `app.py` dentro del docker
 * No olvidar instalar las dependencias antes del building del `docker image`
````bash
# Ejecutar el comando
pip install --no-cache-dir -r requirements.txt
````
 * Se tiene que exponer el `port` 5000. Podes hacerlo usando
````bash
# Exponer  el puerto 5000
EXPOSE 5000
````
 * Es fundamental que se ejecute el comando `CMD` al finalizar el buildeo de la `docker image`
````bash
# Ejecutar el proyecto
python app.py
````

## 🚀 Cómo usar
```bash
# Construir la imagen
docker build -t flask-hola .

# Ejecutar el contenedor
docker run -d -p 5000:5000 --name flask-app flask-hola

# Probar la aplicación (curl opcional, podes entrar desde el navegador)
curl http://localhost:5000
curl http://localhost:5000/saludo/Maria
