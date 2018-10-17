from flask import Flask, jsonify, request, Response
import json
from settings import *
from BookModel import *

def validBookObject(bookObject):
    if ("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return False
books = [
    {
        'name': 'green streets',
        'price': 7.99,
        'isbn': 98323232
    },
    {
        'name': 'famous streets',
        'price': 7.99,
        'isbn': 124502234
    }
]

def checkBookToEdit(bookObject):
    if("name" in bookObject and "price" in bookObject):
        return True
    else:
        return False

print(__name__)

#GET books
@app.route('/books')
def get_books():
    return jsonify({'books': books})

#GET  /books
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    retun_value = {}
    for book in books:
        if book['isbn'] == isbn:
            return_value = {
                'name': book['name'],
                'price': book['price'],
                'isbn': book['isbn'],
            }
    return jsonify(return_value)

#POST /books
# use (request.get_json()) to get the user input
@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()
    if(validBookObject(request_data)):
        # cherry pick what the user suppose to insert
        # instead of accepting uncessary input attributes
        new_book = {
            "name": request_data['name'],
            "price": request_data['price'],
            "isbn": request_data['isbn']
        }
        books.insert(0, new_book)
        response = Response("",201,mimetype='application/json')
        # used to set the location header correctly, view this in postman
        response.headers['Location'] = "/books/" + str(new_book['isbn'])
        # returning text automatically sets the status code to 200
        return response
    else:
        invalidBookErrorMsg = {
            "error": "Invalid book object passed in the request",
            "helpstring": "name': 'green streets', 'price': 7.99, 'isbn': 98323232"
        }
        response = Response(json.dumps(invalidBookErrorMsg), status=400, mimetype='application/json')
        return response
       
## PUT
@app.route('/books/<int:isbn>', methods=['PUT'])
def updateBook(isbn):
    request_data = request.get_json()
    if (not checkBookToEdit(request_data)):
        invalidBookErrorMsg = {
                "error": "Invalid book object passed in the request",
                "helpstring": "name': 'green streets', 'price': 7.99, 'isbn': 98323232"
            }
        response = Response(json.dumps(invalidBookErrorMsg), status=400, mimetype='application/json')
        return response

    updateDetails = {
        "name": request_data['name'],
        "price": request_data['price'],
        "isbn": isbn
    }
    i = 0
    for book in books:
        current_isbn = book['isbn']
        if current_isbn == isbn:
            books[i] = updateDetails
        i += 1
    
    response = Response("", status=204)
    return response

##PATCH
# {
#     "name": "name of book",
#     "price": "7.99"
# }

@app.route('/books/<int:isbn>', methods=['PATCH'])
def updateBookByParts(isbn):
    request_data = request.get_json()
    updated_book = {}
    if("name" in request_data):
        updated_book["name"] = request_data["name"]
    if ("price" in request_data):
        updated_book["price"] = request_data["price"]
    for book in books:
        if book["isbn"] == isbn:
            book.update(updated_book)
    response = Response("", status=204)
    response.headers["Location"] = "/books/" + str(isbn)
    return response


@app.route('/books/<int:isbn>', methods=['DELETE'])
def delete_book(isbn):
    i = 0
    for book in books:
        if (book['isbn'] == isbn):
            books.pop(i)
            return jsonify(books)
        i += 1
    invalidBookErrorMsg ="Book could not be deleted"
    response = Response(json.dumps(invalidBookErrorMsg), status=404, mimetype="application/json")
    return response

    
app.run(port=5000)
