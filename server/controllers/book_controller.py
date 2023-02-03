class BookController:
    def getAllBooks(self):
        """
        :return: All books information.
        """
        from server.models.book import BookModel
        bm = BookModel()
        return bm.getAllBooks()

    def getBookById(self, bookId):
        """
        :param bookId: Book id to search.
        :return: Searched book info.
        """
        from server.models.book import BookModel
        bm = BookModel()
        return bm.getBookById(bookId)

    def createBook(self, bookName, bookAuthor, publication):
        """
        :param bookName: New book name.
        :param bookAuthor: Who written the book.
        :param publication: Who public the book.
        :return: Book created success or crash.
        """
        from datetime import datetime
        from server.models.book import BookModel
        from server.models.book import bookStruct
        bm = BookModel()
        count = len(bm.getAll())
        try:
            del bookStruct["_id"]
        except:
            pass
        bookStruct["bookId"] = count
        bookStruct["bookName"] = bookName
        bookStruct["bookAuthor"] = bookAuthor
        bookStruct["publication"] = publication
        bookStruct["deleted"] = False
        bookStruct["createdDate"] = str(datetime.now())
        bookStruct["updatedDate"] = str(datetime.now())
        print(bookStruct)
        bm.createBook(bookStruct)
        return {
            "success": True,
            "message": "Successfully created the book"
        }

    def deleteBook(self, bookId):
        """
        :param bookId: Book id for delete book.
        :return: Book deleted success or crash.
        """
        from server.models.book import BookModel
        bm = BookModel()
        bm.deleteBookById(bookId)
        return {
            "success": True,
            "message": "Successfully deleted the book"
        }

    def updateBook(self, bookId, bookName=None, bookAuthor=None, publication=None):
        """
        :param bookId: Book id of updating book.
        :param bookName: New book name.
        :param bookAuthor: New book author.
        :param publication: New book publisher.
        :return:
        """
        from server.models.book import BookModel
        bm = BookModel()
        bm.updateBookById(bookId=bookId, bookName=bookName, bookAuthor=bookAuthor, publication=publication)
        return {
            "success": True,
            "message": "Successfully updated the book"
        }
