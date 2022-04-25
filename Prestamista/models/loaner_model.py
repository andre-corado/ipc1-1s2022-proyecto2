class loaner_model:
    def __init__(self, cui, name, lastName):
        self.__cui = cui
        self.__name = name
        self.__lastName = lastName
        self.__books = []
        self.__record = []

    def addBook(self, book):
        self.__accounts.append(book)

    def addLoan(self, loan):
        self.__record.append(loan)

    def getCui(self):
        return self.__cui

    def getName(self):
        return self.__name

    def getLastName(self):
        return self.__lastName

    def getBook(self, ssidBook):
        for book in self.__books:
            if book.getUuid() == ssidBook:
                return book
        return None

    def getData(self):
        list_account = []
        for acc in self.__accounts:
            list_account.append(acc.getData())
        return {
            "cui": self.__cui,
            "name": self.__name,
            "lastName": self.__lastName,
            "accounts": list_account
        }