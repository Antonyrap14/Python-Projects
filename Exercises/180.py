books = [
    {"title": "Book A", "author": "Author A", "pages": 200},
    {"title": "Book B", "author": "Author B", "pages": 50},
    {"title": "Book C", "author": "Author C", "pages": 150},
    {"title": "Book D", "author": "Author D", "pages": 320},
    {"title": "Book E", "author": "Author E", "pages": 100}
]


def pagine_tra_100_e_300(books):
    books_under300 = [
        book for book in books if 100 <= book["pages"] <= 300
    ] 
    print(books_under300)

pagine_tra_100_e_300(books)