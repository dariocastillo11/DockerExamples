# 🐳 Actividad de Docker: Desarrollo y Testing entre Grupos

## 📋 Descripción General

¡Bienvenidos a la actividad práctica de Docker! 🎯 En esta experiencia de aprendizaje, trabajarán en equipos para desarrollar y ejecutar aplicaciones utilizando containers de Docker. La actividad se divide en **dos instancias** clave donde cada grupo tendrá la oportunidad de tanto desarrollar como runnear proyectos.

---

## 🎯 Objetivos de la Actividad

- 🧠 **Aprender** a containerizar aplicaciones con Docker
- 🤝 **Trabajar** colaborativamente en equipos
- 🔍 **Ejecutar** contenedores de otros grupos
- 🚀 **Familiarizarse** con el flujo de trabajo de contenedores

---

## 📅 Estructura de la Actividad

### 🔹 Primera Instancia: Desarrollo

1. **Selección de Proyecto** 📂
   - Cada grupo elige un proyecto del repositorio proporcionado

2. **Desarrollo con Docker** 🛠️
   - Deberán codear el **dockerfile**
   - No está permitido instalar frameworks o dependencias directamente en sus máquinas
   - Todo el entorno del sistema debe estar containerizado

3. **Entrega del Proyecto** 📦
   - Al finalizar, prepararán su proyecto para ser ejecutado por otro grupo. Para esto, deberan crear un repositorio en GitHub, subir el proyecto creado, y compartir el link.
   - Deben incluir un `DOCKER_SETUP.md` con instrucciones claras. Este fichero es importante, ya que va a ser la documentación que el otro grupo va a usar para correr el proyecto. Podrán usar alguna herramienta de IA para realizarlo.

### 🔹 Segunda Instancia: Testing Cruzado

1. **Asignación Aleatoria** 🔀
   - El profesor asignará aleatoriamente qué grupo ejecutará cada proyecto

2. **Ejecución del Proyecto Asignado** 🧪
   - Cada grupo recibirá el proyecto de otro equipo
   - Deberán seguir las instrucciones del `DOCKER_SETUP.md` para ejecutarlo

---

## 🚫 Reglas Importantes

### ❌ Restricciones Técnicas
- **No está permitido** instalar frameworks, lenguajes o dependencias directamente en sus equipos
- **Todo** debe ejecutarse through Docker containers
- Si ya tienen algún framework instalado, **deben igualmente utilizar Docker**

### ✅ Requisitos de Entrega
Cada proyecto debe incluir:

1. **Dockerfile** bien documentado
2. **docker-compose.yml** (si aplica)
3. **DOCKER_SETUP.md** con instrucciones de:
   - Cómo construir la imagen
   - Cómo ejecutar el contenedor
   - Cómo verificar que funciona correctamente. Por ejemplo, si es un proyecto front-end pueden contar qué deberían ver en pantalla.
4. **Código fuente** de la aplicación

---

## 📂 Proyectos Disponibles


### 🟢 Nivel Básico
1. **🐍 Hola Mundo con Flask** - Servidor web simple
2. **🌐 Servidor Web Estático** - HTML/CSS con Nginx
3. **📊 Contador de Visitas** - Flask + Redis
4. **🐹 Hola Mundo con Go** - Servidor web simple en Go

### 🟡 Nivel Medio
5. **📈 GNU Octave CLI** - Script matemático simple
6. **📊 Graficador con Matplotlib** - Señal senoidal
7. **🎮 Juego con Pygame** - Juego simple


---

## 🧰 Recursos Adicionales

### 📚 Documentación útil:
- [Docker Documentation](https://docs.docker.com/)
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
- [Docker Compose Reference](https://docs.docker.com/compose/)
- [Notas Docker](https://drive.google.com/file/d/1rUnLn98fu-KZJvF6QfbLh3GFw2AASPeM/view?usp=sharing)

### 🛠️ Herramientas recomendadas:
- **Docker Desktop** (para Windows/Mac)
- **Docker Engine** (para Linux)
- **Visual Studio Code** con extensión de Docker

---

## ❓ Preguntas Frecuentes

### 🤔 ¿Qué pasa si no terminamos a tiempo?
- Entreguen lo que tengan, documentando qué funciona y qué no

### 🤔 ¿Podemos usar contenedores preconstruidos?
- Sí, pueden usar imágenes oficiales de Docker Hub como base

### 🤔 ¿Qué hacer si el proyecto de ejecutamos no funciona?
- Deben hablarlo con el profesor o ayudante de la materia

---

## 🎉 ¡Manos a la obra!

¡Es hora de dockerizar! 🐳💻 Recuerden que el objetivo principal es aprender a trabajar con containers y entender su flujo de trabajo. 

**¡Éxitos a todos!** 🚀

---

*¿Preguntas? Consulten al profesor o al ayudante durante la actividad.* 👨‍🏫👩‍🏫
