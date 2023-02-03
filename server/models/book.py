bookStruct = {
    "bookId": "",
    "bookName": "",
    "bookAuthor": "",
    "publication": "",
    "deleted": False,
    "createdDate": "",
    "updatedDate": "",
    "deletedDate": ""
}


class BookModel:
    def createBook(self, book):
        """
        :param book: book structure for add to db.
        :return: added book structure.
        """
        from server.config.mogo import Mongo
        mongo = Mongo()
        mongoDB = mongo.connect()
        mongoDB.insert_one(book)
        return book

    def deleteBookById(self, bookId):
        """
        :param bookId: book id for delete.
        :return: deleted book id.
        """
        from server.config.mogo import Mongo
        from datetime import datetime
        mongo = Mongo()
        mongoDB = mongo.connect()
        myquery = {"bookId": bookId}
        newvalues = {"$set": {
            "deleted": True,
            "deletedDate": str(datetime.now())
        }}
        mongoDB.update_one(myquery, newvalues)
        return bookId

    def updateBookById(self, bookId, bookName = None, bookAuthor = None, publication = None):
        """
        :param bookId: book id.
        :param bookName: new book name.
        :param bookAuthor: new book author.
        :param publication: new book publisher.
        :return: edited book info.
        """
        from server.config.mogo import Mongo
        from datetime import datetime
        mongo = Mongo()
        mongoDB = mongo.connect()
        myquery = {"bookId": bookId}
        set_val = {"bookId": bookId}
        if bookName is not None:
            set_val["bookName"] = bookName
        if bookAuthor is not None:
            set_val["bookAuthor"] = bookAuthor
        if publication is not None:
            set_val["publication"] = publication
        set_val["updatedDate"] = str(datetime.now())
        newvalues = {"$set": set_val}
        mongoDB.update_one(myquery, newvalues)
        return mongoDB.find_one({"bookId": bookId})

    def getBookById(self, bookId):
        """
        :param bookId: book id to find.
        :return: searched book info.
        """
        from server.config.mogo import Mongo
        mongo = Mongo()
        mongoDB = mongo.connect()
        book = mongoDB.find_one({"bookId": bookId})
        res_data = {
            "bookId": book["bookId"],
            "bookName": book["bookName"],
            "bookAuthor": book["bookAuthor"],
            "publication": book["publication"],
            "createdDate": book["createdDate"],
            "updatedDate": book["updatedDate"]
        }
        return res_data

    def getAllBooks(self):
        """
        :return: all available books.
        """
        from server.config.mogo import Mongo
        mongo = Mongo()
        mongoDB = mongo.connect()
        booksObject = mongoDB.find({"deleted": False})
        books = []
        for book in booksObject:
            res_data = {
                "bookId": book["bookId"],
                "bookName": book["bookName"],
                "bookAuthor": book["bookAuthor"],
                "publication": book["publication"],
                "createdDate": book["createdDate"],
                "updatedDate": book["updatedDate"]
            }
            books.append(res_data)
        return books

    def getAll(self):
        """
        :return: all books (deleted books also included).
        """
        from server.config.mogo import Mongo
        mongo = Mongo()
        mongoDB = mongo.connect()
        booksObject = mongoDB.find({"deleted": False})
        books = []
        for book in booksObject:
            res_data = {
                "bookId": book["bookId"],
                "bookName": book["bookName"],
                "bookAuthor": book["bookAuthor"],
                "publication": book["publication"],
                "createdDate": book["createdDate"],
                "updatedDate": book["updatedDate"]
            }
            books.append(res_data)
        return books
