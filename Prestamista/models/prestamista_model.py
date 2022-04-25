#Si self._EstadoPrestamo es True significa que puedo prestar libro con ese CUI
#Si self._EstadoPrestamo es False se bloqueara la funcion de crear prestamo para ese CUI
class Prestamista():
    def __init__(self, cui, last_name, first_name):
        self.cui = cui
        self.last_name = last_name
        self.first_name = first_name
        self._prestamos = []
        self._libros = []


    def getLibros(self):
        return self._libros

    def agregarLibro(self, libro):
        self._libros.append(libro)

    def agregarPrestamo(self, prestamo):
        self._prestamos.append(prestamo)

    def getCui(self):
        return self.cui

    def getApellido(self):
        return self.last_name

    def getNombre(self):
        return self.first_name

    def getPrestamo(self):
        return self._prestamos

    def getrecord(self):
        record = []
        if self._prestamos is None:
            return record
        for p in self._prestamos:
            record.append(p.getDatos())
        return record

    def getDatos(self):
        return {
            "cui": self.cui,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "record": self.getrecord()
        }