from flask import Blueprint, jsonify, request
from BaseDeDatos.database import DB
from Prestamista.models.prestamista_model import Prestamista

prestamista = Blueprint('prestamista', __name__, url_prefix='/person')


# -------------------------------------CREAR PRESTAMISTA--------------------------------------
@prestamista.route('', methods=['POST'])
def crear():
    BODY = request.get_json()
    try:
        if "cui" in BODY and "last_name" in BODY and "first_name" in BODY:
            prestamista = Prestamista(BODY["cui"], BODY["last_name"], BODY["first_name"])
            if DB.CrearPrestamista(prestamista):
                return {'msg': 'Prestamista creado exitosamente'}, 201
            return {'msg': 'Prestamista duplicado'}, 400
        else:
            return {'msg': 'Faltan campos en el cuerpo de la petición'}, 400
    except:
        return {'msg': 'Ocurrio un error en el servidor'}, 500


# --------------------------------------------------------------------------------------------

# -----------------------------------CONSULTAR PRESTAMISTA------------------------------------
@prestamista.route('/<cui>', methods=['GET'])
def consultar(cui):
    try:
        prestamista = DB.getPrestamista(cui)
        if (prestamista != None):
            return jsonify(prestamista.getDatos()), 200
        else:
            return {'msg': 'No se encontró al prestamista.'}, 400
    except:
        return {'msg': 'Ocurrió un error en el servidor.'}, 500
# --------------------------------------------------------------------------------------------
