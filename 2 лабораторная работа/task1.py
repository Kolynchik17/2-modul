BOOKS = [
    {
        "id": 1,
        "name": "name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "name_2",
        "pages": 400,
    }
]

class Book:
    def __init__(self, id_, name, pages):
        self.id_ = id_
        self.name = name
        self.pages = pages
        if not (isinstance(self.id_,int) and isinstance(self.name, str) and isinstance(self.pages, int)):
            raise TypeError
        if (self.id_<0 and self.pages<0):
            raise TypeError

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id_}, name={repr(self.name)}, pages={self.pages})'

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
