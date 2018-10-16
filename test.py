def validBookObject(bookObject):
if("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
    return True
else:
    return False

validObject = {
    'name': 'good name',
    'price': 6.99,
    'isbn': 53782833
}

missingName = {
    'price': 6.63,
    'isbn': 53433234
}

missingPrice = {
    'price': 5.42,
    'isbn': 35323433
}
