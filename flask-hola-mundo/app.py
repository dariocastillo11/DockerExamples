from flask import Flask
app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '¡Hola Mundo desde Docker! 🐳'

@app.route('/saludo/<nombre>')
def saludar(nombre):
    return f'¡Hola {nombre}! 👋'

@app.route('/info')
def info():
    return {
        'lenguaje': 'Python',
        'framework': 'Flask',
        'version': '2.3.3',
        'mensaje': '¡Funcionando en Docker!'
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)