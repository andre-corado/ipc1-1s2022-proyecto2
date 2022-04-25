class Libro():
    def __init__(self, isbn, author, title, year, no_copies,  no_available_copies):
        self.isbn = isbn
        self.author = author
        self.title = title
        self.year = year
        self.no_copies = no_copies
        self.no_available_copies = no_available_copies

    def getIsbn(self):
        return int(self.isbn)
    
    def getTitle(self):
        return str(self.title)

    def getAuthor(self):
        return self.author

    def sumarCopias(self):
        self.no_available_copies += 1
        return True

    def setAuthor(self, NewAuthor):
        self.author = NewAuthor

    def setTitle(self, NewTitle):
        self.title = NewTitle
    
    def setYear(self, NewYear):
        self.year = NewYear

    def hayCopiasDisponibles(self):
        if(self.no_available_copies > 0):
            self.no_available_copies -= 1
            return True
        return False
        
    def getDatos(self):
        return {
            "isbn": self.isbn,
            "author": self.author,
            "title": self.title,
            "year": self.year,
            "no_copies": self.no_copies,
            "no_available_copies": self.no_available_copies
        }