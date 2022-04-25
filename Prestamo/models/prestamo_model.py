from uuid import uuid4
import datetime

#El prestamo crea un UUID el cual es de tipo objeto
#datetime Toma la hora en el momento en que se llama el objeto (hora acutal)
class Prestamo():
    def __init__(self, isbn, title, cui):
        self.__uuid = uuid4()
        self.isbn = isbn
        self._title = title
        self._lend_date = datetime.datetime.now()
        self._return_date = None
        self.cui = cui

    
    def setHoraDevolucion(self, hora):
        self._devuelto = hora

    def getUuid(self):
        return self.__uuid

    def getCuiP(self):
        return self.cui

    def getIsbnP(self):
        return self.isbn
        
    def getDatos(self):
        return {
            "uuid": self.__uuid,
            "isbn": self.isbn,
            "title": self._title,
            "lend_date": self._lend_date,
            "return_date": self._return_date
        }