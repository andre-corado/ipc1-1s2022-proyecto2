class Database():
    def __init__(self):
        self._cuiPrestamista = []
        self._prestamistas = []
        self._isbnLibro = []
        self._libros = []
        self._prestamos = []

    #---------------------------------PRESTAMISTA---------------------------------
    def CrearPrestamista(self, prestamista):
        #Añade un registro de un nuevo prestamista a la lista de prestamistas
        if not(prestamista.getCui() in self._cuiPrestamista):
            self._prestamistas.append(prestamista)
            self._cuiPrestamista.append(prestamista.getCui())
            print(self._prestamistas)
            return True
        return False

    def getPrestamista(self, cuiPrestamista):
        if cuiPrestamista in self._cuiPrestamista:
            for prestamista in self._prestamistas:
                if prestamista.getCui() == cuiPrestamista:
                    return prestamista
        return None

    #------------------------------------LIBRO------------------------------------
    def CrearLibro(self, libro):
        if not(libro.getIsbn() in self._isbnLibro):
            self._libros.append(libro)
            self._isbnLibro.append(libro.getIsbn())
            print(self._libros)
            return True
        return False

    def ActualizarLibro(self, isbn, author, title, year):
        if isbn in self._isbnLibro:
            for libro in self._libros:
                if libro.getIsbn() == int(isbn):
                    libro.setAuthor(author)
                    libro.setTitle(title)
                    libro.setYear(year)
                    return True
        return False

    def getLibros(self):
        if self._libros is None:
            return None
        return self._libros

    def BuscarPorTitulo(self, titulo):
        listaLibros = []
        for libro in self._libros:
            if titulo == libro.getTitle():
                listaLibros.append(libro.getDatos())
        return listaLibros

    def BuscarPorAutor(self, autor):
        listaLibros = []
        for libro in self._libros:
            if autor == libro.getAuthor():
                listaLibros.append(libro.getDatos())
        return listaLibros

    def getLibro(self, isbnLibro):
        if int(isbnLibro) in self._isbnLibro:
            for libro in self._libros:
                if libro.getIsbn() == int(isbnLibro):
                    return libro 
        return None
    #-----------------------------------PRESTAMO------------------------------------
    
    def agregarPrestamo(self, prestamo):
        self._prestamos.append(prestamo)
        return True
    
    def TituloDeLibroPrestamo(self, isbn):
        for libro in self._libros:
            if libro.getIsbn() == isbn:
                return libro.getTitle()

    def VerificarUUid(self, uuid):
        for prestamo in self._prestamos:  
            if str(prestamo.getUuid()) == str(uuid):
                for prestamista in self._prestamistas:
                    if prestamo.getCuiP() == prestamista.getCui():
                        return prestamista

    def buscarPrestamo(self, uuid):
        for prestamo in self._prestamos:  
            if str(prestamo.getUuid()) == str(uuid):
                return prestamo

    def buscarLibro(self, uuid):
        for prestamo in self._prestamos:  
            if str(prestamo.getUuid()) == str(uuid):
                for libro in self._libros:
                    if prestamo.getIsbnP() == libro.getIsbn():
                        return libro
            
DB = Database()
