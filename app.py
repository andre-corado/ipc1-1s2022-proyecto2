from flask import Flask
from flask_cors import CORS
from Prestamista.routes.prestamista_routes import prestamista
from Libro.routes.libro_routes import libro
from Prestamo.routes.prestamos_routes import prestamo

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return {'msg': 'Esta es una api que funciona! Bienvenido al lobby uwu.'}

app.register_blueprint(prestamista)
app.register_blueprint(libro)
app.register_blueprint(prestamo)

if __name__ == '__main__':
    app.run(debug=True)