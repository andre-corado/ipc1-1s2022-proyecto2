from flask import Blueprint, jsonify, request
from BaseDeDatos.database import DB
from Libro.models.libro_model import Libro

libro = Blueprint('libro', __name__, url_prefix='/book')


#   -------CREAR LIBRO-----------

@libro.route('', methods=['POST'])
def crear():
    BODY = request.get_json()
    try:
        if (
                "isbn" in BODY and "author" in BODY and "title" in BODY and "year" in BODY and "no_copies" in BODY and "no_available_copies" in BODY):
            if BODY["no_copies"] >= 0 and BODY["no_available_copies"] >= 0:
                libro = Libro(BODY["isbn"], BODY["author"], BODY["title"], BODY["year"], BODY["no_copies"],
                              BODY["no_available_copies"])
                if (DB.CrearLibro(libro)):
                    return {'msg': 'Libro creado exitosamente'}, 201
                return {'msg': 'Ya existe un libro con ese ISBN.'}, 400
            else:
                return {'msg': 'El número en las copias  no es válido.'}, 400
        else:
            return {'msg': 'Faltan campos en el cuerpo/body de la petición'}, 400
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500


# -------------------------------------------------------ACTUALIZAR UN LIBRO--------------------------------------------------------
@libro.route('', methods=['PUT'])
def actualizar():
    BODY = request.get_json()
    try:
        if "isbn" in BODY and "author" in BODY and "title" in BODY and "year" in BODY:
            isbnlibro = BODY["isbn"]
            author = request.json["author"]
            title = request.json["title"]
            year = request.json["year"]
            if DB.ActualizarLibro(isbnlibro, author, title, year):
                return {'msg': 'Libro modificado con exito'}, 200
            return {'msg': 'No existe un libro con el ISBN ingresado.'}, 400
        else:
            return {'msg': 'Faltan campos en el cuerpo de la petición.'}, 400
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500


# -------------------BUSCAR LIBRO-------------------

@libro.route('', methods=['GET'])
def Buscar():
    try:
        libroslista = DB.BuscarPorTitulo(str(request.args.get('title')))

        return jsonify(libroslista), 200
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500
# -------------------------------------------------------------------------------------------------------------------------------------------------
