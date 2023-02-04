
# Book Shop API
The API allows developers to search for books by book id to retrieve detailed information about each book. The API also allows developers to edit the books and save them to the database.


![Logo](https://telegra.ph/file/a306480e33e287135b0c6.png)


## Features

- Get all books
- Search book
- Update book 
- Create book
- Delete book


## Installation

Creating virtual environment

```bash
py -m pip install --upgrade pip
py -m pip install --user virtualenv
py -m venv env

```
    
Activating virtual environment

```bash
.\env\Scripts\activate
```

install requirements
```bash
pip3 install -r requirements.txt
```


## Run API

Run main.py

```bash
  python main.py
```



## API Reference

#### Get all books

```http
  GET /getAllBooks
```

#### Get book by ID

```http
  GET /getBook
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `bookId`      | `int` | **Required**. Id of the book |

#### Delete book by ID

```http
  GET /deleteBook
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `bookId`      | `int` | **Required**. Id of the book |

#### Create book

```http
  GET /createBook
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `bookName`      | `string` | **Required**. Name of the book |
| `bookAuthor`      | `string` | **Required**. Name of the book author |
| `publication`      | `string` | **Required**. Publication year |

#### Update book by ID

```http
  GET /createBook
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `bookId`      | `string` | **Required**. Name of the book |
| `bookName`      | `string` | Name of the book |
| `bookAuthor`      | `string` | Name of the book author |
| `publication`      | `string` | Publication year |
