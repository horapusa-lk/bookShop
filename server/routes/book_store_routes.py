from fastapi import APIRouter
from server.controllers.book_controller import BookController
router = APIRouter()
book_controller = BookController()


def returnError(error_code, error_message):
    return {
        "error": {
            "code": error_code,
            "message": error_message
        }

    }


@router.get("/getAllBooks")
def get_all_books():
    try:
        return book_controller.getAllBooks()
    except:
        return returnError(500, "The request failed due to an internal error.")


@router.get("/getBook")
def get_book(bookId: int):
    try:
        return book_controller.getBookById(bookId)
    except:
        return returnError(400, "Invalid book id.")


@router.get("/deleteBook")
def delete_book(bookId: int):
    try:
        book = book_controller.getBookById(bookId=bookId)
        print(book["bookName"])
        return book_controller.deleteBook(bookId=bookId)
    except:
        return returnError(400, "Invalid book id.")


@router.post("/createBook")
def create_book(bookName, bookAuthor, publication):
    if bookName == " " or bookName is None or bookName == "":
        return returnError(400, "Invalid Book Name")
    if bookAuthor == " " or bookAuthor is None or bookAuthor == "":
        return returnError(400, "Invalid Book author")
    if publication == " " or publication is None or publication == "":
        return returnError(400, "Invalid Book publication")
    try:
        return book_controller.createBook(bookName=bookName, bookAuthor=bookAuthor, publication=publication)
    except Exception as e:
        print(e)
        return returnError(500, "The request failed due to an internal error.")


@router.post("/updateBook")
def update_book(bookId: int, bookName=None, bookAuthor=None, publication=None):
    try:
        book = book_controller.getBookById(bookId=bookId)
        print(book["bookName"])
        return book_controller.updateBook(bookId=bookId, bookName=bookName, bookAuthor=bookAuthor, publication=publication)
    except:
        return returnError(400, "Invalid book id.")

