from flask import Blueprint, jsonify, request
import datetime
from BaseDeDatos.database import DB
from Prestamo.models.prestamo_model import Prestamo

prestamo = Blueprint('prestamo', __name__)


# ------------------------PRESTAR LIBRO---------------------------------
@prestamo.route('/borrow', methods=['POST'])
def prestar():
    BODY = request.get_json()
    try:
        if "cui" in BODY and "isbn" in BODY:
            prestamista = DB.getPrestamista(BODY["cui"])
            if prestamista != None:
                libro = DB.getLibro(int(BODY["isbn"]))
                if libro != None:
                    if len(prestamista.getLibros()) == 0:
                        if (libro.hayCopiasDisponibles()):
                            prestamo = Prestamo(int(BODY["isbn"]), DB.TituloDeLibroPrestamo(int(BODY["isbn"])),
                                                BODY["cui"])
                            DB.agregarPrestamo(prestamo)
                            prestamista.agregarPrestamo(prestamo)
                            prestamista.agregarLibro(libro)
                            return {'msg': f" UUID: '{prestamo.getUuid()}' Préstamo exitoso."}, 201
                        return {'msg': 'No hay copias disponibles'}, 400
                    else:
                        return {'msg': f"Cui: '{prestamista.getCui()}' tiene un préstamo pendiente"}, 400
                else:
                    return {'msg': 'ISBN no ingresado en la base de datos.'}, 400
            else:
                return {'msg': 'Cui no existente en el sistema'}, 400
        else:
            return {'msg': 'Faltan campos en la petición'}, 400
    except:
        return {'msg': 'Ocurrió un error en el sevidor'}, 500


# --------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------DEVOLVER LIBRO------------------------------------------------------------
@prestamo.route('/borrow/<uuid>', methods=['PATCH'])
def devolver(uuid):
    try:
        prestamista = DB.VerificarUUid(uuid)
        if (prestamista != None):
            if(len(prestamista._libros) != 0):
                time = datetime.datetime.now()
                prestamo = DB.buscarPrestamo(uuid)
                prestamo._return_date = datetime.datetime.now()
                prestamista._libros = []
                libro = DB.buscarLibro(uuid)
                libro.sumarCopias()
                return {'msg': 'Libro devuelto con exito!'}, 200
            else:
                return {'msg': f"El prestamista no tiene el libro del préstamo: '{str(uuid)}'."}, 400
        else:
            return {'msg': f"El prestamo id. '{str(uuid)}' no existe."}, 400
    except:
        return {'msg': 'Ocurrio un error en el sevidor'}, 500
# --------------------------------------------------------------------------------------------------------------------------------------
